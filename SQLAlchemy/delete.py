from models.user import User
from main import session


user = User.query.first()

print(user)

session.delete(user)
session.commit()

user = User.query.first()
print(user)

user = User.query.filter_by(first_name = "Tony").first()
# session.delete(user)
# session.commit()