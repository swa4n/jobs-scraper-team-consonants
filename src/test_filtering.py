import unittest
import sys
from scrapping import *
from source import sources
class TestStructure(unittest.TestCase):
    def teststruct(self):
            mock_githubjobs={'id':'d3713af8-8be5-11e7-8900-ce8d211c7a9c','created_at':'Mon Aug 28 11:44:24 UTC 2017', 'title':'Lead Digital Transformation - Future Leader','location':'Den Bosch ', 'type':'Full Time','description':'<p><b>Lead Digital Trans…ader Programma.</i></p>','how_to_apply':'<p>Solliciteer online vi…','company':'Essent','company_url':'https://essent.redirect.…63101/V819/solliciteren','company_logo':'http://github-jobs.s3.am…7-8ad6-de97513e4ef4.jpg','url':'http://jobs.github.com/p…-11e7-8900-ce8d211c7a9c'}
            mock_remoteok={'slug':'61554-remote-ios-developer-europe-hotjar','id':'61554','epoch':'1504092265','date':'2017-08-30T04:24:25-07:00','company':'Hotjar','position':'iOS Developer (Europe)','tags':'[3]','logo':'https://we-work-remotely…ogos/0001/6604/logo.gif','description':'<div><strong>Note:</stro…os-developer-europe</a>','url':'https://remoteok.io/jobs…developer-europe-hotjar'}
            jobgithub=structurize(mock_githubjobs,'big+data',sources[0])
            jobro=structurize(mock_remoteok,'big+data',sources[1])
            jobgithubassert={'source_id': '1', 'title': 'Lead Digital Transformation - Future Leader','id': 'd3713af8-8be5-11e7-8900-ce8d211c7a9c', 'date': 'Mon Aug 28 11:44:24 UTC 2017','tags': 'big+data','source':'Github jobs','url':'http://jobs.github.com/p…-11e7-8900-ce8d211c7a9c'}
            jobroassert={'source_id': '2','title': 'iOS Developer (Europe)','id': '61554',   'date': '2017-08-30T04:24:25-07:00','tags': 'big+data', 'source': 'Remoteok jobs', 'url': 'https://remoteok.io/jobs…developer-europe-hotjar'}
            self.assertEqual(jobgithub,jobgithubassert)
            self.assertEqual(jobro,jobroassert)
if __name__ == '__main__':
    unittest.main()
