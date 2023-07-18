from django.shortcuts import render, get_list_or_404

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


def solutions(request):
    return render(request,'solution.html')