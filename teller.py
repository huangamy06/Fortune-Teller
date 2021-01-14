import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('mpebPCpmpD839zHAE3RXeTwmz3l9wTGuYJq-JrL4hZaC')
tone_analyzer = ToneAnalyzerV3(version='2017-09-21', authenticator = authenticator)

tone_analyzer.set_service_url('https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/6607d310-f775-4c5c-8346-8b0b7dbf3e44')

with open('sample1.txt', 'r') as file:
	text = file.read()
#print(data)

tone_analysis = tone_analyzer.tone({'text': text}, content_type='application/json', sentences = False).get_result()
output = json.dumps(tone_analysis, indent=2)
output_dict = json.loads(output)

newlist = sorted(output_dict["document_tone"]["tones"], key=lambda k: k['score'], reverse=True)
tones = []
for i in range(len(newlist)):
	tones.append(newlist[i].get("tone_id"))

print(tones)

#for i in range(len(output_dict["document_tone"]["tones"])):
#	print(output_dict["document_tone"]["tones"][i])

#print(output_dict["document_tone"]["tones"][0].keys())
