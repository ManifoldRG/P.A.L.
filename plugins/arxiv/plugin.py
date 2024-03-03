import random
import json, sys
import requests
from scholarly import scholarly
import re
from ..proactive_plugin import ProactivePlugin


class ArxivPlugin(ProactivePlugin):
    def __init__(self):
        #self.date = '[202005280000+TO+202005290000]'
        self.citations_filter = 10000
        #self.title_keywords = 'language models'
        self.orgfilters = ['OpenAI', 'Anthropic', 'Meta', 'Google', 'Microsoft']
        self.triggered = False
    
    def filter_by_citations(self, paper_metadata):

        search_query = scholarly.search_author(paper_metadata['first_author'])
        author = next(search_query)
        
        # Only pick the papers from renowned authors and orgs
        '''if author['citedby'] > 0 and author['affiliation'] in self.orgfilters:

            return 1
        
        else:

            return 0'''
        
        return 1
    
    def process_results(self, papers):

        papers_metadata = []
        for paper in papers:
            
            temp_dict = {}
            temp_dict['title'] = paper.split('</title>')[0].replace('\n', '')
            temp_dict['title'] = temp_dict['title'].replace('\\', '')


            temp_dict['summary'] = re.split(r'<summary>|</summary>', paper)[1].replace('\n', '')
            temp_dict['summary'] = temp_dict['summary'].replace('\\', '')

            temp_dict['first_author'] = re.split(r'<name>|</name>', paper)[1].replace('\n', '')
            temp_dict['first_author'] = temp_dict['first_author'].replace('\\', '')

            papers_metadata.append(temp_dict)
        
        #print(papers_metadata)
        return papers_metadata

    
    def retrieve_arxiv_results(self):

        '''modified_title_keyword = ""
        for word in self.title_keywords.split(' '):

            if len(modified_title_keyword)>0:
                modified_title_keyword=modified_title_keyword+'%20'+word
            else:
                modified_title_keyword=word'''

        r = requests.get('http://export.arxiv.org/api/query?search_query=ti:language%20models+AND+submittedDate:[202402280000+TO+202403020000]&max_results=3')
        #print(r.content)
        # Separating the papers based on the results
        papers = str(r.content).split('<title>')

        papers_metadata = self.process_results(papers[1:])
        
        final_paper_list = []

        for paper in papers_metadata:

            filter_result = self.filter_by_citations(paper)
            if filter_result == 1:
                final_paper_list.append(paper)


        #print(final_paper_list)
        return final_paper_list


    def invoke(self, event):
        papers = self.retrieve_arxiv_results()
        final_output = "New Arxiv papers:"

        if len(papers)==0:
            return None
        
        else:

            for paper in papers:

                final_output = final_output+'\nTitle: '+paper['title']
                final_output = final_output+'\nSummary: '+paper['summary']
                final_output = final_output+'\nFirst author: '+paper['first_author']
            
            #print(final_output)
            return final_output
        





