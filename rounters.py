from fastapi import APIRouter
from converter import sync_converter
import time

router = APIRouter()

# path parameter
# query parameter

# body parameter
#/url?to_currencies=USD,EUR,GBP&price=5.55

@router.get("/converter/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")

    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result.append(response)
        time.sleep(1.2)

    return result





