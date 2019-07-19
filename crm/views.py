from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, World!")

def board(request):
    # keyword = request.GET.get("keyword")
    #
    # if keyword:
    #     articles = Article.objects.filter(title__contains=keyword)
    #     return render(request, "articles.html", {"articles": articles})
    # articles = Article.objects.all()

    return render(request, "board.html")