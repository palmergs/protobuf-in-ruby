# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

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
  name='messages.proto',
  package='bmore',
  syntax='proto3',
  serialized_pb=_b('\n\x0emessages.proto\x12\x05\x62more\"\x90\x01\n\x08\x41\x63tivity\x12\x0f\n\x07sent_at\x18\x01 \x01(\x03\x12\x16\n\x0emessage_number\x18\x02 \x01(\x05\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12%\n\x07request\x18\x04 \x01(\x0b\x32\x12.bmore.HttpRequestH\x00\x12\x1b\n\x04\x63hat\x18\x05 \x01(\x0b\x32\x0b.bmore.ChatH\x00\x42\x07\n\x05\x65vent\"\x1c\n\x08\x46irewall\x12\x10\n\x08\x62lock_it\x18\x01 \x01(\x08\";\n\x0c\x43onversation\x12\x0f\n\x07sent_at\x18\x01 \x01(\x03\x12\x1a\n\x05\x63hats\x18\x02 \x03(\x0b\x32\x0b.bmore.Chat\"\xda\x02\n\x0bHttpRequest\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x16\n\x0erequest_method\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\x12\x0e\n\x06script\x18\x07 \x01(\t\x12\x0c\n\x04path\x18\x08 \x01(\t\x12\x36\n\nparameters\x18\t \x03(\x0b\x32\".bmore.HttpRequest.ParametersEntry\x12\x30\n\x07headers\x18\n \x03(\x0b\x32\x1f.bmore.HttpRequest.HeadersEntry\x1a\x42\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.bmore.KeyValue:\x02\x38\x01\x1a?\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.bmore.KeyValue:\x02\x38\x01\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\xf8\x01\n\x04\x43hat\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x12&\n\x08priority\x18\x05 \x01(\x0e\x32\x14.bmore.Chat.Priority\x12-\n\x0c\x63ontent_type\x18\x06 \x01(\x0e\x32\x17.bmore.Chat.ContentType\")\n\x08Priority\x12\x07\n\x03LOW\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\x08\n\x04HIGH\x10\x02\"/\n\x0b\x43ontentType\x12\x08\n\x04TEXT\x10\x00\x12\x08\n\x04HTML\x10\x01\x12\x0c\n\x08MARKDOWN\x10\x02\x62\x06proto3')
)



_CHAT_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='bmore.Chat.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=811,
  serialized_end=852,
)
_sym_db.RegisterEnumDescriptor(_CHAT_PRIORITY)

_CHAT_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='bmore.Chat.ContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKDOWN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=854,
  serialized_end=901,
)
_sym_db.RegisterEnumDescriptor(_CHAT_CONTENTTYPE)


_ACTIVITY = _descriptor.Descriptor(
  name='Activity',
  full_name='bmore.Activity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sent_at', full_name='bmore.Activity.sent_at', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_number', full_name='bmore.Activity.message_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='bmore.Activity.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='bmore.Activity.request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chat', full_name='bmore.Activity.chat', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='event', full_name='bmore.Activity.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=26,
  serialized_end=170,
)


_FIREWALL = _descriptor.Descriptor(
  name='Firewall',
  full_name='bmore.Firewall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_it', full_name='bmore.Firewall.block_it', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=172,
  serialized_end=200,
)


_CONVERSATION = _descriptor.Descriptor(
  name='Conversation',
  full_name='bmore.Conversation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sent_at', full_name='bmore.Conversation.sent_at', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chats', full_name='bmore.Conversation.chats', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=202,
  serialized_end=261,
)


_HTTPREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='bmore.HttpRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmore.HttpRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmore.HttpRequest.ParametersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=545,
)

_HTTPREQUEST_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='bmore.HttpRequest.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmore.HttpRequest.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmore.HttpRequest.HeadersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=610,
)

_HTTPREQUEST = _descriptor.Descriptor(
  name='HttpRequest',
  full_name='bmore.HttpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='bmore.HttpRequest.ip', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_method', full_name='bmore.HttpRequest.request_method', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bmore.HttpRequest.host', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='bmore.HttpRequest.port', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script', full_name='bmore.HttpRequest.script', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='bmore.HttpRequest.path', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='bmore.HttpRequest.parameters', index=6,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='headers', full_name='bmore.HttpRequest.headers', index=7,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HTTPREQUEST_PARAMETERSENTRY, _HTTPREQUEST_HEADERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=610,
)


