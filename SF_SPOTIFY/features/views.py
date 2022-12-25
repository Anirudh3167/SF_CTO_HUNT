from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    #return HttpResponse('<h1> Everything is working fine </h1>')
    return render(request,"Home.html")

def UnderDevelopment(request):
    return render(request,"under_development.html")

def About(request):
    return render(request,"About.html")

def Feature(request,id):
    if request.method == "POST":
        return HttpResponse("<h1> Form Created </h1>")
    context = {}
    context['id'] = id
    if id == "1":
        print("It is Feedback")
        context['featureName'] = "Feedback"
    elif id == "2":
        print("It is Remix Seperator")
        context['featureName'] = "Remix Seperator"
    elif id == "3":
        print("It is Auto Stop")
        context['featureName'] = "Auto Stop"
    elif id == "4":
        print("It is Lyrics Translation")
        context['featureName'] = "Lyrics Translation"
    elif id == "5":
        print("It is Equilizer")
        context['featureName'] = "Equilizer"
    else:
        return render(request,"under_development.html")
    return render(request,"feature_home.html",context)


def FeatureAbout(request,id):
    context = {}
    context['id'] = id
    if id == "1":
        print("It is Feedback")
        context['featureName'] = "Feedback"
    elif id == "2":
        print("It is Remix Seperator")
        context['featureName'] = "Remix Seperator"
    elif id == "3":
        print("It is Auto Stop")
        context['featureName'] = "Auto Stop"
    elif id == "4":
        print("It is Lyrics Translation")
        context['featureName'] = "Lyrics Translation"
    elif id == "5":
        print("It is Equilizer")
        context['featureName'] = "Equilizer"
    if id != "1":
        return render(request,"under_development.html")
    return render(request,"feature_1_about.html",context)


def FeatureAnalysis(request,id):
    context = {}
    context['id'] = id
    if id == "1":
        print("It is Feedback")
        context['featureName'] = "Feedback"
    elif id == "2":
        print("It is Remix Seperator")
        context['featureName'] = "Remix Seperator"
    elif id == "3":
        print("It is Auto Stop")
        context['featureName'] = "Auto Stop"
    elif id == "4":
        print("It is Lyrics Translation")
        context['featureName'] = "Lyrics Translation"
    elif id == "5":
        print("It is Equilizer")
        context['featureName'] = "Equilizer"
    if id != "1":
        return render(request,"under_development.html")
    return render(request,"feature_1_analysis.html",context)
