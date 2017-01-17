from django.shortcuts import render
from django.views.generic import TemplateView
from models import Blog
from models import Category


# Create your views here.
#Display categories and latest posts
#Display posts in a specific category
#Display the post
#Add a post

class HomePageView(TemplateView):
    def get(self,request, **kwargs):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        return render(request, 'index.html', context={'blogs': blogs, 'categories':categories})

def posts_in_category(request, category_id):
    categories = Category.objects.get(pk=category_id)
    return render(request, 'post.html', context={'categories':categories})

def blog_post(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'post.html', context={'blog':blog})

 
def add_post(request):
    if request.method == 'POST':
        post_vars = {}
        for field in request.POST:
            if field != 'csrfmiddlewaretoken':
                post_vars[field] = request.POST[field]
            post_vars['category_id'] = 1
            new_post = Blog(**post_vars)
            new_post.save()
    return render(request, 'add.html')


   