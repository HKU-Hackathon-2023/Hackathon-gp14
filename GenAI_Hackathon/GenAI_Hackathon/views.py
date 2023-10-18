from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def home(request):
    context = {
        'active_item': 'home'
    }
    return render(request, 'index.html', context)

def classroom(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        print(message)
        # Process the message or perform any desired actions
        response_data = {"status": "success", "message": "Message received"}
        return JsonResponse(response_data)
    context = {
        'active_item': 'classroom'
    }
    return render(request, 'classroom.html', context)

def courses(request, course, topic):
    context = {
        'active_item': 'courses'
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

def crearCourse(request):
    if request.method == "POST":
        pass

def setting(request):
    if request.method == "POST":
        pass