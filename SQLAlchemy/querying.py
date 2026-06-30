from sqlalchemy import desc

from main import session
from models.user import User, Preference, Address, Role

#Seeding Test Users

# users_to_add = [
#     User(first_name="John", last_name="Doe", email="johndoe@gmail.com"),
#     User(first_name="Jane", last_name="Smith", email="janesmith@gmail.com"),
#     User(first_name="Bob", last_name="Johnson", email="bobjohnson@gmail.com"),
#     User(first_name="Alice", last_name="Lee", email="alicelee@example.com"),
#     User(first_name="David", last_name="Kim", email="davidkim@example.com"),
#     User(first_name="Emily", last_name="Nguyen", email="emilynguyen@example.com"),
#     User(first_name="Michael", last_name="Davis", email="michaeldavis@example.com")
# ]

# session.add_all(users_to_add)
# session.commit()
#This code should be run only once to add the data to the database otherwise running code multiple times will put in the database for the number of times it is run
#Users added successfully

all_users = User.query.all()
first_user = User.query.first()

# satishs = User.query.filter_by(first_name="Satish").all() #or
# satishs = User.query.filter(User.first_name =="Satish").all()

#All users using gmail
gmail_users = User.query.filter(User.email.ilike("%@gmail.com")).all()

super_admins = (
    User.query
    .join(User.roles)
    .filter(Role.slug =="super-admin")
    .all()
)


users_by_name = (
    User.query
    .order_by("first_name")
    .all()
)


users_by_name_desc = (
    User.query
    .order_by(desc("first_name"))
    .all()
)

users_by_name_desc = (
    User.query
    .order_by(desc("first_name"))
    .order_by(desc("last_name"))
    .all()
)


first_three_users= User.query.limit(3).all()

skip_three_users = User.query.offset(3).all()


num_of_users = User.query.count()

print(f"The number of users is: {num_of_users}")

# print(skip_three_users)

# print(first_three_users)

# print(users_by_name_desc)

# print(super_admins)

# print(all_users)
# print(satishs)

# print(gmail_users)