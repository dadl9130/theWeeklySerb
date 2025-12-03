from pydantic import BaseModel 
from typing import Optional 

class CategoryNameSlugSchema(BaseModel): 
    name: str
    slug: str