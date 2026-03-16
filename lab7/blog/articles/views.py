from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {"posts": posts})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):

    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":

        form = {
            "title": request.POST.get("title"),
            "text": request.POST.get("text")
        }

        if form["title"] and form["text"]:

            # проверка уникальности названия
            if Article.objects.filter(title=form["title"]).exists():
                form["errors"] = "Статья с таким названием уже существует"
                return render(request, "create_post.html", {"form": form})

            article = Article.objects.create(
                title=form["title"],
                text=form["text"],
                author=request.user
            )

            return redirect('get_article', article_id=article.id)

        else:
            form["errors"] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})

    else:
        return render(request, "create_post.html", {})

def register(request):

    if request.method == "POST":

        form = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password")
        }

        if not form["username"] or not form["password"]:
            form["errors"] = "Не все поля заполнены"
            return render(request, "register.html", {"form": form})

        if User.objects.filter(username=form["username"]).exists():
            form["errors"] = "Пользователь с таким именем уже существует"
            return render(request, "register.html", {"form": form})

        User.objects.create_user(
            form["username"],
            form["email"],
            form["password"]
        )

        return redirect("login")

    return render(request, "register.html")

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, "login.html",
                          {"error": "Заполните все поля"})

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "login.html",
                          {"error": "Нет аккаунта с таким логином и паролем"})

        login(request, user)
        return redirect("archive")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("archive")