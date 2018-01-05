import grpc

from pb2 import akademik_pb2_grpc
from pb2 import akademik_pb2

channel = grpc.insecure_channel('127.0.0.1:50051')

stub = akademik_pb2_grpc.CalculatorStub(channel)
number = akademik_pb2.inputs(a ="nlp" ,
                             b="kemalcanbora@gmail.com" ,
                             c=10)

stub.science_for_everyone(number)
