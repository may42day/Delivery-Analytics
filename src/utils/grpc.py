import threading
import grpc
import sys
from repository.user_repository import insert_reg_info

sys.path.append("../build")

import analytics_pb2
import analytics_pb2_grpc
import users_pb2_grpc
import users_pb2
from config import GRPC_ANALYTICS_ADDRESS, GRPC_USER_ADDRESS
from threading import Thread
import asyncio

grpc_thread = None
shutdown_event = threading.Event()


async def start_grpc_server():
    grpc_thread = Thread(target=asyncio.run, args=(serve_grpc(),))
    grpc_thread.start()


async def stop_grpc_server():
    print("start stoping server")
    shutdown_event.set()


async def serve_grpc():
    grpc_server = grpc.aio.server()
    analytics_pb2_grpc.add_analyticsServicer_to_server(
        AnalyticsGrpcServer(), grpc_server
    )
    grpc_server.add_insecure_port(GRPC_ANALYTICS_ADDRESS)
    await grpc_server.start()
    print("Server started, listening on " + GRPC_ANALYTICS_ADDRESS)
    # await grpc_server.wait_for_termination()
    shutdown_event.wait()
    print("stop(0)")
    await grpc_server.stop(0)


class AnalyticsGrpcServer(analytics_pb2_grpc.analytics):
    async def SaveRegInfo(
        self, request: analytics_pb2.SaveRegRequest, context: grpc.aio.ServicerContext
    ) -> analytics_pb2.SaveRegResponse:
        print(request)
        registration_info = {
            "uuid": request.uuid,
            "role": request.role,
            "created_at": request.created_at,
        }
        await insert_reg_info(registration_info)
        return analytics_pb2.SaveRegResponse(record_created=True)

    async def SaveOrderInfo(
        self, request: analytics_pb2.SaveOrderRequest, _context
    ) -> analytics_pb2.SaveRegResponse:
        # order_info
        return analytics_pb2.SaveOrderResponse(record_created=True)


async def send_token_to_user_service(token: str) -> str:
    with grpc.insecure_channel(GRPC_USER_ADDRESS) as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.SendTokenClaims(users_pb2.TokenClaimsRequest(token=token))
    return response.role


async def serve_grpc():
    grpc_server = grpc.aio.server()
    analytics_pb2_grpc.add_analyticsServicer_to_server(
        AnalyticsGrpcServer(), grpc_server
    )
    grpc_server.add_insecure_port(GRPC_ANALYTICS_ADDRESS)
    await grpc_server.start()
    await grpc_server.wait_for_termination()
