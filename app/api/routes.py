from fastapi import APIRouter, Depends
from app.scraper.scraper import BlixScraper
from aiohttp import ClientSession
from typing import List

from app.models.blix import Shop, LeafletPreview, Offer

router = APIRouter()

async def get_blix_scraper():
    client = ClientSession()
    client.headers.add('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')
    scraper = BlixScraper(client=client)
    try:
        yield scraper
    finally:
        await client.close()

@router.get('/shops', response_model=List[Shop])
async def get_shops(blix: BlixScraper = Depends(get_blix_scraper)):
    data = await blix.get_shops()
    return data

@router.get('/shops/{shop}/leaflets', response_model=List[LeafletPreview])
async def get_leaflets(shop: str, blix: BlixScraper = Depends(get_blix_scraper)):
    data = await blix.get_leaflets(shop)
    return data

@router.get('/shops/{shop}/leaflets/{leaflet}', response_model=List[Offer])
async def get_leaflet(shop: str, leaflet: str, blix: BlixScraper = Depends(get_blix_scraper)):
    data = await blix.get_leaflet(shop=shop, id=leaflet)
    return data