from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from bookstoreapp.models import *


def bookcreate(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'bookstoreapp/create.html', {'form': form})
    elif request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        return HttpResponseRedirect('')


class IndexView(generic.ListView):
    template_name = 'bookstoreapp/index.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

# class BooksInCategoryView(generic.ListView):
#    template_name = 'admin/booklist.html'
#    context_object_name = 'book_list'

#    def get_queryset(self):
#        return Book.objects.filter()


def category_view(request, category_id):
    try:
        book_list = Book.objects.filter(category_id=category_id)
        category = Category.objects.get(id=category_id).name
        return render(request, 'bookstoreapp/booklist.html', {'book_list': book_list, 'category': category})
    except:
        return render(request, 'bookstoreapp/booklist.html', {'book_list': [], 'category': ''})