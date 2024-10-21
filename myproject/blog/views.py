from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.http import HttpResponse, JsonResponse, Http404

from account.models import User
from .models import Article, Category

from django.views.generic import ListView

# Create your views here.

def home(request, page=1):
	
	articles_list = Article.objects.published()
	paginator = Paginator(articles_list, 3)
	# page = request.GET.get('page')
	articles = paginator.get_page(page)

	context = {
		# 'articles' : Article.objects.all()
		# 'articles'  : Article.objects.filter(status='p').order_by('-publish')[:3]
		# 'articles' : Article.objects.filter(status = 'p'),

		'articles' : articles,
		'categories' : Category.objects.filter(status = True)
	}
	return render(request,'blog/home.html',context)


def detail(request,slug):
	
	# try:
	# 	article = Article.objects.get(slug=slug)
	# except Exception as e:
	# 	raise Http404
	
	context = {
		# 'article' : get_object_or_404(Article, slug=slug, status='p'),
		'article' : get_object_or_404(Article.objects.published(), slug=slug, status='p'),

		'categories' : Category.objects.filter(status = True)


	}

	return render(request, 'blog/detail.html', context)

def category(request, slug, page=1):
	
	category = get_object_or_404(Category, slug=slug, status = True)
	articles_list = category.articles.published()
	paginator = Paginator(articles_list, 3)
	articles = paginator.get_page(page)

	context = {
		'category' : category,
		'articles' : articles
	}

	return render(request, 'blog/category.html', context)

def authorList(request, username, page=1):

	author = get_object_or_404(User, username = username)
	article_author_list = Article.objects.filter(author=author,status='p')
	paginator = Paginator(article_author_list, 3)
	articles = paginator.get_page(page)

	context = {
		'author' : author,
		'article_author_list' : articles,
		'username':username,
	}
	return render(request,'blog/author_list.html', context)