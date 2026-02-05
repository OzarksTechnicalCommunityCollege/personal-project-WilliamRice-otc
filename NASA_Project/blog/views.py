from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404


# Create your views here.

# displays all published posts
def published_list(request):
    posts = Post.published.all()
    return render(
        request, 'blog/post/list.html',
        {'posts': posts}
    )

# displays draft posts
# def drafted_list(request):
#     posts = Post.drafted.all()
#     return render(
#         request, 'blog/post/list.html',
#         {'posts': posts}
#     )

# allows published post details to be accessed
def published_detail(request, id):

    post = get_object_or_404(
        Post,
        id=id,
        status = Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/published_detail.html',
        {'post': post}
    )

# allows drafted post details to be accessed
# def draft_detail(request, id):

#     post = get_object_or_404(
#         Post,
#         id=id,
#         status = Post.Status.DRAFT
#     )
#     return render(
#         request,
#         'blog/post/draft_detail.html',
#         {'post':post}
#     )

