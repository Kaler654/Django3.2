from django.shortcuts import render


def user_list(request):
    template = "users/user_list.html"
    context = {}
    return render(request, template, context=context)


def user_detail(request, user_id):
    template = "users/user_detail.html"
    context = {}
    return render(request, template, context=context)


def signup(request):
    template = "users/signup.html"
    context = {}
    return render(request, template, context=context)


def profile(request):
    template = "users/profile.html"
    context = {}
    return render(request, template, context=context)
