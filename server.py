import grpc 
from concurrent import futures
import time
import number_square_pb2
import number_square_pb2_grpc

class Servicer(number_square_pb2_grpc.squareServicer):
    def num_square(self, request_iterator, context):
        for request in request_iterator:
            print("Number recieved from client : ", request.number)
            num = int(request.number)
            reply = number_square_pb2.reply()
            reply.square = str(num*num)
            print("Number sent : ", num*num)

            yield reply
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    number_square_pb2_grpc.add_squareServicer_to_server(Servicer(),server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("server listening...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    