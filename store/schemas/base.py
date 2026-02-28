from datetime import datetime
from decimal import Decimal
import uuid
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator(mode="before")
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data
