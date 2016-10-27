from django.shortcuts import render
from django.utils import timezone
from .models import Post
#propojeni modelu a sablon


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


'''
python manage.py shell

from blog.models import Post
Post.objects.all()
Post.objects.all()[0].text

'''
