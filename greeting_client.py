import os
import grpc

import proto.greeting_pb2 as greeting_pb2
import proto.greeting_pb2_grpc as greeting_pb2_grpc


class GreetingService:
    def __init__(self):
        host = os.environ.get('ARTICLE_HOST', '0.0.0.0:50052')
        channel = grpc.insecure_channel(host)
        self.stub = greeting_pb2_grpc.GreeterStub(channel)

    def greeting(self, name, greeting):
        response = self.stub.greet(greeting_pb2.ClientInput(name=name, greeting=greeting))
        return response.message
# def run():
#     with grpc.insecure_channel('localhost:50052') as channel:
#         stub = greeting_pb2_grpc.GreeterStub(channel)
#         response = stub.greet(greeting_pb2.ClientInput(name='John', greeting="Yo"))
#     print("Greeter client received following from server: " + response.message)
#
#
# if __name__ == "__main__":
#     run()
