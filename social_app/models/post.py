import datetime
from database import *
import uuid

class Post:
    def __init__(self,content,author,post_id,date=datetime.datetime.utcnow(),user_id=None):
        self.user_id=uuid.uuid4().hex if user_id is None else user_id
        self.author=author
        self.content=content
        self.date=date
        self.post_id=post_id
    def save_to_mongo(self):
        Database.insert(collection='poskak',data= self.json())

    def json(self):
        return {

            'content':self.content,
            'author': self.author,

            "post_id":self.post_id,
            "created_date": self.date,

            'user_id': self.user_id
        }
# find one post based on the post id
    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',query={'post_id':id})
# find all posts based on user_id
    @staticmethod
    def from_timeline(user_id):
        return [post for post in Database.find(collection='posts', query={'user_id': post_id})]



