import time
from concurrent import futures

import grpc
import science_for_everyone

from pb2 import akademik_pb2
from pb2 import akademik_pb2_grpc

class CalculatorServicer(akademik_pb2_grpc.CalculatorServicer):

    def science_for_everyone(self, input, context):

        response = akademik_pb2.return_x(value=science_for_everyone.main(input.a,
                                                                         input.b,
                                                                         input.c))

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
akademik_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)