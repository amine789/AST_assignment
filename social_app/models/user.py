import datetime
from database import *
import uuid
from models.post import *

from models.group import *
class User:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        if User.find_user(self.id) is None:
             Database.insert(collection='users', data={'name': name, '_id': id})

    @staticmethod
    def show_users():
        return [friend for friend in Database.find(collection='users', query={})]




    def add_post(self):
        v = input(" enter post content: ")
        post = Post(v,self.name,self.id)
        post.save_to_mongo()
    def show_friends(self,name):
        return [friend for friend in Database.find(collection=name, query={})]

    def add_friend(self,name,id):
        Database.insert(collection=self.name, data={'name':name,'id':id})
    def remove_friend(self):
        pass

    def get_my_posts(self, id):
        Post.from_mongo(id)
    def save_to_mongo(self):
        Database.insert(collection='friends', data=self.json())
    def from_json(self):
        return {
            'name': self.name,
            'id': self.id
        }
    def create_group(self,group_name,user_name,user_id):
        #Database.insert(collection=name, data={'name': self.name, 'id': self.id})
        Group.create_group(group_name,user_name,user_id)
    def join_group(self,name):
        Database.insert(collection=name, data={'name': self.name, 'id': self.id})

    @staticmethod
    def find_user(id):
        data=Database.find_one(collection='users', query={'_id':id})
        print(data)
        return data

