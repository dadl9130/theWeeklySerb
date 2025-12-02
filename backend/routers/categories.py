from fastapi import APIRouter
from database import categories_collection
from collection.categoryCollection import CategoryCollection 

router = APIRouter()

@router.get("/categories/", response_model=CategoryCollection)
def get_categories():
    categories = categories_collection.find().to_list(1000)

    return CategoryCollection(categories=categories)
