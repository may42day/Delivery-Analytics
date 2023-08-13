from fastapi import FastAPI
from routes.api.v1_config import v1_api_router
from middleware.auth_middleware import check_token_claims
from starlette.middleware.base import BaseHTTPMiddleware
from utils.grpc import serve_grpc, start_grpc_server, stop_grpc_server

app = FastAPI(title="Analytics Service")

app.include_router(v1_api_router)

@app.on_event("startup")
async def startup():
    await start_grpc_server()

@app.on_event("shutdown")
async def shutdown():
    await stop_grpc_server()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8090)
