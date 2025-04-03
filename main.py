from fastapi import FastAPI
from service import facebook, tiktok
from api import types

app = FastAPI()



@app.post("/facebook/ads")
async def fb_ads_list(request: types.FacebookRequest) -> types.Response:
    result = await facebook.search_ads(request)
    if isinstance(result, Exception):
        return types.Response(
            status="error",
            message=str(result),
        )
    return types.Response(
        status="success",
        data=result
    )


@app.post("/tiktok/ads")
async def tiktok_ads_list(request: types.TiktokRequest) -> types.Response:
    result = await tiktok.search_ads(request)
    if isinstance(result, Exception):
        return types.Response(
            status="error",
            message=str(result),
        )
    return types.Response(
        status="success",
        data=result
    )