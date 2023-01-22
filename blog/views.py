from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import NewPostOrUpdateForm


######                                   Imports


####                                   List_View
##   class

class Post_List(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


##   def

# def post_list_view(request):
#     #post_list = Post.objects.all()
#     post_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'post_list':post_list})

####                                   Detail_View
##   class

class Post_Detail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # context_object_name = 'post'


##   def

# def post_detail_view(request, pk):
# ####error handling
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     post=None
#     #     print('Excepted')
#
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post=None
#     #     print('Excepted')
#
#
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})

####                                   Add_View
##   class

class Post_Add(generic.CreateView):
    form_class = NewPostOrUpdateForm
    template_name = 'blog/add_post.html'



##   def

# def post_add_view(request):
#     if request.method == 'POST':
#         form = NewPostOrUpdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#             # form = NewPostOrUpdateForm()
#     else:
#         form = NewPostOrUpdateForm()
#     return render(request, 'blog/add_post.html', context={'form':form})
#     # if request.method == 'POST' :---
#         # post_title = request.POST.get('tit')---
#         # post_text = request.POST.get('tex')---
#         # user = User.objects.all()[0]---
#         # Post.objects.create(title=post_title, text=post_text, author=user, status='pub')---
#     # else:---
#         # print('is method request GET')---
#     # return render(request, 'blog/add_post.html')---


####                                   Update_View
##   class

class Post_Update(generic.UpdateView):
    model = Post
    form_class = NewPostOrUpdateForm # Or    fields = ['title', 'text', 'author', 'status']
    template_name = 'blog/add_post.html'


##   def

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostOrUpdateForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#
#     return render(request, 'blog/add_post.html', context={'form':form})


####                                   Delete_View
##   class

class Post_Delete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post_list'
    success_url = reverse_lazy('post_list') # Or   '/blog/'

    # or
    # def get_success_url(self):
    #     return reverse('post_list')



##   def

# def post_delete_view(erquest, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if erquest.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(erquest, 'blog/post_delete.html', context={'post':post})