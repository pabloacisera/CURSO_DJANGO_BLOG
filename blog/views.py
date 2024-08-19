from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .forms import BlogPostForm

class BlogViewList(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'blog/list.html', {})
    

class BlogCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/create.html', {})
    
    def post(self, request, *args, **kwargs):
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
        else:
            return render(request, 'blog/create.html', {'form': form})