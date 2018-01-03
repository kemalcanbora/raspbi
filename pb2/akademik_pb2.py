# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: akademik.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='akademik.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x61kademik.proto\")\n\x06inputs\x12\t\n\x01\x61\x18\x04 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\t\x12\t\n\x01\x63\x18\x05 \x01(\x05\"\x19\n\x08return_x\x12\r\n\x05value\x18\x01 \x03(\t28\n\nCalculator\x12*\n\x14science_for_everyone\x12\x07.inputs\x1a\t.return_xb\x06proto3')
)




_INPUTS = _descriptor.Descriptor(
  name='inputs',
  full_name='inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='inputs.a', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='inputs.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c', full_name='inputs.c', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=59,
)


_RETURN_X = _descriptor.Descriptor(
  name='return_x',
  full_name='return_x',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='return_x.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['inputs'] = _INPUTS
DESCRIPTOR.message_types_by_name['return_x'] = _RETURN_X
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

inputs = _reflection.GeneratedProtocolMessageType('inputs', (_message.Message,), dict(
  DESCRIPTOR = _INPUTS,
  __module__ = 'akademik_pb2'
  # @@protoc_insertion_point(class_scope:inputs)
  ))
_sym_db.RegisterMessage(inputs)

return_x = _reflection.GeneratedProtocolMessageType('return_x', (_message.Message,), dict(
  DESCRIPTOR = _RETURN_X,
  __module__ = 'akademik_pb2'
  # @@protoc_insertion_point(class_scope:return_x)
  ))
_sym_db.RegisterMessage(return_x)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=88,
  serialized_end=144,
  methods=[
  _descriptor.MethodDescriptor(
    name='science_for_everyone',
    full_name='Calculator.science_for_everyone',
    index=0,
    containing_service=None,
    input_type=_INPUTS,
    output_type=_RETURN_X,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
