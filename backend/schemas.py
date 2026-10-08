from pydantic import BaseModel


class AccountCreate(BaseModel):
    name: str
    institution: str
    account_type: str


class AccountResponse(AccountCreate):
    id: int
    model_config = {"from_attributes": True}