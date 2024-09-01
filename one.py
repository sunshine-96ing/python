import requests

# resp = requests.get('https://api.lovelive.tools/api/SweetNothings')

resp = requests.get('https://v1.hitokoto.cn/', params={'encode': 'text'})
print(resp.text)