from django.shortcuts import render, redirect
from django.urls import path, re_path
import markdown2
from .models import *

def landing(request):
    return render(request, 'courses/matlab/matlab.html')

def index(request):
    try:
        materials = MatlabMaterial.objects.all()
        experiments = MatlabExperiment.objects.all()
        context = {
            'experiments': experiments,
            'materials': materials
        }
        return render(request, template_name="courses/matlab/home.html", context=context)
    except Exception as e:
        return redirect('/')

def exp_detail(request):
    try:
        exp_id = request.GET.get('id')
        if not exp_id:
            return redirect('/courses/calculus-using-matlab/')
        exp_blog = MatlabExperiment.objects.get(id=exp_id)
        markdown_content = exp_blog.blog_file.read().decode('utf-8')
        html_content = markdown2.markdown(markdown_content, extras=["tables", "fenced-code-blocks"])
        context = {'exp': exp_blog, 'blog_content_html': html_content}
        return render(request, 'courses/matlab/experiment_desc.html', context=context)
    except MatlabExperiment.DoesNotExist:
        return redirect('/courses/calculus-using-matlab/')
    except Exception as e: 
        print(f"An error occurred: {e}") 
        return redirect('/courses/calculus-using-matlab/')

def exp_view(request):
    exp_id = request.GET.get("id")
    exp_implementation = MatlabExperiment.objects.get(id=exp_id)
    # print(exp_implementation.exp_data)
    slide_count = [count for count in range(1, len(exp_implementation.exp_data['slides']) + 1)]

    # for i, slide in enumerate(exp_implementation.exp_data['slides']):
    #     exp_implementation.exp_data['slides'][i] = markdown2.markdown(slide['output'], extras=["tables", "fenced-code-blocks"])
    #     print(exp_implementation.exp_data['slides'][i])

    context = {
        "slide_count" : slide_count,
        "exp": exp_implementation
    }
    return render(request,template_name='courses/matlab/experiment_viewer.html', context=context)