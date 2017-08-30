#The source file provides links corrsponding to the APIs in websites
#The links are put in a list called links
links= ["http://jobs.github.com/positions.json?description={{keyword}}", "https://remoteok.io/remote-jobs.json?tags={{keyword}}"]
sources=[{"source_id":"1", "url":"http://jobs.github.com/positions.json?description={{keyword}}", "title":"title","id":"id", "date":"created_at","source":"Github jobs"},{"source_id":"2", "url":"https://remoteok.io/remote-jobs.json?tags={{keyword}}", "title":"position","id":"id", "date":"date","source":"Remoteok jobs"}]
