import number_square_pb2
import number_square_pb2_grpc
import time
import grpc

def get_client_strean_requests():
    while True:
        num = input("Enter a number : ")

        if num =="":
            break

        request = number_square_pb2.request(number = num)
        yield request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = number_square_pb2_grpc.squareStub(channel)
        responses = stub.num_square(get_client_strean_requests())

        for response in responses:
            print("Response from server : ", response.square)

if __name__ == "__main__":
    run()