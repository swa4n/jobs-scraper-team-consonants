import requests
import json

input(keyword)
link="http://jobs.github.com/positions.json?description="+keyword
r=requests.get(link)
joblist =json.loads(r.text)
for job in joblist:
    print(joblist[job]['title'])
