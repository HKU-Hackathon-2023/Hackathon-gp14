from django.shortcuts import render
import json
from django.http import JsonResponse

context = {
    'page': 'home',
    'user': {'name': '', 'age': '', 'gender': 'Male', 'educationLevel': '', 'educationNeed': ''},
    'course' : {}
}


# Create your views here.
def home(request):
    context['page'] = 'home'
    return render(request, 'index.html', context)

def classroom(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        print(message)
        # Process the message or perform any desired actions
        response_data = {"status": "success", "message": "Message received"}
        return JsonResponse(response_data)
    context['page'] = 'classroom'
    return render(request, 'classroom.html', context)

def courses(request, course, topic):
    context['page'] = 'courses'
    return render(request, 'classroom.html', context)

def note(request):
    context['page'] = 'note'    
    return render(request, 'note.html', context)

def bookmark(request):
    context['page'] = 'bookmark'
    return render(request, 'bookmark.html', context)

def dailychallenge(request):
    context['page'] = 'challenge' 
    return render(request, 'challenge.html', context)

def crearCourse(request):
    if request.method == "POST":
        data = json.loads(request.body)
        courseName = data.get("courseName")
        # create courses and store it in context['course]
        response_data = {"status": "success"}
        return JsonResponse(response_data)

def setting(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        educationLevel = data.get("educationLevel")
        educationNeed = data.get("educationNeed")
        
        context['user']['name'] = name
        context['user']['age'] = age
        context['user']['gender'] = gender
        context['user']['educationLevel'] = educationLevel
        context['user']['educationNeed'] = educationNeed

        # Store values in session
        request.session['name'] = name
        request.session['age'] = age
        request.session['gender'] = gender
        request.session['educationLevel'] = educationLevel
        request.session['educationNeed'] = educationNeed

        response_data = {"status": "success"}
        return JsonResponse(response_data)
    
    elif request.method == "GET":
        name = request.session['name']
        age = request.session['age']
        gender = request.session['gender']
        educationLevel = request.session['educationLevel']
        educationNeed = request.session['educationNeed']
        
        response_data = {"name": name,
                         "age": age,
                         "gender": gender,
                         "educationLevel": educationLevel,
                         "educationNeed": educationNeed}
        return JsonResponse(response_data) 
