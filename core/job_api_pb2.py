# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_api.proto',
  package='fedscale',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rjob_api.proto\x12\x08\x66\x65\x64scale\"/\n\x12UpdateModelRequest\x12\x19\n\x11serialized_tensor\x18\x01 \x01(\x0c\"&\n\x13UpdateModelResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x0cTrainRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x04\x12\x1f\n\x17serialized_train_config\x18\x02 \x01(\x0c\"2\n\rTrainResponse\x12!\n\x19serialized_train_response\x18\x01 \x01(\x0c\"!\n\x0c\x46\x65tchRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x04\"2\n\rFetchResponse\x12!\n\x19serialized_fetch_response\x18\x01 \x01(\x0c\"\r\n\x0bStopRequest\"\x0e\n\x0cStopResponse\"\x1b\n\x19ReportExecutorInfoRequest\"7\n\x1aReportExecutorInfoResponse\x12\x19\n\x11training_set_size\x18\x01 \x03(\x03\"\x1e\n\x0bTestRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"0\n\x0cTestResponse\x12 \n\x18serialized_test_response\x18\x01 \x01(\x0c\x32\xa7\x03\n\nJobService\x12L\n\x0bUpdateModel\x12\x1c.fedscale.UpdateModelRequest\x1a\x1d.fedscale.UpdateModelResponse\"\x00\x12:\n\x05Train\x12\x16.fedscale.TrainRequest\x1a\x17.fedscale.TrainResponse\"\x00\x12:\n\x05\x46\x65tch\x12\x16.fedscale.FetchRequest\x1a\x17.fedscale.FetchResponse\"\x00\x12\x37\n\x04Stop\x12\x15.fedscale.StopRequest\x1a\x16.fedscale.StopResponse\"\x00\x12\x61\n\x12ReportExecutorInfo\x12#.fedscale.ReportExecutorInfoRequest\x1a$.fedscale.ReportExecutorInfoResponse\"\x00\x12\x37\n\x04Test\x12\x15.fedscale.TestRequest\x1a\x16.fedscale.TestResponse\"\x00\x62\x06proto3'
)




_UPDATEMODELREQUEST = _descriptor.Descriptor(
  name='UpdateModelRequest',
  full_name='fedscale.UpdateModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_tensor', full_name='fedscale.UpdateModelRequest.serialized_tensor', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=27,
  serialized_end=74,
)


_UPDATEMODELRESPONSE = _descriptor.Descriptor(
  name='UpdateModelResponse',
  full_name='fedscale.UpdateModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='fedscale.UpdateModelResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=76,
  serialized_end=114,
)


_TRAINREQUEST = _descriptor.Descriptor(
  name='TrainRequest',
  full_name='fedscale.TrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='fedscale.TrainRequest.client_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialized_train_config', full_name='fedscale.TrainRequest.serialized_train_config', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=116,
  serialized_end=182,
)


_TRAINRESPONSE = _descriptor.Descriptor(
  name='TrainResponse',
  full_name='fedscale.TrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_train_response', full_name='fedscale.TrainResponse.serialized_train_response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=184,
  serialized_end=234,
)


_FETCHREQUEST = _descriptor.Descriptor(
  name='FetchRequest',
  full_name='fedscale.FetchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='fedscale.FetchRequest.client_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=236,
  serialized_end=269,
)


_FETCHRESPONSE = _descriptor.Descriptor(
  name='FetchResponse',
  full_name='fedscale.FetchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_fetch_response', full_name='fedscale.FetchResponse.serialized_fetch_response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=271,
  serialized_end=321,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='fedscale.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=323,
  serialized_end=336,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='fedscale.StopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=338,
  serialized_end=352,
)


_REPORTEXECUTORINFOREQUEST = _descriptor.Descriptor(
  name='ReportExecutorInfoRequest',
  full_name='fedscale.ReportExecutorInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=354,
  serialized_end=381,
)


