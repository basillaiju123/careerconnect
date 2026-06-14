from django.shortcuts import render
from .models import Job
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')


def jobs(request):

    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(title__icontains=search)
    else:
        jobs = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': jobs
    })


from django.shortcuts import render
from .models import Job

def home(request):
    return render(request, 'home.html')


def jobs(request):

    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(title__icontains=search)
    else:
        jobs = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': jobs
    })


from django.shortcuts import render
from .models import Job

def home(request):
    return render(request, 'home.html')


def jobs(request):

    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(title__icontains=search)
    else:
        jobs = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': jobs
    })


from django.shortcuts import render
from .models import Job, Application

def job_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        jobs = Job.objects.filter(
            title__icontains=search_query
        )
    else:
        jobs = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': jobs
    })


from django.shortcuts import render
from .models import Job, Application
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_detail.html', {'job': job})

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        Application.objects.create(
            user=request.user,
            job=job,
            name=name,
            email=email,
            resume=resume
        )

        return render(request, "success.html")

    return render(request, "apply.html", {"job": job})
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('jobs')

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('home')  
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user)

    return render(request, 'my_applications.html', {
        'applications': applications
    })    