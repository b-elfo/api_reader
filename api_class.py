import requests
from requests.adapters import HTTPAdapter, Retry
import json

#

class API_Connect:
    def __init__(self,
                 retries=5,
                 backoff_factor=1,
                 forcelist=[502,503,504],
                 sleep=10,
                 ):
        #
        self.session = requests.Session()
        retries = Retry(total=retries, 
                        backoff_factor=backoff_factor, 
                        status_forcelist=forcelist,
                        )
        self.session.mount('http://', 
                           HTTPAdapter(max_retries=retries),
                           )
        #
        self.endpoints = {}
        self.params = {}
        #
        self.sort_keys = True
        self.indent = 2
        #
        self.sleep = sleep
        
    def add_endpoint(self,
                     url_key,
                     url,
                     param=None,
                     ):
        #
        self.endpoints[url_key] = url
        #
        if param:
            self.params[url_key] = param
        
    def enum(self, 
             obj,
             ):
        # TODO: Update to include GraphQL
        print(json.dumps(obj,
                         sort_keys=self.sort_keys,
                         indent=self.indent,
                         ))
        
    def get_response(self, 
                     url_key,
                     ):
        #
        if url_key in self.params:
            #
            return self.session.get(self.endpoints[url_key]+self.params[url_key])
        else:
            #
            return self.session.get(self.endpoints[url_key])
        time.sleep(self.sleep)