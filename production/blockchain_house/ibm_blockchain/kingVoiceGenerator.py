import os.path 
import os 


import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# os.chdir("production/blockchain_house/ibm_blockchain/assets/npc/npcVoice/theKing")
#os.chdir("theKing")
os.chdir("../theKing")
print("In the King Voice Generator, your current directory is",os.getcwd())


hardHiddenMapVoice_exist = os.path.isfile("hardHiddenWelcome.wav")
hardModeMapVoice_exist = os.path.isfile("hardWelcome.wav")


theKingDialog1Voice_exist = os.path.isfile("theKingDialog1.wav")
theKingDialog2Voice_exist = os.path.isfile("theKingDialog2.wav")
theKingDialog3Voice_exist = os.path.isfile("theKingDialog3.wav")
theKingDialog4Voice_exist = os.path.isfile("theKingDialog4.wav")
theKingDialog5Voice_exist = os.path.isfile("theKingDialog5.wav")


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
    


def generateTheKingVoice():
    print("In the King Voice Generator, your current directory is",os.getcwd())

    if not theKingDialog1Voice_exist: 
        watsonGenerator("theKingDialog/theKingDialog1.txt", "theKingDialog1.wav")

    if not theKingDialog2Voice_exist: 
        watsonGenerator("theKingDialog/theKingDialog2.txt", "theKingDialog2.wav")

    if not theKingDialog3Voice_exist: 
        watsonGenerator("theKingDialog/theKingDialog3.txt", "theKingDialog3.wav")
        
    if not theKingDialog4Voice_exist: 
        watsonGenerator("theKingDialog/theKingDialog4.txt", "theKingDialog4.wav")

    if not theKingDialog5Voice_exist: 
        watsonGenerator("theKingDialog/theKingDialog5.txt", "theKingDialog5.wav")
        
    if not hardHiddenMapVoice_exist: 
        watsonGenerator("theKingDialog/hardHiddenWelcome.txt", "hardHiddenWelcome.wav")

    if not hardModeMapVoice_exist: 
        watsonGenerator("theKingDialog/hardWelcome.txt", "hardWelcome.wav")
    
        





