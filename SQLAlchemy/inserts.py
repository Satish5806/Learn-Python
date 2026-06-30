from models.user import Address, Preference, Role, User
from main import session

admin_role = Role.query.filter(Role.slug == "admin").first()

user = User(
    first_name="Roronoa",
    last_name="Zoro",
    email="roronoazoro@gmail.com"
)

session.add(user)

user2 = User()
user2.first_name = "Monkey"
user2.last_name = "Luffy"
user2.email = "monkeyluffy@gmail.com"

session.add(user2)

user3 = User(
    first_name = "Sanji",
    last_name = "Vinsmoke",
    email = "vinsmokesanji@gmail.com"
)

user3.roles.append(admin_role)
user3.addresses.append(
    Address(
        road_name = "34 main road",
        postcode = "58630",
        city = "London"
    )
)
user3.preference = Preference(
    language = "English",
    currency = "GBP"
)

session.add(user3)

session.commit()