from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from typing import Annotated

app = FastAPI()

# First Steps

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

@app.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
  return {"token": token}
