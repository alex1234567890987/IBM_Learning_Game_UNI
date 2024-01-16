import os.path 
import os 


import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#os.chdir("production/blockchain_house/ibm_blockchain/assets/npc/npcVoice/emma") # For emmaVoiceGenerator.py
#os.chdir("assets/npc/npcVoice/emma") # For BlockChainHouse.py
os.chdir("assets/npc/npcVoice/emma")
print("In the Emma Voice Generator, your current directory is",os.getcwd())

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
    

def generateEmmaVoice():
    if not emmaIntroVoice_exist: 
        watsonGenerator("emmaDialog/emmaIntroVoice.txt", "emmaIntroVoice.wav")

    if not emmaDialog2Voice_exist: 
        watsonGenerator("emmaDialog/emmaDialog2.txt", "emmaDialog2Voice.wav")
        
    if not emmaDialog3Voice_exist: 
        watsonGenerator("emmaDialog/emmaDialog3.txt", "emmaDialog3Voice.wav")

    if not emmaDialog4Voice_exist: 
        watsonGenerator("emmaDialog/emmaDialog4.txt", "emmaDialog4Voice.wav")
    
    if not emmaDialog5Voice_exist: 
        watsonGenerator("emmaDialog/emmaDialog5.txt", "emmaDialog5Voice.wav")
    
    os.chdir("../")
 

