from database import *
from models.user import *
from models.group import *

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
            self.user_acc=User(acc["name"],acc["_id"])
            return True
        else:
            return False
    def _prompt_user_for_account(self):
        name=input("enter your name please: ")
        id= input("enter your id please: ")
        user = User(name,id)
        self.user_acc=user



    def run_menu(self):



        service =None

        while(service != "Q"):
            print("if you want join group type (J) if you want create group type (C)")
            print("")
            print('if you want add friend "type (A) if you want write on your wall type (W)')
            print("")
            print("type (L) for listing all the blogs")
            print("")
            print("if you want join group type (J) if you want create group type (C)")
            print("")
            print('if you want add friend "type (A) if you want write on your wall type (W)')
            print("")
            print("type (L) for listing all the blogs")
            print("")
            print("type (S) for listing all your friends")
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
                print("yes")
                groups=Group.list_groups()
                for group in groups:
                    print("Name: {} ".format(group["group_name"]))
            else:
                print("thank you for your visit!!!")









