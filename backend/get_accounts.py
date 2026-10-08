from sqlalchemy import select
from database import SessionLocal
from models import Account


with SessionLocal() as db:
    statement = select(Account)
    accounts = db.scalars(statement).all()
    for account in accounts:
        print(f"{account.id}: {account.name} ({account.account_type})")