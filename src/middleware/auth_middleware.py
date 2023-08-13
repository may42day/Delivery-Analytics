from fastapi import HTTPException, Request

from utils.grpc import send_token_to_user_service
from fastapi.responses import JSONResponse


async def check_token_claims(request: Request, call_next):
    if request.client.host == "127.0.0.1" and (
        request.url.path.startswith("/docs")
        or request.url.path.startswith("/redoc")
        or request.url.path.startswith("/openapi.json")
    ):
        response = await call_next(request)
        return response

    token_header_value = request.headers.get("authorization")
    if token_header_value.startswith("Bearer "):
        token = token_header_value.split(" ")[1]
        claims_from_response = await send_token_to_user_service(token)
        if claims_from_response == "ANALYST":
            response = await call_next(request)
            return response

    # TO DO: token expiration
    # TO DO: logs
    return JSONResponse(content="Invalid Token", status_code=403)
