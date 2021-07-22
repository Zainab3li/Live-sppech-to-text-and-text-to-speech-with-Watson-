
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = 'Xcc2JvvanDgNPx_VqUaS6X3cWWmTrReWppoeUpp3ykqV'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/14c63f94-0d23-44f4-b1eb-7cabb52e52c3'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open('test.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)


with open('./sound.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)


    