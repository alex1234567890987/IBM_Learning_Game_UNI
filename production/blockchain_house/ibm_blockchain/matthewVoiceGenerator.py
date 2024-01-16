import os.path 
import os 


import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#os.chdir("../matthew")
os.chdir("matthew")
print("In the Matthew Voice Generator, your current directory is",os.getcwd())
#os.chdir("npcVoice/matthew")
#os.chdir("production/blockchain_house/ibm_blockchain/assets/npc/npcVoice/matthew")


dialog1Voice_exist = os.path.isfile("matthewDialog1.wav")
dialog2Voice_exist = os.path.isfile("matthewDialog2.wav")
dialog3Voice_exist = os.path.isfile("matthewDialog3.wav")
dialog4Voice_exist = os.path.isfile("matthewDialog4.wav")
dialog5Voice_exist = os.path.isfile("matthewDialog5.wav")



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
    
    
def generateMatthewVoice():
    if not dialog1Voice_exist: 
        watsonGenerator("matthewDialog/matthewDialog1.txt", "matthewDialog1.wav")

    if not dialog2Voice_exist: 
        watsonGenerator("matthewDialog/matthewDialog2.txt", "matthewDialog2.wav")
        
    if not dialog3Voice_exist: 
        watsonGenerator("matthewDialog/matthewDialog3.txt", "matthewDialog3.wav")

    if not dialog4Voice_exist: 
        watsonGenerator("matthewDialog/matthewDialog4.txt", "matthewDialog4.wav")
    if not dialog5Voice_exist: 
        watsonGenerator("matthewDialog/matthewDialog5.txt", "matthewDialog5.wav")
    
   


# print(os.getcwd())
# print(emmaIntroVoice_exist)