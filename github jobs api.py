import requests
import json
execfile ("database.py")
keyword= input()
link="http://jobs.github.com/positions.json?description="+keyword
r=requests.get(link)
joblist =json.loads(r.text)
for job in joblist:
	cur.execute("INSERT INTO offers (title, description , date, type , location, url) VALUES(%s,%s,%s,%s,%s,%s)",(job['title'],job['description'],job['created_at'],job['type'],job['location'],job['url']))	
	db.commit()



cur.close()
db.close()
