from itemCatalog import session
from databaseSetup import Base, User, Item

def checkDuplicateUser(username):
    user = session.query(User).filter_by(username = username).first()
    if (user == None):
        return False
    else:
        return True
