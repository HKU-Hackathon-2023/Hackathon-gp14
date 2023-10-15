from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'active_item': 'home'
    }
    return render(request, 'index.html', context)

def classroom(request):
    context = {
        'active_item': 'classroom'
    }
    return render(request, 'classroom.html', context)

def note(request):
    context = {
        'active_item': 'note'
    }
    return render(request, 'note.html', context)

def bookmark(request):
    context = {
        'active_item': 'bookmark'
    }
    return render(request, 'bookmark.html', context)

def dailychallenge(request):
    context = {
        'active_item': 'challenge'
    }
    return render(request, 'challenge.html', context)

def setting(request):

    return render(request, 'setting.html')