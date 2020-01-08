
from models.post import *
from bson.objectid import ObjectId
from database import *
from models.user import *
from models.menu import *
# trial
#post= Post("bah","amin333")
# always call this method
Database.initialize()


menu = menu()

menu.run_menu()