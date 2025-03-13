# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.coffees_api_base import BaseCoffeesApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt
from typing import Any, List
from openapi_server.models.coffee import Coffee
from pydantic import BaseModel
from typing import  Optional


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)

class Coffee(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

coffees = []


@router.post(
    "/coffees",
    responses={
        201: {"description": "Coffee drink added successfully"},
    },
    tags=["Coffees"],
    summary="Add a new coffee drink",
    response_model_by_alias=True,
)
async def add_coffee(
    coffee: Coffee,
) -> None:
    for existing_coffee in coffees:
        if existing_coffee.id == coffee.id:
            raise HTTPException(status_code=400, detail="Coffee with this ID already exists")
    coffees.append(coffee)
    return {"message": "Coffee added successfully"}
    
    #if not BaseCoffeesApi.subclasses:
        #raise HTTPException(status_code=500, detail="Not implemented")
    #return await BaseCoffeesApi.subclasses[0]().add_coffee(coffee)


@router.delete(
    "/coffees/{coffee_id}",
    responses={
        204: {"description": "Coffee deleted successfully"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Delete a coffee drink",
    response_model_by_alias=True,
)
async def delete_coffee(
    coffee_id: int,
) -> None:
    global coffees
    coffees = [coffee for coffee in coffees if coffee.id != coffee_id]
    return {"message": "Coffee deleted successfully"}
    
    


@router.get(
    "/coffees/{coffee_id}",
    responses={
        200: {"model": Coffee, "description": "Details of the coffee drink"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Get details of a specific coffee drink",
    response_model_by_alias=True,
)
async def get_coffee_by_id(
    coffee_id: int,
) -> Coffee:
    for coffee in coffees:
        if coffee.id == coffee_id:
            return coffee
    raise HTTPException(status_code=404, detail="Coffee not found")

@router.get("/coffees", response_model=List[Coffee],
    responses={
        200: {"model": List[Coffee], "description": "A list of coffee drinks"},
    },
    tags=["Coffees"],
    summary="Get a list of all coffee drinks",
    response_model_by_alias=True,
)
async def get_coffees(
) -> List[Coffee]:
    return coffees

@router.put(
    "/coffees/{coffee_id}",
    responses={
        200: {"description": "Coffee drink updated successfully"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Update a coffee drink",
    response_model_by_alias=True,
)
async def update_coffee(
    coffee_id: int, updated_coffee: Coffee
) -> None:
    for index, coffee in enumerate(coffees):
        if coffee.id == coffee_id:
            coffees[index] = updated_coffee
            return {"message": "Coffee updated successfully"}
    raise HTTPException(status_code=404, detail="Coffee not found")
