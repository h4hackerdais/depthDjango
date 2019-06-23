from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .models import BlogPost
# from .forms import BlogPostForm
from .forms import BlogPostModelForm
def posts(request):
    posts = BlogPost.objects.all() # all data
    return render(request, "posts.html", {"posts":posts})

def post(request, post_id):
    # print(post_id.__class__) <class 'int'> check data type
    # first way
    # try:
    #     post = BlogPost.objects.get(id=post_id) # single data by id
    # except:
    #     raise Http404 # set error Page not found

    # second way
    # try:
    #     post = BlogPost.objects.get(id=post_id)  # single data by id
    # except BlogPost.DoesNotExist:
    #     raise Http404  # found except set page not found
    # except ValueError:
    #     raise Http404

    # better way and best way with page not founnd
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "post.html", {"post":post})

def post_search(request,name):
    posts = BlogPost.objects.filter(title__contains=name)
    return render(request, "posts.html", {"posts": posts})

# first way insert data
# def post_create(request):
#     form = BlogPostForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         print(form.cleaned_data["title"])
#         BlogPost.objects.create(**form.cleaned_data) # insert data
#         form = BlogPostForm()  # blank form data
#
#     return render(request, "post_create.html",{"form":form})


# second way insert data
# def post_create(request):
#     form = BlogPostModelForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         print(form.cleaned_data["title"])
#         form.save()  # insert data
#         form = BlogPostModelForm()  # blank form data
#
#     return render(request, "post_create.html",{"form":form})
#


# Third modify form
def post_create(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)  # insert data
        obj.title = form.cleaned_data.get("title") + "add"
        obj.save()
        form = BlogPostModelForm()  # blank form data

    return render(request, "post_create.html", {"form":form})


# update
def post_update(request, post_id):
    post = BlogPost.objects.get(id=post_id) # single data by id

    form = BlogPostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        obj = form.save(commit=False)  # insert data
        obj.title = form.cleaned_data.get("title") + "add"
        obj.save()
        form = BlogPostModelForm()  # blank form data

    return render(request, "post_create.html",{"form":form})


def post_delete(request, post_id):
    if request.method == 'POST':
        post = BlogPost.objects.get(id=post_id)  # single data by id
        post.delete()
        return redirect("/posts")

    return render(request, "post_delete.html")
