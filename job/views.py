from django.shortcuts import render,redirect
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.
def job_list(request):
    job_list = job.objects.all()

    #filter # we use filter first before pagination as to pagination works on the filter too
    job_filter = JobFilter(request.GET, queryset= job_list) # filter would get his data to filter on from request.GET, cause we send filter fields by get method from the form # queryset means that im giving him instance from database to filter and search on it
    job_list = job_filter.qs  # we're now overriding job_list to show them in paginator #After the JobFilter instance has been created, you access the filtered queryset using the .qs

    # pagination
    paginator = Paginator(job_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj, 'job_filter':job_filter} #this is template name
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug) #get job name , from job model return object form it where we want slug field

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

@login_required
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

def filtered_job_list(request, category_name):
    jobs = job.objects.filter(category__name=category_name)

    # Other logic for pagination or additional filtering if needed

    context = {
        'jobs': jobs,
    }
    return render(request, 'job/filtered_job_list.html', context)