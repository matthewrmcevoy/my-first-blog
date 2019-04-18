from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	form = PostForm()
	form2 = CommentForm()
	if request.method =="GET":
		return render(request, 'blog/post_list.html', {'posts': posts, 'form': form, 'form2':form2})
	
	elif request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm()
	return render(request, 'blog/post_list.html', {'form': form})