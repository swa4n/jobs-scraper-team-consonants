def structurize(job,keyword,source):
        tmp={"source_id":"","id":"","title":"","tags":"","date":"","source":"","url":""}
        tmp['source_id']=source['source_id']
        tmp['id']=job[source['id']]
        tmp['title']=job[source['title']]
        tmp['tags']=keyword
        tmp['date']=job[source['date']]
        tmp['source']=source['source']
        tmp['url']=job['url']
        return tmp      
