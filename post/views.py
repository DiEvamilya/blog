from django.shortcuts import render, redirect

from post.forms import CreateCategoryModelForm
from post.models import Category


# Create your views here.
def index(request):
    return render(request, 'post/index.html')


def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'post/category_list.html', context)



def create_category_view(request):
    if request.method == 'POST':
        form = CreateCategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CreateCategoryModelForm()

    context = {'form': form}
    return render(request, 'post/categoru_create.html', context)
