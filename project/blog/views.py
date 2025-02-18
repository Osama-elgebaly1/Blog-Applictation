from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,ContactForm

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q



@login_required
def delete_blog(request,pk):
    post = Blog.objects.get(id=pk)
    post.delete()
    return redirect('home')

    


@login_required
def edit_blog(request,pk):
    post = Blog.objects.get(id=pk)
    tags = post.tags.all()
    if request.user == post.author:
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES,instance=post)
            if form.is_valid():
                edited_post = form.save(commit=False)
                edited_post.author = request.user
                edited_post.save()
                # saving the new tags 
                tag_names = form.cleaned_data.get('tags')  
                edited_post.tags.set(tag_names)
    
                messages.success(request,'Post has been updated ...')
                return redirect('home')
        else:
            form = BlogForm(instance=post)
            return render(request,'pages/edit_blog.html',{'form':form,'post':post})
            
    else:
        messages.error(request," You Can't access this page ")
        return redirect('home')



@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            messages.success(request,'The Blog has been created successfully...')
            return redirect('home')
        
    else:
        form = BlogForm()
        return render(request,'pages/create_blog.html',{'form':form})


@login_required
def contact(request):
    info = ContactInfo.objects.all().first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            messages.success(request,'Message is sent successfully...')
            return redirect('home')
    else:
        form = ContactForm()


    return render(request,'pages/contact.html',{'info':info,'form':form})





@login_required
def last_post(request):
    post = Blog.objects.latest('date')
    return render(request,'pages/post.html',{'post':post})


@login_required
def delete_comment(request):
    if request.method == 'POST':
        pk = request.POST.get('comment-pk')
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return redirect("post",comment.blog.id)

@login_required
def add_comment(request):
    if request.method == "POST":
        blog = Blog.objects.get(id = request.POST.get("blog"))
        content = request.POST.get("content")
        user = request.user
        active = True
        new_comment = Comment.objects.create(comment=content,
                                             blog=blog,
                                             user=user,
                                             active=active,
                                             )
        new_comment.save()
        return redirect('post', request.POST.get("blog"))

@login_required
def get_tags(request,tag):
    tag = get_object_or_404(Tag,slug=tag)
    blogs = Blog.objects.filter(tags__in=[tag])
    return render(request,'pages/index.html',{'blogs':blogs})

@login_required
def post(request,pk):
    post = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(blog=post,active=True).order_by('-id')
    # getting related posts 
    tags = post.tags.all()
    related_posts = Blog.objects.filter(tags__in=tags).exclude(id=post.id).distinct()

    context = {
        'post':post,
        'comments':comments,
        'related_posts':related_posts
    }
    return render(request,'pages/post.html',context)





@login_required
def home(request):
    search = request.GET.get('search')
    if search:
        blogs = Blog.objects.filter(Q(content__icontains=search) | Q(title__icontains=search)).annotate(num_comments=Count('comment')).order_by('-date')
    else:
        blogs = Blog.objects.annotate(num_comments= Count('comment')).order_by('-date')
    
    paginator = Paginator(blogs,2)
    page_num = request.GET.get('page')
    page_posts = paginator.get_page(page_num)


    context = {
        'blogs':page_posts, 
    }
    return render(request,'pages/index.html',context)

