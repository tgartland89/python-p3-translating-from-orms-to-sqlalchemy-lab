from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)
    
# passing engine through create_table and base.metadata will clear the following: 
# FAILED lib/dog.py contains function "create_table()" that takes a declarative_base and creates a SQLite database. - 
# TypeError: create_table() takes 1 positional argument but 2 were given

def save(session, dog):
    session.add(dog)

# adding session.add(dog) clears 
# FAILED lib/dog.py contains function "save()" that takes a Dog instance as an argument and saves the dog to the database. 
# - AttributeError: 'NoneType' object has no attribute 'name'

# did not need the session.commit() per the solution: 
    # session.commit()

def get_all(session):
    return session.query(Dog).all()

# adding the return session.query(Dog).all() clears FAILED lib/dog.py contains function "get_all()" that takes a session and returns 
# a list of Dog instances for every record in the database. 
# - TypeError: 'NoneType' object is not subscriptable

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

# adding the return with .filter(Dog.name == name).first() clear FAILED lib/dog.py contains function "find_by_name()" that takes a session 
# and name and returns a Dog instance corresponding to its database record retrieved by name. 
# - AttributeError: 'NoneType' object has no attribute 'name'

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

# adding the above return simmilar to the find_name above, swapping id for name will clear FAILED lib/dog.py contains function 
# "find_by_id()" that takes a session and id and returns a Dog instance corresponding to its database record retrieved by id. 
# - AttributeError: 'NoneType' object has no attribute 'id'

def find_by_name_and_breed(session, name, breed):
# this def is clearing this lib/models.py contains model "Dog" with name and breed attributes. .   
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

# adding this return with name and breed passes FAILED lib/dog.py contains function "find_by_name_and_breed()" 
# that takes a session, a name, and a breed as arguments and returns a Dog instance matching that record. 
# - AttributeError: 'NoneType' object has no attribute 'name'

def update_breed(session, dog, breed):
    dog.breed = breed

# adding the above clears the final two errirs, but there is still the warning:
# FAILED lib/dog.py contains function "create_table()" that takes a declarative_base and creates a SQLite database. - AssertionError: assert False
# FAILED lib/dog.py contains function "update_breed()" that takes a session instance, and breed as arguments and updates the instance's breed. - AssertionError: assert 'cocker spaniel' == 'bulldog'


# did not need the session.commit() or .add(dog) per the solution: 
    # session.add(dog)
    # session.commit()




