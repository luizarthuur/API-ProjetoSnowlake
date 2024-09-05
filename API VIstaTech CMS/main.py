from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request




app = FastAPI(title='API (FastAPI + SQLalchemy) - CMS VistaTech')
app.include_router(api_router, prefix=settings.API_V1_STR)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",  # Adicione esta linha
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# /api/v1/texto e /api/v1/imagens

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)