_REPORTEXECUTORINFORESPONSE = _descriptor.Descriptor(
  name='ReportExecutorInfoResponse',
  full_name='fedscale.ReportExecutorInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='training_set_size', full_name='fedscale.ReportExecutorInfoResponse.training_set_size', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=383,
  serialized_end=438,
)


_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='fedscale.TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='fedscale.TestRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=440,
  serialized_end=470,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='fedscale.TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_test_response', full_name='fedscale.TestResponse.serialized_test_response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=472,
  serialized_end=520,
)

DESCRIPTOR.message_types_by_name['UpdateModelRequest'] = _UPDATEMODELREQUEST
DESCRIPTOR.message_types_by_name['UpdateModelResponse'] = _UPDATEMODELRESPONSE
DESCRIPTOR.message_types_by_name['TrainRequest'] = _TRAINREQUEST
DESCRIPTOR.message_types_by_name['TrainResponse'] = _TRAINRESPONSE
DESCRIPTOR.message_types_by_name['FetchRequest'] = _FETCHREQUEST
DESCRIPTOR.message_types_by_name['FetchResponse'] = _FETCHRESPONSE
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
DESCRIPTOR.message_types_by_name['ReportExecutorInfoRequest'] = _REPORTEXECUTORINFOREQUEST
DESCRIPTOR.message_types_by_name['ReportExecutorInfoResponse'] = _REPORTEXECUTORINFORESPONSE
DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateModelRequest = _reflection.GeneratedProtocolMessageType('UpdateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.UpdateModelRequest)
  })
_sym_db.RegisterMessage(UpdateModelRequest)

UpdateModelResponse = _reflection.GeneratedProtocolMessageType('UpdateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELRESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.UpdateModelResponse)
  })
_sym_db.RegisterMessage(UpdateModelResponse)

TrainRequest = _reflection.GeneratedProtocolMessageType('TrainRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.TrainRequest)
  })
_sym_db.RegisterMessage(TrainRequest)

TrainResponse = _reflection.GeneratedProtocolMessageType('TrainResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINRESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.TrainResponse)
  })
_sym_db.RegisterMessage(TrainResponse)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.FetchRequest)
  })
_sym_db.RegisterMessage(FetchRequest)

FetchResponse = _reflection.GeneratedProtocolMessageType('FetchResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHRESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.FetchResponse)
  })
_sym_db.RegisterMessage(FetchResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)

ReportExecutorInfoRequest = _reflection.GeneratedProtocolMessageType('ReportExecutorInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEXECUTORINFOREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.ReportExecutorInfoRequest)
  })
_sym_db.RegisterMessage(ReportExecutorInfoRequest)

ReportExecutorInfoResponse = _reflection.GeneratedProtocolMessageType('ReportExecutorInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTEXECUTORINFORESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.ReportExecutorInfoResponse)
  })
_sym_db.RegisterMessage(ReportExecutorInfoResponse)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'job_api_pb2'
  # @@protoc_insertion_point(class_scope:fedscale.TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)



_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='fedscale.JobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=523,
  serialized_end=946,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateModel',
    full_name='fedscale.JobService.UpdateModel',
    index=0,
    containing_service=None,
    input_type=_UPDATEMODELREQUEST,
    output_type=_UPDATEMODELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Train',
    full_name='fedscale.JobService.Train',
    index=1,
    containing_service=None,
    input_type=_TRAINREQUEST,
    output_type=_TRAINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Fetch',
    full_name='fedscale.JobService.Fetch',
    index=2,
    containing_service=None,
    input_type=_FETCHREQUEST,
    output_type=_FETCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='fedscale.JobService.Stop',
    index=3,
    containing_service=None,
    input_type=_STOPREQUEST,
    output_type=_STOPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportExecutorInfo',
    full_name='fedscale.JobService.ReportExecutorInfo',
    index=4,
    containing_service=None,
    input_type=_REPORTEXECUTORINFOREQUEST,
    output_type=_REPORTEXECUTORINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='fedscale.JobService.Test',
    index=5,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE

# @@protoc_insertion_point(module_scope)
