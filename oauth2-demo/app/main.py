from typing import Optional, List

import jwt
from fastapi import FastAPI, Header, HTTPException


app = FastAPI()


# Kubernetes probes
@app.get("/alive")
async def read_root():
    return {"status": "alive"}


@app.get("/ready")
async def read_root():
    return {"status": "ready"}


@app.get("/startup")
async def read_root():
    return {"status": "startup"}


# app routes
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/me")
async def read_token(x_forwarded_access_token: Optional[str] = Header(None)):
    if x_forwarded_access_token:
        # token was passed
        data = jwt.decode(x_forwarded_access_token, options={"verify_signature": False})
        return {"Token": data}
    else:
        raise HTTPException(status_code=403, detail="Token not found")


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
