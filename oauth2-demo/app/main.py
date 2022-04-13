from typing import Optional, List

import jwt
from fastapi import FastAPI, Header, HTTPException


app = FastAPI()


# app routes
@app.get("/")
async def get_root():
    return {"Hello": "World"}


@app.get("/me")
async def get_me(x_forwarded_access_token: str = Header(None)):
    data = jwt.decode(x_forwarded_access_token, options={"verify_signature": False})
    return {"Token": data}


@app.get("/items/{item_id}")
async def get_item(item_id: int, x_forwarded_access_token: Optional[str] = Header(None)):
    if x_forwarded_access_token:
        data = jwt.decode(x_forwarded_access_token, options={"verify_signature": False})
        mail = data["Email"]
        return {"item_id": item_id, "Email": mail}
    else:
        return {"item_id": item_id, "Email": "not given"}

