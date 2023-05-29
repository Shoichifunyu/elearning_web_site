from django.urls import path
from . import views
 
urlpatterns = [
    path('templates/index.html', views.index_template, name='index_template'),
    path('templates/learn_html.html', views.learn_html_template, name='learn_html_template'),
    path('templates/learn_html_tests_one.html', views.learn_html_tests_one_template, name='learn_html_tests_one_template'),
    path('templates/learn_html_tests_two.html', views.learn_html_tests_two_template, name='learn_html_tests_two_template'),
    path('templates/learn_html_contents_one.html', views.learn_html_contents_one_template, name='learn_html_contents_one_template'),
    path('templates/learn_html_contents_two.html', views.learn_html_contents_two_template, name='learn_html_contents_two_template'),
    path('templates/learn_aws.html', views.learn_aws, name='learn_aws'),
    path('templates/learn_aws_tests_one.html', views.learn_aws_tests_one, name='learn_aws_tests_one'),
    path('templates/blog.html', views.blog_template, name='learn_html_template'),
    path('templates/blog_one.html', views.blog_one_template, name='blog_one_template'),
    path('templates/blog_two.html', views.blog_two_template, name='blog_two_template'),
    path('templates/construction_view.html', views.construction_view_template, name='construction_view_template'),
]