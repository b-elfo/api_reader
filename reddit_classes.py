import inspect

class RedditObject:
    def __init__(self,
                 ):
        self.id                    = None
        self.author                = None
        self.subreddit_id          = None
        self.subreddit             = None
        self.ups                   = None
        self.downs                 = None
        self.likes                 = None
        self.score                 = None
        self.upvote_ratio          = None
        self.controversiality      = None
        self.num_reports           = None
        self.report_reasons        = None
        self.total_awards_recieved = None
        
    def get_listof_attribute(self):
        attributes = inspect.getmembers(MyClass, lambda a:not(inspect.isroutine(a)))
        return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        
    def read_object(self,
                    obj:dict,
                    ):
        attrs = self.get_listof_attributes()
        for attr in attrs:
            try:
                setattr(self,attr,obj[attr])
            except:
                pass # TODO
        
#

class Post(RedditObject):
    def __init__(self,
                 keys:list,
                 obj:dict,
                 ):
        super().__init__()
        self.title        = None
        self.body         = None
        self.upvote_ratio = None
        self.num_comments = None
        self.comments     = []
        #
        super().read_object(obj=obj)


#

class Comment(RedditObject):
    def __init__(self,
                 obj:dict,
                 parent_comment=None,
                 ):
        super().__init__()
        self.body         = None
        self.comment_type = None
        self.depth        = None
        self.replies      = []
        self.parent       = parent_comment
        #
        self.read_object(obj=obj)
        
    def read_object(self,
                    obj:dict,
                    ):
        super().read_object(obj=obj)
        #
        if isinstance(obj['replies'],list):
            self.add_replies(obj=obj)
        
    def add_replies(self,
                    obj:dict,
                    ):
        for reply in obj['replies']['data']['children']:
            reply_obj = reply['data']
            reply_comment = Comment(obj=reply_obj,
                                    # parent_comment=self, #TODO how to pass current object to child
                                    )
            self.replies.append(reply_comment,
                                )
            
    def enum_conversation(self, 
                          depth:int=0,
                          ):
        print(self.replies)
        print(f"{'-'*depth} {self.body}")
        for reply in self.replies:
            reply.enum_conversation(depth=depth+1)