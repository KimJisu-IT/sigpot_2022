#from django.shortcuts import render

# Create your views here.

# def main(request):
#   return render(request, "main.html")

from datetime import timezone
from pdb import post_mortem
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import FreePostform, PostModelForm, CommentForm
from .models import Check, FreePost


def main(request):
    return render(request, 'main.html')


def search(request):
    return render(request, 'search.html')


def board(request):
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'board.html', {'freeposts': freeposts})


def create(request):
    return render(request, 'create.html')


def postcreate(request):
    post = FreePost()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.author = request.user

    print("data : ", request.POST.getlist('answer1[]'))
    post.save()
    return redirect('/detail/' + str(post.id) + '/')


def detail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post': post_detail, 'comment_form': comment_form})


def edit(request, post_id):
    post = FreePost.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('/detail/' + str(post_id))

    else:
        return render(request, 'edit.html')


def delete(request, post_id):
    post = FreePost.objects.get(id=post_id)
    post.delete()
    return redirect('/')


def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
        return redirect('/detail/' + str(post_id) + '/')



def menu1(request, menu1_id):

    post= FreePost.objects.get(pk=menu1_id)
    selection = request.POST['menu1']

    menu1.save()
    return redirect('/board/')







def check(request, check_id):

    check= Check.objects.get(pk=check_id)
    selection = request.POST['check']

    check= Check.objects.get(check_id=check.id,select_id=selection)
    check.save()

    print(check)
    return redirect('/board/' + str(check.id) + '/')



def check_create(request):
    check = Check()
    check.menu= request.GET['menu']
    check.meal_time= request.GET['meal_time']
    check.save()
    return redirect('/home/' + str(check.id) + '/')

