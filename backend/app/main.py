from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.routers.content import content_router

app = FastAPI(title="Content Generator API",
    description="Generate captions, hashtags, and post ideas",
    version="1.0.0")



app.add_middleware(CORSMiddleware, allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(content_router, prefix="/api/")

@app.get("/")
async def root():
    return {"message": "Content Generator API running "}