import requests
def sms_help(number):
	url = "https://smsapi.engineeringtgr.com/send/"
	params = dict(Mobile='7860564879', Password='password@123', Key='pulkiWNZYJrFyd97msz5fMPlbvxnI', Message='Anubhav is very sad. Can you please talk to him and lighten up his mood a bit?', To=number)
#Number is a String
	resp = requests.get(url, params)

def sms_emergency(number):
	url = "https://smsapi.engineeringtgr.com/send/"
	params = dict(Mobile='7860564879', Password='password@123', Key='pulkiWNZYJrFyd97msz5fMPlbvxnI', Message='Anubhav is displaying suicidal tendencies. He needs immediate professional assistance.', To=number)

	resp = requests.get(url, params)
#Number is a String
#emergency is for emergency cases
#help is for normal cases
