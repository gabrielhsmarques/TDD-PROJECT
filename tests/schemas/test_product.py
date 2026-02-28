from uuid import UUID
from pydantic import ValidationError
import pytest

from store.schemas.product import ProductIn


def test_schemas_validated():
    data = {"name": "Iphone 17", "quantity": 20, "price": 6.300, "status": True}
    product = ProductIn(**data)

    assert product.name == "Iphone 17"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "Iphone 17", "quantity": 20, "price": 6.300}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 17", "quantity": 20, "price": 6.3},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
