import grpc
from server_pb2 import EmptyRequest
from server_pb2_grpc import PatternsStub


def run():
    with grpc.insecure_channel('palitra-app.herokuapp.com:50051') as channel:
        stub = PatternsStub(channel)
        response = stub.GetPatterns(request=EmptyRequest())
        print("Patterns client received: " + str(response))


run()
