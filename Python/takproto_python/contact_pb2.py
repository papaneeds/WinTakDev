# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contact.proto',
  package='atakmap.commoncommo.protobuf.v1',
  syntax='proto3',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcontact.proto\x12\x1f\x61takmap.commoncommo.protobuf.v1\"-\n\x07\x43ontact\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61llsign\x18\x02 \x01(\tB\x02H\x03\x62\x06proto3'
)




_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='atakmap.commoncommo.protobuf.v1.Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='atakmap.commoncommo.protobuf.v1.Contact.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='callsign', full_name='atakmap.commoncommo.protobuf.v1.Contact.callsign', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=50,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
  'DESCRIPTOR' : _CONTACT,
  '__module__' : 'contact_pb2'
  # @@protoc_insertion_point(class_scope:atakmap.commoncommo.protobuf.v1.Contact)
  })
_sym_db.RegisterMessage(Contact)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
