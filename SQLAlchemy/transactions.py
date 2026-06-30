from models.user import Preference, User
from main import session

user = User(
    first_name = "Tony",
    last_name = "Chopper",
    email = "tonychopper@gmail.com"
)

session.add(user)


raise Exception("Something went wrong")

preference = Preference(
    language = "English",
    currency = "GBP"
)

preference.user = user
session.commit() #adding commit() at the end of add such that either all is committed or non 