# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='status.proto',
  package='atakmap.commoncommo.protobuf.v1',
  syntax='proto3',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cstatus.proto\x12\x1f\x61takmap.commoncommo.protobuf.v1\"\x19\n\x06Status\x12\x0f\n\x07\x62\x61ttery\x18\x01 \x01(\rB\x02H\x03\x62\x06proto3'
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='atakmap.commoncommo.protobuf.v1.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery', full_name='atakmap.commoncommo.protobuf.v1.Status.battery', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:atakmap.commoncommo.protobuf.v1.Status)
  })
_sym_db.RegisterMessage(Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
