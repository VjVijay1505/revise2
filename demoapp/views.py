from django.shortcuts import redirect, render
from .models import Site, Upload
from .forms import SiteForm, UploadForm

# Create your views here.
def home(request):
    projects = Site.objects.all()
    context = {'projects':projects}

    return render(request, 'home.html', context)

def upload(request):
    form = UploadForm()

    if request.FILES:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'demoapp/upload.html')

def add(request):
    form = SiteForm()

    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'demoapp/add.html', context)

def view(request,pk):
    project = Site.objects.get(id=pk)
    context = {'project':project}

    return render(request, 'demoapp/projectview.html', context)

def edit(request,pk):
    project = Site.objects.get(id=pk)
    form = SiteForm(instance=project)

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'demoapp/modify.html', context)

def remove(request,pk):
    project = Site.objects.get(id=pk)
    project.delete()
    return redirect('/')