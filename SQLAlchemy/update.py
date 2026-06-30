from main import session
from models.user import Preference, User


# user_preference = (
#     Preference.query
#     .join(Preference.user)
#     .filter(User.email == "johndoe@gmail.com")
#     .first()
# )

# user_preference.currency = "GBP"
# session.commit()

User.query \
    .filter(User.first_name == "John")\
    .filter(User.last_name == "Doe")\
    .update({"email": "johndoe01@gmail.com"})

session.commit()

user = User.query.filter_by(first_name = "John", last_name = "Doe").first()

# print(user_preference.currency)
print(user.email)