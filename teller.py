import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('mpebPCpmpD839zHAE3RXeTwmz3l9wTGuYJq-JrL4hZaC')
tone_analyzer = ToneAnalyzerV3(version='2017-09-21', authenticator = authenticator)

tone_analyzer.set_service_url('https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/6607d310-f775-4c5c-8346-8b0b7dbf3e44')

text = 'Hi, my name is Amy. I am a graduating student studying computer science. I was able to sign on for a full time engineering job with an amazing company. I will be in Seattle Washington for a while which I look forward to. I am concerned I will not be able to learn fast enough to keep up with my team as I will be using a completely new tech stack. Based on the interview with my team, they seem very flexible and ready to teach. I hope I can live up to their expectations while also learning a shit ton.'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
analysis = json.dumps(tone_analysis, indent=2)
tone = tone_analysis["document_tone"]['tones'][0]['tone_name']
print("Tone: " + tone)
if tone == "Joy": 
    print("A lifetime of happiness lies ahead of you")
elif tone == "Anger":
    print("A light heart carries you through all the hard times")
elif tone == "Fear":
    print("Fear and desire - two sides of the same coin")
elif tone == "Sadness":
    print("All the troubles you have will pass away very quickly")
elif tone == "Analytical":
    print("You have an active mind and a keen imagination")
elif tone == "Confident":
    print("Believe in yourself and others will too")
elif tone == "Tentative":
    print("The smart thing to do is to begin trusting your intuitions")


