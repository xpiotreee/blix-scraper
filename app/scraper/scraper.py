from datetime import datetime
from lxml import etree
import aiohttp
import json
import re


BLIX_URL = 'https://blix.pl'
parser = etree.HTMLParser()

class BlixScraper:
    def __init__(self, client: aiohttp.ClientSession):
        self.client = client
    
    async def request(self, url):
        if not url.startswith('http'):
            url = f'{BLIX_URL}/{url}'

        async with self.client.get(url) as res:
            content = await res.text('utf-8')
            return  etree.HTML(content, parser)

    async def get_shops(self):
        SHOP_XPATH = '/html/body/section[4]/div[2]/a'
        
        root = await self.request('sklepy')
        cards = root.xpath(SHOP_XPATH)
        results = []
        for card in cards:
            img = card.xpath('.//img/@data-src')[0]
            results.append({
                'title': card.get('title'),
                'slug': card.get('href').rstrip('/').split('/')[-1],
                'url': card.get('href'),
                'image': img
            })
        
        return results
    
    async def get_leaflets(self, shop_slug):
        LEAFLET_XPATH = '/html/body/div[4]/section[3]/div[2]/div'

        root = await self.request(f'sklep/{shop_slug}')
        leaflets = root.xpath(LEAFLET_XPATH)
        results = []
        for leaflet in leaflets:
            href = leaflet.xpath('.//a/@href')[0]
            img = leaflet.xpath('.//source/@data-srcset')[0]
            results.append({
                'brand_name': leaflet.get('data-brand-name'),
                'brand_slug': leaflet.get('data-brand-slug'),
                'id': leaflet.get('data-leaflet-id'),
                'name': leaflet.get('data-leaflet-name'),
                'start': datetime.strptime(leaflet.get('data-date-start'), "%B %d, %Y %H:%M"),
                'end': datetime.strptime(leaflet.get('data-date-end'), "%B %d, %Y %H:%M"),
                'url': href,
                'image': img
            })

        return results
    
    async def get_leaflet(self, url = None, shop = None, id = None):
        LEAFLET_META_XPATH = '//script[contains(text(), "window.offer")]'
        if url:
            root = await self.request(url)
        elif shop and id:
            root = await self.request(f'sklep/{shop}/gazetka/{id}')
        else:
            return []

        script = root.xpath(LEAFLET_META_XPATH)[0].text
        match = re.search(r'window\.offers\s* = \s*(\[.*\])', script, re.DOTALL)
        if match:
            offers = json.loads(match.group(1))
            return [{
                'brand': offer['brandName'],
                'start': offer['dateStart']['date'],
                'end': offer['dateEnd']['date'],
                'image': offer['image'],
                'manufacturer': offer['manufacturerName'],
                'name': offer['name'],
                'price': offer['price'],
                'discount': offer['percentDiscount']
            } for offer in offers]
        else:
            return []


