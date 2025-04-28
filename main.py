import os
import platform
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId

def limpar_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

limpar_console()

uri = "mongodb+srv://gustavogarbim0:oIi8L6SUwpS5lmEy@uc3.nhjgasy.mongodb.net/?retryWrites=true&w=majority&appName=UC3"
client = MongoClient(uri)
db = client['forum']
posts_collection = db['posts']

try:
    client.admin.command('ping')
    print("""
     ▄████  ▄▄▄       ██▀███   ▄▄▄▄    ██▓ ███▄ ▄███▓ ▐██▌
    ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▓█████▄ ▓██▒▓██▒▀█▀ ██▒ ▐██▌
   ▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒ ▄██▒██▒▓██    ▓██░ ▐██▌
   ░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  ▒██░█▀  ░██░▒██    ▒██  ▓██▒
   ░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒░▓█  ▀█▓░██░▒██▒   ░██▒ ▒▄▄ 
    ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▒▓███▀▒░▓  ░ ▒░   ░  ░ ░▀▀▒
     ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░▒░▒   ░  ▒ ░░  ░      ░ ░  ░
   ░ ░   ░   ░   ▒     ░░   ░  ░    ░  ▒ ░░      ░       ░
         ░       ░  ░   ░      ░       ░         ░    ░   
                                ░                     
    """)
except Exception as e:
    print("Deu merda na conexão com o MongoDB:", e)

app = FastAPI()

# liberando o CORS pra não dar erro no frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Post(BaseModel):
    tipo: str
    area: str
    titulo: str
    descricao: str
    nome: str
    data_publicacao: str  # tipo 2025-04-27

@app.post("/posts")
def criar_post(post: Post):

    try:
        posts_collection.insert_one(post.dict())
        return {"mensagem": "Post criado com sucesso!"}
    
    except Exception as e:
        return {"erro": f"Não deu pra criar o post: {e}"}


@app.get("/posts", response_model=List[Post])
def listar_posts():
    
    try:
        posts = []
        for p in posts_collection.find():
            posts.append(Post(
                tipo=p.get('tipo', ''),
                area=p.get('area', ''),
                titulo=p.get('titulo', ''),
                descricao=p.get('descricao', ''),
                nome=p.get('nome', 'Novo usuário'),
                data_publicacao=p.get('data_publicacao', datetime.now().strftime("%Y-%m-%d")),
            ))
        return posts
    
    except Exception as e:
        print("Erro ao listar posts:", e)
        
        return []
