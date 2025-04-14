# 🎬 CineMatch – Sistema de Recomendação de Filmes

Sistema desenvolvido com o objetivo de recomendar filmes personalizados para usuários com base em seus gostos e histórico de visualização.

---

## 🚀 Tecnologias

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Poetry](https://python-poetry.org/)

## ✅ Pré-requisitos
- [Docker + Docker Compose](https://docs.docker.com/)

---

## 📦 Instalação e Execução

### 1. Clone o projeto

```bash
git clone https://github.com/lucasstecher/cinematch.git
cd cinematch
```

### 2. Crie o arquivo .env

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_DB=cinedb
POSTGRES_PORT=5432
DATABASE_HOST=db
API_PORT = 8001

DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${DATABASE_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```
⚠️ Para rodar via Docker, use db no DATABASE_HOST.

### 3. Suba a aplicação usando Docker

```bash
docker-compose up -d
```

Esse comando irá:

- Subir o banco de dados PostgreSQL

- Instalar as dependências com Poetry

- Criar as tabelas no banco

- Popular automaticamente com dados iniciais (seed)

- Iniciar o servidor FastAPI

### 📘 Documentação da API
Com o servidor rodando, acesse:

```bash
http://localhost:8001/docs
```

---

## ✨ Funcionalidades

- ✅ Cadastro de usuários
- ✅ Cadastro de filmes
- ✅ Avaliação de filmes
- ✅ Registro de visualizações
- ✅ Recomendação personalizada com base em:
  - Filmes assistidos
  - Avaliações feitas
  - Gêneros dos filmes
  - Diretores e atores favoritos (calculados dinamicamente)

---

## 🔧 Endpoints principais

| Método | Rota                                 | Descrição                            |
|--------|--------------------------------------|--------------------------------------|
| GET    | `/users`                             | Lista todos os usuários              |
| POST   | `/users`                             | Cria um novo usuário (via `name` como query param ou form) |
| GET    | `/users/{user_id}`                   | Retorna um usuário específico        |
| GET    | `/movies`                            | Lista todos os filmes disponíveis    |
| GET    | `/movies/{movie_id}`                 | Retorna um filme específico        |
| POST   | `/ratings`                           | Avalia um filme                      |
| POST   | `/movies/{movie_id}/watch`           | Marca um filme como assistido        |
| GET    | `/movies/{user_id}/recommendations`  | Retorna recomendações personalizadas |

> ⚠️ Alguns endpoints esperam dados via `query params` ou `form`.

---

## 🗂️ Estrutura de Pastas

```bash
cinematch/
├── app/
│   ├── __init__.py
│   ├── models/                 # Modelos SQLAlchemy (User, Movie, Rating etc.)
│   ├── repositories/             # Operações diretas com o banco (CRUDs)
│   ├── services/               # Lógica de negócio (ex: recomendação)
│   ├── controllers/            # Camada intermediária entre rotas e serviços
│   ├── routers/                # Rotas da API (users, movies, ratings, etc.)
│   ├── utils/                  # Funções auxiliares (ex: favoritos, score)
│   ├── config.py               # Lê variáveis do .env e configurações gerais
│   ├── database.py             # Conexão com o banco de dados
│   └── main.py                 # Inicializa a aplicação FastAPI
├── scripts/
│   ├── create_tables.py        # Cria todas as tabelas no banco
│   └── seed_data.py            # Popula o banco com dados iniciais
├── Dockerfile                  # Define o ambiente da aplicação
├── docker-compose.yml          # Orquestra app + banco PostgreSQL
├── pyproject.toml              # Configuração do Poetry e dependências
├── README.md                   # Este arquivo :)
└── .env                        # Variáveis de ambiente (não versionado)
```

## 🧠 Observações

- A lógica de recomendação é feita de forma **dinâmica**, com base nas interações reais do usuário.
- O projeto não utiliza Pydantic para entrada ou saída de dados, o que simplifica a estrutura, mas limita a documentação automática no Swagger.
- O projeto segue uma separação clara de responsabilidades entre camadas (repository, service, controller e router).
- Os scripts de criação e seed são separados em scripts/, facilitando manutenção e execução manual ou via Docker.

---

Feito com ☕, FastAPI e força de vontade.
