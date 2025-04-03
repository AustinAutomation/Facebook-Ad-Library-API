from httpx import AsyncClient, Response
from typing import Dict, List
from api import types
import os
from datetime import datetime



async def search_ads(request: types.TiktokRequest) -> List[Dict]:
    try:
        start_time = "1664564400"
        end_time = int(datetime.now().timestamp())
        json_data = {
            'query': request.query,
            'query_type': '1',
            'adv_biz_ids': '',
            'order': 'last_shown_date,desc',
            'offset': 0,
            'search_id': '',
            'limit': 12,
        }
        async with AsyncClient(proxy=os.getenv("PROXY"), timeout=30) as client:
            response: Response = await client.post(
                f'https://library.tiktok.com/api/v1/search?region=all&type=1&start_time={start_time}&end_time={end_time}', 
                json=json_data
            )
            return response.json()['data']
    except Exception as e:
        return e