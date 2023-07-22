import itertools

from django.shortcuts import render, get_list_or_404, get_object_or_404

from apps.models import Category, Problems


def home(request):
    return render(request, 'index.html')


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)


def problems(request, id):
    problems = get_list_or_404(Problems, category_id=id)
    context = {
        'problems': problems
    }
    return render(request, 'problems.html', context)


# def problem(request, title):
#     problem = get_object_or_404(Problems, title=title)
#     if request.method == 'POST':
#         post = request.POST['example']
#         result = post.split("(")[1].split(")")[0]
#         try:
#             result = eval(result)
#         except Exception as e:
#             result = e
#         context = {
#             'result': result
#         }
#         return render(request, 'solution.html', context=context)
#     return render(request, 'solution.html',context={'problem' : problem})


def problem(request,id):
    problem = get_object_or_404(Problems,id=id)
    if request.method == 'POST':
        code_input = request.POST['code']
        output = execute_code(code_input)
        context = {
            'output': output
        }
        return render(request, 'solution.html',context )
    context = {
        'problem': problem
    }
    from itertools import islice
    # for k,v in problem.input.items():
    examples = dict(itertools.islice(problem.input.items(),3))
    return render(request, 'solution.html', {"problem": problem, "examples": examples})






def execute_code(code_input):
    try:
        exec_result = {}
        exec(code_input, {}, exec_result)
        return str(exec_result)
    except Exception as e:
        return str(e)
