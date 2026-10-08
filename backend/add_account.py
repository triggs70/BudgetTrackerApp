from database import SessionLocal
from models import Account

db = SessionLocal()

account = Account(name="CIBC Chequing", institution="CIBC", account_type="chequing")
db.add(account)
db.commit()
db.refresh(account)
print(f"Created account with ID: {account.id}")
db.close()