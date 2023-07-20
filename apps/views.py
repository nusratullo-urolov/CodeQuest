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


def problem(request, title):
    problem = get_object_or_404(Problems, title=title)
    if request.method == 'POST':
        post = request.POST['example']
        result = post.split("(")[1].split(")")[0]
        try:
            result = eval(result)
        except Exception as e:
            result = e
        context = {
            'result': result
        }
        return render(request, 'solution.html', context=context)
    return render(request, 'solution.html',context={'problem' : problem})
