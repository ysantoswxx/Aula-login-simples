#Criar um sistema SSR 

from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


app = FastAPI(title="Sistema de login simples")

#Roda o código:
#python -m uvicorn main:app --reload

templates = Jinja2Templates(directory="templates")

#Rota método HHTP (get, post)

@app.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro.html",
        {"request": request}
    )

#tela de login
@app.get("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}    )

#tela inicial
@app.get("/")
def tela_inicio(request: Request):
    return templates.TemplateResponse(
        request,
        "tela_inicial.html",
        {"request": request}
    )