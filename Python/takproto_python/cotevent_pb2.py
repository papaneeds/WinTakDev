# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cotevent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import detail_pb2 as detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cotevent.proto',
  package='atakmap.commoncommo.protobuf.v1',
  syntax='proto3',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63otevent.proto\x12\x1f\x61takmap.commoncommo.protobuf.v1\x1a\x0c\x64\x65tail.proto\"\x8d\x02\n\x08\x43otEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\t\x12\x0b\n\x03qos\x18\x03 \x01(\t\x12\x0c\n\x04opex\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\t\x12\x10\n\x08sendTime\x18\x06 \x01(\x04\x12\x11\n\tstartTime\x18\x07 \x01(\x04\x12\x11\n\tstaleTime\x18\x08 \x01(\x04\x12\x0b\n\x03how\x18\t \x01(\t\x12\x0b\n\x03lat\x18\n \x01(\x01\x12\x0b\n\x03lon\x18\x0b \x01(\x01\x12\x0b\n\x03hae\x18\x0c \x01(\x01\x12\n\n\x02\x63\x65\x18\r \x01(\x01\x12\n\n\x02le\x18\x0e \x01(\x01\x12\x37\n\x06\x64\x65tail\x18\x0f \x01(\x0b\x32\'.atakmap.commoncommo.protobuf.v1.DetailB\x02H\x03\x62\x06proto3'
  ,
  dependencies=[detail__pb2.DESCRIPTOR,])




_COTEVENT = _descriptor.Descriptor(
  name='CotEvent',
  full_name='atakmap.commoncommo.protobuf.v1.CotEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.access', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qos', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.qos', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opex', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.opex', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.uid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendTime', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.sendTime', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.startTime', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='staleTime', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.staleTime', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='how', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.how', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lat', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.lat', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lon', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.lon', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hae', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.hae', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ce', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.ce', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='le', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.le', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='atakmap.commoncommo.protobuf.v1.CotEvent.detail', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=66,
  serialized_end=335,
)

_COTEVENT.fields_by_name['detail'].message_type = detail__pb2._DETAIL
DESCRIPTOR.message_types_by_name['CotEvent'] = _COTEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CotEvent = _reflection.GeneratedProtocolMessageType('CotEvent', (_message.Message,), {
  'DESCRIPTOR' : _COTEVENT,
  '__module__' : 'cotevent_pb2'
  # @@protoc_insertion_point(class_scope:atakmap.commoncommo.protobuf.v1.CotEvent)
  })
_sym_db.RegisterMessage(CotEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
