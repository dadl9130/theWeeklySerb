from pydantic import BaseModel 
from schema.categoryName import CategoryNameSlugSchema 

class CategoryCollection(BaseModel): 
    categories: list[CategoryNameSlugSchema]