from django.shortcuts import render
import json
from django.http import JsonResponse

from . import Student

context = {
    'page': 'home',
    'user': {'name': '', 'age': '', 'gender': 'Male', 'educationLevel': '', 'educationNeed': ''},
    'courses': [],
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
    context['student'].course_change_current_topic(topic)
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        print(message)
        # Process the message or perform any desired actions
        # message = context['student'].course_speak_with_virtual_teacher(message)
        response_data = {"status": "success", "message": message}
        return JsonResponse(response_data)
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
        # create courses
        if 'student' in context:
            context['student'].create_course(courseName)
            update_context()
            print(context)
        response_data = {"status": "course: success"}
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

        if context['user']['gender'] == 'Male':
            gender = 'M'
        elif context['user']['gender'] == 'Female':
            gender = 'F'
        else:
            gender = ''

        context['student'] = Student.Student(context['user']['name'], int(context['user']['age']), gender, context['user']['educationLevel'], context['user']['educationNeed'])
        
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


def update_context():
    course_list = context['student'].retrieve_courses_list()
    for course in course_list:
        course_dir = {}
        course_dir["name"] = course
        course_dir["topics"] = context['student'].get_topic_list_of_current_couese()
        context['courses'].append(course_dir)