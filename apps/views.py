import itertools

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from apps.models import Category, Problems, Task
from apps.services import run_python_code, get_actual_type


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


def problem(request, id):
    problem = get_object_or_404(Problems, id=id)
    if request.method == 'POST':
        code_input = request.POST['code']
        python_output, execution_time, memory_usage = run_python_code(code_input, 5)
        value, actual_type = get_actual_type(python_output)
        problem_value, problem_type = get_actual_type(problem.output)
        if value == problem_value:
            context = {
                'result': 'access',
                'value': value,
                'time': execution_time,
                'memory': memory_usage
            }
        else:
            context = {
                'result': 'error',
                'value': value
            }
        return render(request, 'solution.html',
                      {'problem': problem, 'result': context, 'value': value, 'time': execution_time,
                       'memory': memory_usage})
    # context = {
    #     'problem': problem,
    #
    # }
    examples = dict(itertools.islice(problem.input.items(), 3))
    return render(request, 'solution.html', {"problem": problem, "examples": examples})


def submission(request, id):
    return render(request, 'submission.html')

def about(request):
    return render(request, 'about.html')

def homee(request):
    todos = Task.objects.all()
    return render(request, "task/index.html", {"todo_list": todos, })


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        new_todo = Task.objects.create(title=title)
        return redirect("todo")
    else:
        return HttpResponse("Method not allowed", status=405)


def update(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("todo")


def delete(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")