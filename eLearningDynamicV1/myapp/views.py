from django.shortcuts import render
from django.http.response import HttpResponse
 
def index_template(request):
    return render(request, 'myapp/index.html')
def learn_html_template(request):
    return render(request, 'myapp/learn_html.html')
def learn_html_tests_one_template(request):
    return render(request, 'myapp/learn_html_tests_one.html')
def learn_html_tests_two_template(request):
    return render(request, 'myapp/learn_html_tests_two.html')
def learn_html_contents_one_template(request):
    return render(request, 'myapp/learn_html_contents_one.html')
def learn_html_contents_two_template(request):
    return render(request, 'myapp/learn_html_contents_two.html')
def learn_aws(request):
    return render(request, 'myapp/learn_aws.html')
def learn_aws_tests_one(request):
    return render(request, 'myapp/learn_aws_tests_one.html')
def blog_template(request):
    return render(request, 'myapp/blog.html')
def blog_one_template(request):
    return render(request, 'myapp/blog_one.html')
def blog_two_template(request):
    return render(request, 'myapp/blog_two.html')
def construction_view_template(request):
    return render(request, 'myapp/construction_view.html')
