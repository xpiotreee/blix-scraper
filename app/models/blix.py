from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

class Shop(BaseModel):
    title: str
    slug: str
    url: HttpUrl
    image: HttpUrl

class LeafletPreview(BaseModel):
    brand_name: str
    brand_slug: str
    id: str
    name: str
    start: datetime
    end: datetime
    url: HttpUrl
    image: HttpUrl

class Offer(BaseModel):
    brand: str
    start: datetime
    end: datetime
    image: HttpUrl
    manufacturer: Optional[str]
    name: str
    price: Optional[int] = None
    discount: int

