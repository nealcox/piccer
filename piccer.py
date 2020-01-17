import requests

r = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
print(r.status_code)
print(r.json())
