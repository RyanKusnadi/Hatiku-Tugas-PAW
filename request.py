import requests
url = 'http://127.0.0.1:5000/api'
r = requests.post(url,json={'age':50, 'gender':2, 'height':168, 'weight':62, 'ap_hi':110, 'ap_lo':80, 'cholesterol':1, 'gluc':1,'smoke':0, 'alco':0, 'active':1,})
print(r.json())