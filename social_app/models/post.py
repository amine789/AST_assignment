import datetime
from database import *
import uuid

class Post:
    def __init__(self,content,author,user_id=None,date=datetime.datetime.utcnow()):

        self.user_id=uuid.uuid4().hex if user_id is None else user_id
        self.author=author
        self.content=content
        self.date=date
        #self.post_id=uuid.uuid4().hex if post_id is None else post_id
        #Database.insert(collection='poskak',data= self.json())


    def save_to_mongo(self):
        data=self.json()

        Database.insert(collection='poskak', data=self.json())

    def json(self):
        return {

            'content':self.content,
            'author': self.author,


            "created_date": self.date,

            'user_id': self.user_id
        }

    def new_post(self):
        v = input(" enter post content: ")
        post = Post(v,)
# find one post based on the post id
    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='poskak',query={'post_id':id})
# find all posts based on user_id
    @staticmethod
    def from_timeline(user_id):
        return [post for post in Database.find(collection='poskak', query={'user_id': user_id})]






