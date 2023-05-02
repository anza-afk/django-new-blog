from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         paginator.page(paginator.num_pages)
#     return render(
#         request=request,
#         template_name='blog/post/list.html',
#         context={
#             'posts': posts,
#             'page': page
#         }
#     )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(
        request=request,
        template_name='blog/post/detail.html',
        context={'post': post}
    )
