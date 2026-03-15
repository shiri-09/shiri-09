import urllib.request, json
url = "https://api.github.com/users/shiri-09/repos?sort=updated&per_page=10"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req).read()
data = json.loads(response)
for r in data:
    if r['name'] != 'shiri-09':
        print(f"{r['name']}: {r['description']} ({r['language']})")
