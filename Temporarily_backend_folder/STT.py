import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "c08374bc35f74d46b1442fe01b4fcdc9"
service_region = "eastasia"

def convert_speech_to_text(file_name):
    """This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"""
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=service_region)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(filename=file_name)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

convert_speech_to_text('./recording_1.wav')