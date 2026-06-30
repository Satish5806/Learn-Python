#eagerloading is used to avoid extra query required to access data from joined tables

from models.user import User, Address
from sqlalchemy.orm import contains_eager, joinedload, subqueryload


users = (
    User.query
    .join(User.addresses)
    .options(contains_eager(User.addresses))
    .all()
)

for user in users:
    print(user.addresses)