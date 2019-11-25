from __future__ import print_function
import logging

import grpc
from decouple import config

from adenine.stubs import common_pb2
from adenine.stubs import common_pb2_grpc

class Common():
    def generate_api_request(self, secret_key, did):
        # NOTE(gRPC Python Team): .close() is possible on a channel and should be
        # used in circumstances in which the with statement does not fit the needs
        # of the code.
        grpc_server = "%s:%s" % (config('GRPC_SERVER_HOST'), config('GRPC_SERVER_PORT'))
        
        with grpc.insecure_channel(grpc_server) as channel:
            stub = common_pb2_grpc.CommonStub(channel)
            response = stub.GenerateAPIRequest(common_pb2.Request(secret_key=secret_key, did=did))
            return response
        
