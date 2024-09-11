import itertools

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from apps.models import Category, Problems, Task, Submission
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
    submission = Submission.objects.all()
    context = {
        'problems': problems,
        'submissions': submission,
    }

    return render(request, 'problems.html', context)


def problem(request, id):
    problem = get_object_or_404(Problems, id=id)

    if request.method == 'POST':
        c = 0
        for example in problem.example.all():
            problem_output = example.output
            variable_values = example.variable_value.values()

            # Initialize j with a default value like None
            j = None

            # Check if variable_values is empty
            if not variable_values:
                return render(request, 'solution.html', {'error': 'No variable values found to test'})

            # Loop through the variable_values and assign j
            for variable in variable_values:
                j = variable.get('value', None)  # Safely access 'value' key

            # Ensure j has been assigned a valid value
            if j is None:
                return render(request, 'solution.html', {'error': 'No valid variable value found to test'})

            # Now continue with the code execution
            code_input = request.POST['code']
            function = f'\nprint(function({j}))'
            python_output, execution_time, memory_usage = run_python_code(code_input, function, 5)
            value, actual_type = get_actual_type(python_output)
            j, find_type_variable = get_actual_type(j)
            problem_value, problem_type = get_actual_type(problem_output)

            if value == problem_value:
                c += 1
            else:
                context = {
                    'result': 'error',
                    'value': value
                }

                return render(request, 'solution.html', {
                    'problem': problem,
                    'result': context,
                    'value': value,
                    'time': execution_time,
                    'memory': memory_usage,
                    'expected': problem_value,
                    'problem_type': find_type_variable
                })

        # Success case if all examples are correct
        if c == len(problem.example.all()):
            context = {
                'result': 'access',
                'value': value,
                'time': execution_time,
                'memory': memory_usage
            }
            Submission.objects.create(
                problem_id=problem.id,
                user_id=request.user.id,
                answer=code_input
            )
            return render(request, 'solution.html', {
                'problem': problem,
                'result': context,
                'value': value,
                'time': execution_time,
                'memory': memory_usage,
                'expected': problem_value
            })

    # Handle GET requests or when no POST is made
    for example in problem.example.all():
        problem_output = example.output
        variable_values = example.variable_value.values()

        j = None  # Initialize j

        # Check if variable_values is empty
        if not variable_values:
            return render(request, 'solution.html', {'error': 'No variable values found to test'})

        for variable in variable_values:
            j = variable.get('value', None)

    # Ensure j has been assigned a valid value
    if j is None:
        return render(request, 'solution.html', {'error': 'No valid variable value found to test'})

    j, find_type_variable = get_actual_type(j)
    problem.view_count += 1
    problem.save()

    return render(request, 'solution.html', {"problem": problem, 'problem_type': find_type_variable})


def submission(request, id):
    problem = get_object_or_404(Problems, id=id)
    # if request.method == 'POST':

    # return render(request, 'submission.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def homee(request):
    todos = Task.objects.all()
    return render(request, "task/index.html", {"todo_list": todos, })


@login_required
def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        new_todo = Task.objects.create(title=title)
        return redirect("todo")
    else:
        return HttpResponse("Method not allowed", status=405)


@login_required
def update(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("todo")


@login_required
def delete(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")



def function(request):
    return render(request, 'test_core.html')