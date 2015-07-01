#coding:utf-8
# Create your views here.
from django.template import loader,Context
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite.models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import time

#单页显示的博客数量
BLOGS_PER_PAGE = 5

def intro_index(request):
	return render_to_response('intro/index.html')

def blog_user(request):
	dict = {'login': False}
	if request.user.is_authenticated():
		dict['login'] = True
		dict['username'] = request.user.username
	return dict

@csrf_protect
def blog_login(request):
	if request.method == "POST":
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/blog/index")
		else:
			return render_to_response('blog/login.html', {'login_fail': True}, context_instance = RequestContext(request))
	else:
		return render_to_response('blog/login.html', context_instance = RequestContext(request))

@login_required
def blog_logout(request):
	logout(request)
	return HttpResponseRedirect("/blog/index")

@csrf_protect
def blog_index(request):
	blogs = Blog.objects.all().order_by("-id")[0 : BLOGS_PER_PAGE]
	dict = {'blogs': blogs, 'page': 1}
	if len(blogs) == BLOGS_PER_PAGE:
		dict['next_page'] = True
	return render_to_response('blog/index.html', dict, context_instance = RequestContext(request))

def blog_page(request, page):
	blogs = Blog.objects.all().order_by("-id")[BLOGS_PER_PAGE * (int(page) - 1) : BLOGS_PER_PAGE * int(page)]
	dict = {'blogs': blogs, 'page': page}
	if len(blogs) == BLOGS_PER_PAGE:
		dict['next_page'] = True
	if int(page) > 1:
		dict['pre_page'] = True
	return render_to_response('blog/index.html', dict)

def blog_post(request, id):
	blog = Blog.objects.get(id = id)
	return render_to_response('blog/post.html', {'blog': blog})

def blog_about(request):
	return render_to_response('blog/about.html')

def blog_contact(request):
	return render_to_response('blog/contact.html')

@login_required
@csrf_protect
def edit_blog(request):
	dict = { 'status': False }
	if request.method == 'POST':
		dict['status'] = True
		dict['title'] = request.POST['title']
		dict['content'] = request.POST['content']
		blog = Blog(title = dict['title'], author = request.user.username, publish_time = time.strftime("%Y-%m-%d %H:%M:%S"), content = dict['content'])
		blog.save()
	return render_to_response('blog/edit_blog.html', dict, context_instance = RequestContext(request))

def sunny(request):
	return render_to_response("sunny/index.htm")