from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

job_title = ["First job",
        "Second job", 
        "Third job"]

jobs_descriptions = ["First job description",
                     "Second job description",
                     "Third job description"]

def hello(request):
    #template = loader.get_template("app\hello.html")
    context={"name": "Artur"}
    #return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)

def jobs_list(request):
    # list_of_jobs = "<ul>"
    # for job in job_title:
    #     job_id = job_title.index(job)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs+=f"<li><a href='{detail_url}'>{job}</a></li>\n"
    # list_of_jobs += "</ul>"
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app\job_list.html", context)

# Create your views here.
def job_detail(request, id):
    try:
        # if id == 0:
        #     return redirect(reverse('jobs_home'))
        # context = {'job_title': job_title[id], 
        #            'job_description': jobs_descriptions[id]}
        # return_html = f"<h1>{job_title[id]}</h1><br><h5>{jobs_descriptions[id]}</h5>"
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_page.html", context)
    except:
        return HttpResponseNotFound("Not Found")