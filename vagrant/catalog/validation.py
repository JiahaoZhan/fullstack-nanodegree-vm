from itemCatalog import session
from databaseSetup import Base, User, Item

def checkDuplicateUser(username):
    user = session.query(User).filter_by(username = username).first()
    if (user == None):
        return False
    else:
        return True

def checkDuplicateItem(itemName):
    item = session.query(Item).filter_by(itemName = itemName).first()
    if (item == None):
        return False
    else: 
        return True

def validateLogin(username, password):
    user = session.query(User).filter_by(username = username).first()
    if (user.pwd != password):
        return False
    else:
        return True