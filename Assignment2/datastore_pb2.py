# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datastore.proto

import sys

#import channel as channel

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='datastore.proto',
  package='',
  syntax='proto3',
  #serialized_pb=_b('\n\x0f\x64\x61tastore.proto\"\x17\n\x07Request\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x18\n\x08Response\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2G\n\tDatastore\x12\x1c\n\x03put\x12\x08.Request\x1a\t.Response\"\x00\x12\x1c\n\x03get\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')
  serialized_pb=_b('\n\x0f\x64\x61tastore.proto\"$\n\x07Request\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x18\n\x08Response\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\r\n\x0bReplicatorRequest\"6\n\rReplicatorResponse\x12\n\n\x02rp\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t2\x93\x01\n\nDatastore\x12(\n\x04sync\x12\x0c.ReplicatorRequest\x1a\x0e.ReplicatorResponse\"\x00\x30\x01\x12\x1c\n\x03put\x12\x08.Request\x1a\t.Response\"\x00\x12\x1f\n\x06\x64\x65lete\x12\x08.Request\x1a\t.Response\"\x00\x12\x1c\n\x03get\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Request.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
      _descriptor.FieldDescriptor(
          name='data', full_name='Request.data', index=1,
          number=2, type=9, cpp_type=9, label=1,
          has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=62,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Response.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=63,
  serialized_end=89,
)

_REPLICATORREQUEST = _descriptor.Descriptor(
  name='ReplicatorRequest',
  full_name='ReplicatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=93,
  serialized_end=112,
)

_REPLICATORRESPONSE = _descriptor.Descriptor(
  name='ReplicatorResponse',
  full_name='ReplicatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rp', full_name='ReplicatorResponse.rp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicatorResponse.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='ReplicatorResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=116,
  serialized_end=156,
)


DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ReplicatorRequest'] = _REPLICATORREQUEST
DESCRIPTOR.message_types_by_name['ReplicatorResponse'] = _REPLICATORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

ReplicatorRequest = _reflection.GeneratedProtocolMessageType('ReplicatorRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPLICATORREQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

ReplicatorResponse = _reflection.GeneratedProtocolMessageType('ReplicatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLICATORRESPONSE,
  __module__ = 'datastore_pb2'
# @@protoc_insertion_point(class_scope:SyncOperation)
  ))
_sym_db.RegisterMessage(ReplicatorResponse)



_DATASTORE = _descriptor.ServiceDescriptor(
  name='Datastore',
  full_name='Datastore',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=168,
  serialized_end=346,
  methods=[
  _descriptor.MethodDescriptor(
    name='sync',
    full_name='Datastore.sync',
    index=0,
    containing_service=None,
    input_type=_REPLICATORREQUEST,
    output_type=_REPLICATORRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='put',
    full_name='Replicator.put',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='Datastore.delete',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='Datastore.get',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASTORE)

DESCRIPTOR.services_by_name['Datastore'] = _DATASTORE



try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DatastoreStub(object):
    # missing associated documentation comment in .proto file
    pass
    def __init__(self, channel):

        self.sync = channel.unary_stream(
        '/Datastore/sync',
        request_serializer=ReplicatorRequest.SerializeToString,
        response_deserializer=ReplicatorResponse.FromString,
        )
        self.put = channel.unary_unary(
        '/Datastore/put',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response.FromString,
        )
        self.delete = channel.unary_unary(
        '/Datastore/delete',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response.FromString,
        )
        self.get = channel.unary_unary(
        '/Datastore/get',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response.FromString,
        )

    class DatastoreServicer(object):
        # missing associated documentation comment in .proto file
        pass

        def put(self, request, context):
            # missing associated documentation comment in .proto file
            pass
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def sync(self, request, context):
            # missing associated documentation comment in .proto file
            pass
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def delete(self, request, context):
            """Operations on the db
            """
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def get(self, request, context):
            # missing associated documentation comment in .proto file
            pass
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

    def add_DatastoreServicer_to_server(servicer, server):
        rpc_method_handlers = {
            'put': grpc.unary_unary_rpc_method_handler(
                servicer.put,
                request_deserializer=Request.FromString,
                response_serializer=Response.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                servicer.get,
                request_deserializer=Request.FromString,
                response_serializer=Response.SerializeToString,
            ),
            'sync': grpc.unary_stream_rpc_method_handler(
                servicer.sync,
                request_deserializer=ReplicatorRequest.FromString,
                response_serializer=ReplicatorResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                servicer.delete,
                request_deserializer=Request.FromString,
                response_serializer=Response.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            'Datastore', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


  class BetaDatastoreServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.
    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def sync(self, request, context):
        pass
        context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

    def delete(self, request, context):
        pass
        context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

  class BetaDatastoreStub(object):
    """The Beta API is deprecated for 0.15.0 and later.
    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    put.future = None
    def get(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    get.future = None
    def sync(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
        # missing associated documentation comment in .proto file
        pass
        raise NotImplementedError()
    def delete(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
        # missing associated documentation comment in .proto file
        pass
        raise NotImplementedError()
    delete.future = None


  def beta_create_Datastore_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.
    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Datastore', 'get'): Request.FromString,
      ('Datastore', 'put'): Request.FromString,
      ('Datastore', 'sync'): Request.FromString,
      ('Datastore', 'delete'): Request.FromString,
    }
    response_serializers = {
      ('Datastore', 'get'): Response.SerializeToString,
      ('Datastore', 'put'): Response.SerializeToString,
      ('Datastore', 'sync'): Response.SerializeToString,
      ('Datastore', 'delete'): Response.SerializeToString,
    }
    method_implementations = {
      ('Datastore', 'get'): face_utilities.unary_unary_inline(servicer.get),
      ('Datastore', 'put'): face_utilities.unary_unary_inline(servicer.put),
      ('Datastore', 'sync'): face_utilities.unary_unary_inline(servicer.sync),
      ('Datastore', 'delete'): face_utilities.unary_unary_inline(servicer.delete),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Datastore_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.
    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Datastore', 'get'): Request.SerializeToString,
      ('Datastore', 'put'): Request.SerializeToString,
      ('Datastore', 'sync'): Request.SerializeToString,
      ('Datastore', 'delete'): Request.SerializeToString,
    }
    response_deserializers = {
      ('Datastore', 'get'): Response.FromString,
      ('Datastore', 'put'): Response.FromString,
      ('Datastore', 'sync'): Response.FromString,
      ('Datastore', 'delete'): Response.FromString,
    }
    cardinalities = {
      'get': cardinality.Cardinality.UNARY_UNARY,
      'put': cardinality.Cardinality.UNARY_UNARY,
      'sync': cardinality.Cardinality.UNARY_UNARY,
      'delete': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Datastore', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
