from asyncio import gather
from fastapi import APIRouter
from converter import sync_converter, async_converter
import time

router = APIRouter(prefix="/converter")

# path parameter
# query parameter

# body parameter
#/url?to_currencies=USD,EUR,GBP&price=5.55

@router.get("/{from_currency}")
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

@router.get("/async/{from_currency}")
async def async_converter_router(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")

    courotines = []

    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        courotines.append(coro)

    result = await gather(*courotines)
    return result





