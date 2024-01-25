import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from accessToken import AccessToken
from config import ConfigFile
from fastapi import Request

app = FastAPI(
    title="Token",
    description="This application 'Token', generate token using framework FastAPI",
    version="0.0.1",
    contact={
        "name": "Daniel Goldacker",
        "url": "https://github.com/daniel-goldacker",
        "email": "daniel-goldacker@hotmail.com",
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ConfigFile.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Jinja2 template configuration
templates = Jinja2Templates(directory="./src/html")

# Route to serve ssr.html
@app.get("/ssr")
def read_root(request: Request):
    # Gera um token de exemplo
    username = "testuser"
    token = AccessToken.createToken(username)
    
    return templates.TemplateResponse("ssr.html", {"request": request, "token": token})


# Route to serve csr.html
@app.get("/csr")
def read_root(request: Request):
    return templates.TemplateResponse("csr.html", {"request": request})


# Route to serve /token
@app.post("/token")
def login_for_access_token(username: str, password: str):
    user = ConfigFile.FAKE_USERS_DB.get(username)
    if user is None or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": AccessToken.createToken(username), "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
