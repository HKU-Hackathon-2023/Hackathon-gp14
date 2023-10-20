from django.shortcuts import render
import json
from django.http import JsonResponse


context = {
    'page': 'home',
    'user': {'name': '', 'age': '', 'gender': 'Male', 'educationLevel': '', 'educationNeed': ''},
    'course': []
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
        # create courses
        if 'student' in context:
            context['student'].create_course(courseName)
        
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

        if context['user']['gender'] == 'Male':
            gender = 'M'
        elif context['user']['gender'] == 'Female':
            gender = 'F'
        else:
            gender = ''

        context['student'] = Student(context['user']['name'], int(context['user']['age']), gender, context['user']['educationLevel'], context['user']['educationNeed'])
        
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

def voice_to_text(request):
    try:
        service_region = "eastasia"
        subscription_key = "c08374bc35f74d46b1442fe01b4fcdc9"

        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
        speech_config.speech_recognition_language = "en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return JsonResponse({"status": "success", "text": speech_recognition_result.text})
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            return JsonResponse({"status": "error", "message": "No speech could be recognized"})
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                return JsonResponse({"status": "error", "message": "Speech Recognition canceled: {}".format(cancellation_details.error_details)})
        return JsonResponse({"status": "error", "message": "Unknown error occurred"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

