from fastapi import FastAPI
from sqlalchemy import select
from database import SessionLocal
from models import Account
from schemas import AccountCreate, AccountResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Budget Tracker API"}


@app.get("/accounts", response_model=list[AccountResponse])
def get_accounts():
    with SessionLocal() as db:
        statement = select(Account)
        accounts = db.scalars(statement).all()

        return accounts


@app.post("/accounts",response_model=AccountResponse, status_code=201)
def create_account(account_data: AccountCreate):
    with SessionLocal() as db:
        new_account = Account(name=account_data.name, institution=account_data.institution, account_type=account_data.account_type)
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return new_account