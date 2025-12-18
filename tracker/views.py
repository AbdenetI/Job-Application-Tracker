from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View
from django.core.paginator import Paginator

from .forms import RegisterForm, CompanyForm, JobForm, ApplicationForm
from .models import Application
from .filters import ApplicationFilter

class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html', {'form': RegisterForm()})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'auth/register.html', {'form': form})

@login_required
def dashboard(request):
    today = timezone.localdate()
    qs = Application.objects.filter(user=request.user)
    counts = {k: qs.filter(status=k).count() for k, _ in Application.Status.choices}
    upcoming = qs.filter(next_follow_up_on__gte=today).order_by('next_follow_up_on')[:10]
    due = qs.filter(next_follow_up_on__lte=today)
    return render(request, 'tracker/dashboard.html', {
        'counts': counts,
        'upcoming': upcoming,
        'due': due,
    })

@login_required
def application_list(request):
    base_qs = Application.objects.filter(user=request.user).select_related('company', 'job')
    f = ApplicationFilter(request.GET, queryset=base_qs)
    paginator = Paginator(f.qs.order_by('-date_applied', '-created_at'), 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'tracker/application_list.html', {
        'filter': f,
        'page_obj': page_obj,
    })

@login_required
def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            if app.status in [Application.Status.APPLIED, Application.Status.INTERVIEW, Application.Status.OFFER] and not app.date_applied:
                app.date_applied = timezone.localdate()
            app.save()
            return redirect('application_detail', pk=app.pk)
    else:
        form = ApplicationForm()
    return render(request, 'tracker/application_form.html', {'form': form, 'mode': 'Add'})

@login_required
def application_update(request, pk):
    app = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save()
            return redirect('application_detail', pk=app.pk)
    else:
        form = ApplicationForm(instance=app)
    return render(request, 'tracker/application_form.html', {'form': form, 'mode': 'Edit'})

@login_required
def application_detail(request, pk):
    app = get_object_or_404(Application.objects.select_related('company', 'job'), pk=pk, user=request.user)
    return render(request, 'tracker/application_detail.html', {'app': app})

@login_required
def application_status_update(request, pk):
    app = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Application.Status.choices):
            app.status = new_status
            if new_status in [Application.Status.APPLIED, Application.Status.INTERVIEW, Application.Status.OFFER] and not app.date_applied:
                app.date_applied = timezone.localdate()
            app.save()
    return redirect('application_detail', pk=pk)

@login_required
def company_create(request):
    from .forms import CompanyForm
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_create')
    else:
        form = CompanyForm()
    return render(request, 'tracker/company_form.html', {'form': form})

@login_required
def job_create(request):
    from .forms import JobForm
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_create')
    else:
        form = JobForm()
    return render(request, 'tracker/job_form.html', {'form': form})
