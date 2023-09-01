from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')