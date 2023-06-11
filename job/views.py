from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm 

# Create your views here.
def job_list(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj} #this is template name
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug) #get job name

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            updatedForm = form.save(commit=False)
            updatedForm.job = job_detail
            updatedForm.save()
        else:
            print(form.errors)
    else:
        form = ApplyForm()# if no sent button hit then only show form

    context = {'job':job_detail, 'form1':form}
    return render(request, 'job/job_detail.html', context)