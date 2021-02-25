import requests

x = requests.get('http://thuesms.com/api-v2/?show=phone&api=2968-4b877134438d4924bd834a1c6714e344&service=213t')
# x = requests.get('http://thuesms.com/api-v2/?show=sessions&sessions=05_3446816&api=2968-4b877134438d4924bd834a1c6714e344')
print(x.text)