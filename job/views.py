from django.shortcuts import render,redirect
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.urls import reverse

# Create your views here.
def job_list(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj} #this is template name
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug) #get job name

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES) #if we're sending files dont forget to put request.FILES
        if form.is_valid():
            updatedForm = form.save(commit=False)#dont save to database
            updatedForm.job = job_detail #
            updatedForm.save()
        else:
            print(form.errors)
    else:
        form = ApplyForm()# if no sent button hit then only show form

    context = {'job':job_detail, 'form1':form}
    return render(request, 'job/job_detail.html', context)


def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST, request.FILES)   
        if form.is_valid():
            updatedForm = form.save(commit=False)
            updatedForm.owner = request.user #owner is coming form job model # غالبا جايه من ملف فورمز وهو بيسيف هناك
            updatedForm.save()
            return redirect(reverse('jobs:job_list'))
        else:
            print(form.errors)
    else:
        form =  JobForm()   

    return render(request, 'job/add_job.html',{'form':form}) # we're sending form from the else statement or first one in if statement 
