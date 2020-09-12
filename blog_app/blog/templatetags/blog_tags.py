#this is for creating own template tags

from blog.models import Post
from django import template

register=template.Library()

@register.simple_tag
def total_post():    #here we can use this -->total_post(name='my_tag') and use {% my_tag %} in html file
    return Post.objects.count()


@register.inclusion_tag('blog/latest_posts123.html')
def show_latestposts():
    latest_posts=Post.objects.order_by('-publish')[:3]
    return {'latest_posts':latest_posts}

from django.db.models import Count

@register.assignment_tag
def get_most_commented_post(count=3):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
