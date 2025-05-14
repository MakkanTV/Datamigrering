
from db import init_db, session
from models import Customer, Account

def main():
    init_db()

    db = session()


    customer = Customer(name="Max", ssn="7001092445", email = "Benjamin@exempel.se")
    db.add(customer)
    db.commit()

    account = Account(name="Max", balance=3000, customer_id=customer.id)
    db.add(account)
    db.commit()

    print(f"{customer.name}({customer.email}) har saldo {account.balance}")

    db.close()

if __name__ == "__main__":
    main()