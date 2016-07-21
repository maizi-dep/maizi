from django.shortcuts import render


# Create your views here.
def index(request):
    try:
        pass
    except Exception as e:
        print e
    return render(request, 'index.html', locals())
