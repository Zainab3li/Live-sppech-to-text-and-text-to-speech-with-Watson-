# Live-sppech-to-text-and-text-to-speech-with-Watson-
In this task I have created live speech to text with Watson Speech to Text then convert Text to Speech by using python language. I have used this code to save what the person says in the .txt file ( AB= data[‘results’][0][‘alternatives’][0][‘transcript’] with open (“test.txt”,”w”) as adout: adout.write(AB) ). Then to convert from text to speech I have used ( with open('test.txt', 'r') as f:     text = f.readlines()     text = [line.replace('\n', '') for line in text]     text = ''.join(str(line) for line in text)  with open('./sound.mp3', 'wb') as audio_file:     res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()     audio_file.write(res.content)