_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='bmore.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmore.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmore.KeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=612,
  serialized_end=650,
)


_CHAT = _descriptor.Descriptor(
  name='Chat',
  full_name='bmore.Chat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='bmore.Chat.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='bmore.Chat.receiver', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='bmore.Chat.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='bmore.Chat.count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='bmore.Chat.priority', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='bmore.Chat.content_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAT_PRIORITY,
    _CHAT_CONTENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=901,
)

_ACTIVITY.fields_by_name['request'].message_type = _HTTPREQUEST
_ACTIVITY.fields_by_name['chat'].message_type = _CHAT
_ACTIVITY.oneofs_by_name['event'].fields.append(
  _ACTIVITY.fields_by_name['request'])
_ACTIVITY.fields_by_name['request'].containing_oneof = _ACTIVITY.oneofs_by_name['event']
_ACTIVITY.oneofs_by_name['event'].fields.append(
  _ACTIVITY.fields_by_name['chat'])
_ACTIVITY.fields_by_name['chat'].containing_oneof = _ACTIVITY.oneofs_by_name['event']
_CONVERSATION.fields_by_name['chats'].message_type = _CHAT
_HTTPREQUEST_PARAMETERSENTRY.fields_by_name['value'].message_type = _KEYVALUE
_HTTPREQUEST_PARAMETERSENTRY.containing_type = _HTTPREQUEST
_HTTPREQUEST_HEADERSENTRY.fields_by_name['value'].message_type = _KEYVALUE
_HTTPREQUEST_HEADERSENTRY.containing_type = _HTTPREQUEST
_HTTPREQUEST.fields_by_name['parameters'].message_type = _HTTPREQUEST_PARAMETERSENTRY
_HTTPREQUEST.fields_by_name['headers'].message_type = _HTTPREQUEST_HEADERSENTRY
_CHAT.fields_by_name['priority'].enum_type = _CHAT_PRIORITY
_CHAT.fields_by_name['content_type'].enum_type = _CHAT_CONTENTTYPE
_CHAT_PRIORITY.containing_type = _CHAT
_CHAT_CONTENTTYPE.containing_type = _CHAT
DESCRIPTOR.message_types_by_name['Activity'] = _ACTIVITY
DESCRIPTOR.message_types_by_name['Firewall'] = _FIREWALL
DESCRIPTOR.message_types_by_name['Conversation'] = _CONVERSATION
DESCRIPTOR.message_types_by_name['HttpRequest'] = _HTTPREQUEST
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Chat'] = _CHAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Activity = _reflection.GeneratedProtocolMessageType('Activity', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVITY,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.Activity)
  ))
_sym_db.RegisterMessage(Activity)

Firewall = _reflection.GeneratedProtocolMessageType('Firewall', (_message.Message,), dict(
  DESCRIPTOR = _FIREWALL,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.Firewall)
  ))
_sym_db.RegisterMessage(Firewall)

Conversation = _reflection.GeneratedProtocolMessageType('Conversation', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSATION,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.Conversation)
  ))
_sym_db.RegisterMessage(Conversation)

HttpRequest = _reflection.GeneratedProtocolMessageType('HttpRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _HTTPREQUEST_PARAMETERSENTRY,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:bmore.HttpRequest.ParametersEntry)
    ))
  ,

  HeadersEntry = _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), dict(
    DESCRIPTOR = _HTTPREQUEST_HEADERSENTRY,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:bmore.HttpRequest.HeadersEntry)
    ))
  ,
  DESCRIPTOR = _HTTPREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.HttpRequest)
  ))
_sym_db.RegisterMessage(HttpRequest)
_sym_db.RegisterMessage(HttpRequest.ParametersEntry)
_sym_db.RegisterMessage(HttpRequest.HeadersEntry)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

Chat = _reflection.GeneratedProtocolMessageType('Chat', (_message.Message,), dict(
  DESCRIPTOR = _CHAT,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:bmore.Chat)
  ))
_sym_db.RegisterMessage(Chat)


_HTTPREQUEST_PARAMETERSENTRY.has_options = True
_HTTPREQUEST_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_HTTPREQUEST_HEADERSENTRY.has_options = True
_HTTPREQUEST_HEADERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
