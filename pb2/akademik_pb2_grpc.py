# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb2 import akademik_pb2 as akademik__pb2


class CalculatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.science_for_everyone = channel.unary_unary(
        '/Calculator/science_for_everyone',
        request_serializer=akademik__pb2.inputs.SerializeToString,
        response_deserializer=akademik__pb2.return_x.FromString,
        )


class CalculatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def science_for_everyone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'science_for_everyone': grpc.unary_unary_rpc_method_handler(
          servicer.science_for_everyone,
          request_deserializer=akademik__pb2.inputs.FromString,
          response_serializer=akademik__pb2.return_x.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
