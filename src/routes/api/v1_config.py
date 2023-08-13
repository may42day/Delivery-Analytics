from fastapi import APIRouter
from .v1.orders_routes import router as orders_router
from .v1.products_routes import router as products_router
from .v1.queue_routes import router as queue_router
from .v1.users_routes import router as users_router

v1_api_router = APIRouter(prefix="/api/v1")

v1_api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
v1_api_router.include_router(products_router, prefix="/products", tags=["Products"])
v1_api_router.include_router(queue_router, prefix="/queue", tags=["Queue"])
v1_api_router.include_router(users_router, prefix="/users", tags=["Users"])
