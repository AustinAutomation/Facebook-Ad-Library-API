from httpx import AsyncClient, Response
import json
from typing import Dict
from api import types
import os



async def search_ads(request: types.FacebookRequest) -> Dict:
    try:
        payload = {
            'av': '0',
            'dpr': '1',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdLibraryMobileFocusedStateProviderRefetchQuery',
            'variables': json.dumps({
                "activeStatus": "ACTIVE",
                "adType": "ALL",
                "audienceTimeframe": "LAST_7_DAYS",
                "bylines": [],
                "contentLanguages": [],
                "countries": ["ALL"],
                "country": "ALL",
                "excludedIDs": [],
                "fetchPageInfo": False,
                "fetchSharedDisclaimers": False,
                "isTargetedCountry": False,
                "location": None,
                "mediaType": "ALL",
                "multiCountryFilterMode": None,
                "pageIDs": [],
                "potentialReachInput": [],
                "publisherPlatforms": [],
                "queryString": f"\"{request.query}\"",
                "regions": [],
                "searchType": "KEYWORD_EXACT_PHRASE",
                "sortData": None,
                "source": None,
                "startDate": None,
                "viewAllPageID": "0"
            }),
            'server_timestamps': 'true',
            'doc_id': '28754955950818960',
        }
        async with AsyncClient(proxy=os.getenv("PROXY"), timeout=30) as client:
            response: Response = await client.post(
                url="https://web.facebook.com/api/graphql/", 
                data=payload, 
                headers={"content-type": "application/x-www-form-urlencoded"},
            )
            return json.loads(response.text.splitlines()[1])['data']['ad_library_main']['search_results_connection']
    except Exception as e:
        return e
