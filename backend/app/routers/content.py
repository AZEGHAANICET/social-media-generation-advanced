from fastapi import APIRouter, Depends, HTTPException
from app.services.content_generator import  ContentGenerator
from ..schemas import ContentRequest, HashtagRequest,PostIdeasRequest



content_router = APIRouter()


@content_router.post("/generate/caption")
async def generate_caption(request:ContentRequest, content_gen: ContentGenerator = Depends(ContentGenerator)):
    try:
        result = await content_gen.generate_caption(
            **request.dict()
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@content_router.post("/generate/hashtags")
async def generate_hashtags(request:HashtagRequest, content_gen: ContentGenerator = Depends(ContentGenerator) ):
    try:
        result = await content_gen.generate_hashtags(**request.dict())
        return {
            "hashtags": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@content_router.post("/generate/post-ideas")
async def generate_post_ideas(
        request: PostIdeasRequest, content_gen: ContentGenerator = Depends(ContentGenerator)
):
    try:
        result = await content_gen.generate_post_idea(**request.dict())
        return {
            "ideas": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
