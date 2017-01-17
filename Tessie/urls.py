from django.conf.urls import url
from Tessie import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^add/$', views.add_post),
    url(r'^category/(?P<category_id>\d+)/$', views.posts_in_category),
    url(r'^post/$', views.blog_post),
    
]