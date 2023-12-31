from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from ..operations.router import get_specific_operations

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search/{operation_type}")
def get_base_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("operations/search.html", {"request": request, "operations": operations["data"]})


@router.get("/search")
def get_base_page(request: Request):
    return templates.TemplateResponse("operations/search.html", {"request": request})


@router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse("chat/chat.html", {"request": request})
