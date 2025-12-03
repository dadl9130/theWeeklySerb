from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]
class CategoryModel(BaseModel):
    """
    Container for a single student record.
    """
    # The primary key for the StudentModel, stored as a `str` on the instance.
    # This will be aliased to ``_id`` when sent to MongoDB,
    # but provided as ``id`` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    slug: str = Field(...)
    description: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Leben",
                "slug": "leben",
                "description": "Alles rund ums Leben"
            }
        },
    )