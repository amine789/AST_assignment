
from models.post import *
from bson.objectid import ObjectId
from database import *

# trial
post= Post("hi2","vancou2ver",113,datetime.datetime.utcnow())
# always call this method
Database.initialize()
# save something to database
post.save_to_mongo()

p=Post.from_timeline(113)

# retrieve from database and print
for pk in p:
    print(pk)