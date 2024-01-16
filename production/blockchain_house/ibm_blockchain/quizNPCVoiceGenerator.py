import os.path 
import os 


import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


os.chdir("../quizNPC")
print("In the quizNPC Voice Generator, your current directory is",os.getcwd())

dialog1Voice_exist = os.path.isfile("quizNPCDialog1.wav")
dialog2Voice_exist = os.path.isfile("quizNPCDialog2.wav")
dialog3Voice_exist = os.path.isfile("quizNPCDialog3.wav")
dialog4Voice_exist = os.path.isfile("quizNPCDialog4.wav")
dialog5Voice_exist = os.path.isfile("quizNPCDialog5.wav")

emmaIntroVoice_exist = os.path.isfile("emmaIntroVoice.wav")
emmaDialog2Voice_exist = os.path.isfile("emmaDialog2Voice.wav")
emmaDialog3Voice_exist = os.path.isfile("emmaDialog3Voice.wav")
emmaDialog4Voice_exist = os.path.isfile("emmaDialog4Voice.wav")
emmaDialog5Voice_exist = os.path.isfile("emmaDialog5Voice.wav")


def watsonGenerator(textFilePath, fileName):
    watsonTextFile = open(textFilePath,"r")
    watsonText = watsonTextFile.read()
    watsonTextFile.close()

    authenticator = IAMAuthenticator('FbVBCmrflY290CiorB8QH9mUT-nuybxutzFzZLNjTspT')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2340778d-f272-4d32-bf19-1d83f9ad9a0d')

    with open(fileName, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                watsonText,
                voice='en-US_EmmaExpressive',
                accept='audio/wav'        
            ).get_result().content) 
    
def generateQuizNPCVoice():
    
    print("In the quizNPC Voice Generator, your current directory is",os.getcwd())
    
    if not dialog1Voice_exist: 
        watsonGenerator("quizNPCDialog/quizNPCDialog1.txt", "quizNPCDialog1.wav")

    if not dialog2Voice_exist: 
        watsonGenerator("quizNPCDialog/quizNPCDialog2.txt", "quizNPCDialog2.wav")
        
    if not dialog3Voice_exist: 
        watsonGenerator("quizNPCDialog/quizNPCDialog3.txt", "quizNPCDialog3.wav")

    if not dialog4Voice_exist: 
        watsonGenerator("quizNPCDialog/quizNPCDialog4.txt", "quizNPCDialog4.wav")
    
    if not dialog5Voice_exist: 
        watsonGenerator("quizNPCDialog/quizNPCDialog5.txt", "quizNPCDialog5.wav")
    
    



