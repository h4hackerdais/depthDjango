from django.shortcuts import render

def home_page(request):
    title = "Hello there...."
    # doc = "<h2>{title}</h2>".format(title=title)
    return render(request,"index.html",{"title":title})

def about_page(request):
    return render(request, "about.html")