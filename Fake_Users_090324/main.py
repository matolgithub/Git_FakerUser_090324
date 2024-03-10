from faker import Faker


def make_users():
    # fake_user = Faker("RU")
    # name = fake_user.name()
    # job = fake_user.job()
    # address = fake_user.address()
    # city = fake_user.city()
    # country = fake_user.country()
    # region = fake_user.region()
    # bank = fake_user.bank()
    # company = fake_user.company()
    # inn = fake_user.individuals_inn()
    # ogrn = fake_user.individuals_ogrn()
    # card = fake_user.credit_card_full()
    # emoji = fake_user.emoji()
    # email = fake_user.email()
    # phone = fake_user.phone_number()
    # agent = fake_user.user_agent()
    # print(
    #     f"{name}\n{job}\n{address}\n{city}\n{country}\n{region}\n{bank}\n{company}\n{inn}\n{ogrn}\n{card}\n{emoji}\n{email}\n{phone}\n{agent}")
    for num in range(1, 11):
        user = Faker("EN")
        name = user.name()
        address = user.address()
        print(f"{num}. {name}, {address}")


if __name__ == "__main__":
    make_users()
