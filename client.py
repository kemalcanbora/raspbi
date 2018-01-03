import grpc

from pb2 import akademik_pb2_grpc
from pb2 import akademik_pb2

channel = grpc.insecure_channel('192.168.8.101:50051')

stub = akademik_pb2_grpc.CalculatorStub(channel)
number = akademik_pb2.inputs(a ="bitcoin" ,
                             b="kemalcanbora@gmail.com" ,
                             c=5)

response = stub.science_for_everyone(number)

print(response.value)