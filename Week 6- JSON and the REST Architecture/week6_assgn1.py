import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
print('Count:', len(info['comments']))

sum = 0
for item in info['comments']:
    sum += int(item['count'])

print('Sum:',sum)

