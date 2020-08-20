from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
# search
from django.db.models import Q

from .models import Book
from .forms import BookForm

# Create your views here.
class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 12


@method_decorator(login_required, name="dispatch")
class BookDetail(DeleteView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_detail.html'

@login_required
def bookCreate(request):
    model = Book
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_at = timezone.now()
            book.created_by = request.user
            book.save()
            SuccessMessageMixin = "Book successfully created!"
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_new.html', {'form':form})

@method_decorator(login_required, name="dispatch")
class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    context_object_name = 'books'
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    success_message = 'Book successfully updated!'
    template_name = 'book_update.html'


@method_decorator(login_required, name="dispatch")
class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    context_object_name = 'books'
    success_url = reverse_lazy('book_list')
    success_message = "Book successfully deleted!"
    template_name = 'book_delete.html'

@method_decorator(login_required, name="dispatch")
class UserPostList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'user_post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by = self.request.user)

def search(request):
    template = 'search.html'
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else: 
        results = {}
    return render(request, template,{"results":results})