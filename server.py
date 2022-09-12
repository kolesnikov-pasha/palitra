from concurrent import futures
import logging

import grpc
from server_pb2_grpc import PatternsServicer, add_PatternsServicer_to_server
from server_pb2 import PatternsCollection, Pattern, Rect

class Patterns(PatternsServicer):

  def GetPatterns(self, request, context):
    return PatternsCollection(patterns=[
        Pattern(
            image=Rect(left=0, top=0, right=1, bottom=1),
            colors=[
                Rect(left=0, top=1, right=1/4, bottom=4/3),
                Rect(left=1/4, top=1, right=1/2, bottom=4/3),
                Rect(left=1/2, top=1, right=3/4, bottom=4/3),
                Rect(left=3/4, top=1, right=1, bottom=4/3)
            ]
    )])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PatternsServicer_to_server(Patterns(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()