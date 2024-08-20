from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import BlogPostForm
from .models import BlogPost
from django.urls import reverse_lazy

class BlogViewList(View):
    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all()  # trae todos los post
        return render(request, 'blog/list.html', {
            'posts': posts,
        })

class BlogCreate(View):
    def get(self, request, *args, **kwargs):
        form = BlogPostForm()
        print("GET request - Form initialized:", form)
        return render(request, 'blog/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BlogPostForm(request.POST)
        print("POST request - Form data:", request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid and saved.")
            return redirect('blog:home')
        else:
            print("Form errors:", form.errors)
            return render(request, 'blog/create.html', {'form': form})

class BlogUpdate(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/updateView.html'  # Cambiado a un nombre más común
    success_url = reverse_lazy('blog:home')

    def get_object(self, queryset=None):
        return BlogPost.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        print("Form data:", form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form errors:", form.errors)
        return super().form_invalid(form)

class BlogDelete(DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('blog:home')
    
    def get_object(self, queryset=None):
        return BlogPost.objects.get(pk=self.kwargs['pk'])
    
    def delete(self, request, *args, **kwargs):
        print("POST request - Deleting post:", self.kwargs['pk'])
        return super().delete(request, *args, **kwargs)
    
    