import os
import grpc
import proto.user_pb2_grpc as user_pb2_grpc
import proto.user_pb2 as user_pb2



class UserService:
    def __init__(self):
        host = os.environ.get('USER_HOST', '0.0.0.0:50051')
        channel = grpc.insecure_channel(host)

        self.stub = user_pb2_grpc.UserServiceStub(channel)

    def sign_up(self, username, password) -> user_pb2.SignUpResponse:
        r = user_pb2.SignUpRequest(username=username, password=password)
        return self.stub.SignUp(r)
        # send request to grpc server

    def sign_in(self, username, password) -> user_pb2.SignInResponse:

        r = user_pb2.SignInRequest(username=username, password=password)

        # send request to grpc server
        return self.stub.SignIn(r)