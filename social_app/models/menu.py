from database import *
from models.user import *
from models.group import *
from datetime import datetime
import unittest
class menu:
    def __init__(self):
        self.user=input("enter your user name: ")
        self.user_acc=None
        if self.user_check_has_account():
            print("welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def user_check_has_account(self):
        acc= Database.find_one('users', {'_id':self.user})

        if acc is not None:
            p=acc['_id']
            self.user_acc=User(acc["name"],acc["_id"],acc['date_of_birth'],acc['relationship status'])
            return True
        else:
            return False
    def _prompt_user_for_account(self):
        print("regitration form")
        name=input("enter your name please: ")
        id= input("enter your id please: ")
        date=input("please enter your date in dd.mm.yy format: ")
        try:
            status=input('please enter your relationship status S for single and M for married C for complicated: ')
        except ValueError:
            print("Incorrect format")

        year, month, day = map(int, date.split('.'))
        print(day)
        date = datetime(day, month, year)
        user = User(name,id,date,status)
        self.user_acc=user



    def run_menu(self):
        print("***********************welcome in facelook!!***************************")



        service =None

        while(service != "Q"):
            print("if you want join group type (J)")
            print("")
            print('if you want add friend "type (A) if you want write on your wall type (W)')
            print("")
            print("type (G) to see all your posts")
            print("")
            print("if you want create group type (C)")
            print("")
            print('if you want add friend "type (A) if you want write on your wall type (W)')
            print("")
            print("type (L) for listing all the Groups")
            print("")
            print("type (S) for listing all your friends")
            print("")
            print("type (V) for listing group members")
            print("")

            service = input("type the value here: ")



            if service=='W':
                self.user_acc.add_post()
            elif service=='J':
                inp = input("please give the group name: ")
                group = Group(inp, self.user_acc.name, self.user_acc.id)
                group.create_group(inp, group.user_name, group.user_id)
            elif service=='C':

                inp = input("please give the group name: ")
                group= Group(inp,self.user_acc.name,self.user_acc.id)
                group.create_group(inp,group.user_name,group.user_id)
            elif service=='A':
                name = input("please write  the friend name: ")
                id = input("please write the friend ID")
                self.user_acc.add_friend(name,id)
            elif service=="S":
                name=self.user_acc.name

                t=self.user_acc.show_friends(name)
                for v in t:
                    print(v)

            elif service=='L':

                groups=Group.list_groups()
                for group in groups:
                    print("Name: {} ".format(group["group_name"]))
            elif service=='G':

                groups=Post.from_timeline(self.user_acc.id)
                for group in groups:
                    print(group['content'])
                    print("posted on ",group['created_date'])
                    print("")
            elif service=='V':
                inp=input("please enter the group name: ")
                a=Group.list_members(inp)
                for m in a:
                    print(m)
            else:
                print("thank you for your visit!!!")









