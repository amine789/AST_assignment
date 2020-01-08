

from database import *
class Group:
    def __init__(self,group_name,user_name,user_id):
        self.group_name=group_name
        self.user_id=user_id
        self.user_name=user_name


    def join_group(self,group_name,user_name,user_id):
        Database.insert(collection=group_name, data=self.json())



    def create_group(self,group_name,user_name,user_id):
        Database.insert(collection='groups', data=self.json2())
        Database.insert(collection=group_name, data=self.json())
    @staticmethod
    def list_groups():
        return [post for post in Database.find(collection='groups', query={})]

    def json(self):
        return {

            'group_name': self.group_name,
            'user_name': self.user_name,

            "user_id": self.user_id

        }
    def json2(self):
        return {
            'group_name':self.group_name

        }



