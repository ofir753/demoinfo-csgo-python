# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steamdatagram_messages_auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import steamnetworkingsockets_messages_certs_pb2 as steamnetworkingsockets__messages__certs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steamdatagram_messages_auth.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n!steamdatagram_messages_auth.proto\x1a+steamnetworkingsockets_messages_certs.proto\"\x86\x04\n CMsgSteamDatagramRelayAuthTicket\x12\x13\n\x0btime_expiry\x18\x01 \x01(\x07\x12\"\n\x1a\x61uthorized_client_identity\x18\x0c \x01(\x0c\x12\x1b\n\x13gameserver_identity\x18\r \x01(\x0c\x12\x1c\n\x14\x61uthorized_public_ip\x18\x03 \x01(\x07\x12\x1a\n\x12gameserver_address\x18\x0b \x01(\x0c\x12\x0e\n\x06\x61pp_id\x18\x07 \x01(\r\x12\x14\n\x0cvirtual_port\x18\n \x01(\r\x12\x42\n\x0c\x65xtra_fields\x18\x08 \x03(\x0b\x32,.CMsgSteamDatagramRelayAuthTicket.ExtraField\x12\"\n\x1alegacy_authorized_steam_id\x18\x02 \x01(\x06\x12\"\n\x1alegacy_gameserver_steam_id\x18\x04 \x01(\x06\x12 \n\x18legacy_gameserver_net_id\x18\x05 \x01(\x06\x12 \n\x18legacy_gameserver_pop_id\x18\t \x01(\x07\x1a\\\n\nExtraField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cstring_value\x18\x02 \x01(\t\x12\x13\n\x0bint64_value\x18\x03 \x01(\x12\x12\x15\n\rfixed64_value\x18\x05 \x01(\x06\"x\n&CMsgSteamDatagramSignedRelayAuthTicket\x12\x1b\n\x13reserved_do_not_use\x18\x01 \x01(\x06\x12\x0e\n\x06key_id\x18\x02 \x01(\x06\x12\x0e\n\x06ticket\x18\x03 \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"d\n(CMsgSteamDatagramCachedCredentialsForApp\x12\x13\n\x0bprivate_key\x18\x01 \x01(\x0c\x12\x0c\n\x04\x63\x65rt\x18\x02 \x01(\x0c\x12\x15\n\rrelay_tickets\x18\x03 \x03(\x0c\"\x88\x01\n+CMsgSteamDatagramGameCoordinatorServerLogin\x12\x16\n\x0etime_generated\x18\x01 \x01(\r\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x0f\n\x07routing\x18\x03 \x01(\x0c\x12\x0f\n\x07\x61ppdata\x18\x04 \x01(\x0c\x12\x10\n\x08identity\x18\x05 \x01(\x0c\"\x88\x01\n1CMsgSteamDatagramSignedGameCoordinatorServerLogin\x12\x31\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\r\n\x05login\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"q\n-CMsgSteamDatagramHostedServerAddressPlaintext\x12\x0c\n\x04ipv4\x18\x01 \x01(\x07\x12\x0c\n\x04ipv6\x18\x02 \x01(\x0c\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x16\n\x0erouting_secret\x18\x04 \x01(\x06\x42\x05H\x01\x80\x01\x00')
  ,
  dependencies=[steamnetworkingsockets__messages__certs__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD = _descriptor.Descriptor(
  name='ExtraField',
  full_name='CMsgSteamDatagramRelayAuthTicket.ExtraField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CMsgSteamDatagramRelayAuthTicket.ExtraField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='CMsgSteamDatagramRelayAuthTicket.ExtraField.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='CMsgSteamDatagramRelayAuthTicket.ExtraField.int64_value', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed64_value', full_name='CMsgSteamDatagramRelayAuthTicket.ExtraField.fixed64_value', index=3,
      number=5, type=6, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=601,
)

_CMSGSTEAMDATAGRAMRELAYAUTHTICKET = _descriptor.Descriptor(
  name='CMsgSteamDatagramRelayAuthTicket',
  full_name='CMsgSteamDatagramRelayAuthTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_expiry', full_name='CMsgSteamDatagramRelayAuthTicket.time_expiry', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authorized_client_identity', full_name='CMsgSteamDatagramRelayAuthTicket.authorized_client_identity', index=1,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gameserver_identity', full_name='CMsgSteamDatagramRelayAuthTicket.gameserver_identity', index=2,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authorized_public_ip', full_name='CMsgSteamDatagramRelayAuthTicket.authorized_public_ip', index=3,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gameserver_address', full_name='CMsgSteamDatagramRelayAuthTicket.gameserver_address', index=4,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='CMsgSteamDatagramRelayAuthTicket.app_id', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_port', full_name='CMsgSteamDatagramRelayAuthTicket.virtual_port', index=6,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra_fields', full_name='CMsgSteamDatagramRelayAuthTicket.extra_fields', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_authorized_steam_id', full_name='CMsgSteamDatagramRelayAuthTicket.legacy_authorized_steam_id', index=8,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_gameserver_steam_id', full_name='CMsgSteamDatagramRelayAuthTicket.legacy_gameserver_steam_id', index=9,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_gameserver_net_id', full_name='CMsgSteamDatagramRelayAuthTicket.legacy_gameserver_net_id', index=10,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_gameserver_pop_id', full_name='CMsgSteamDatagramRelayAuthTicket.legacy_gameserver_pop_id', index=11,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=601,
)


_CMSGSTEAMDATAGRAMSIGNEDRELAYAUTHTICKET = _descriptor.Descriptor(
  name='CMsgSteamDatagramSignedRelayAuthTicket',
  full_name='CMsgSteamDatagramSignedRelayAuthTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reserved_do_not_use', full_name='CMsgSteamDatagramSignedRelayAuthTicket.reserved_do_not_use', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='CMsgSteamDatagramSignedRelayAuthTicket.key_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticket', full_name='CMsgSteamDatagramSignedRelayAuthTicket.ticket', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='CMsgSteamDatagramSignedRelayAuthTicket.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=723,
)


_CMSGSTEAMDATAGRAMCACHEDCREDENTIALSFORAPP = _descriptor.Descriptor(
  name='CMsgSteamDatagramCachedCredentialsForApp',
  full_name='CMsgSteamDatagramCachedCredentialsForApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='private_key', full_name='CMsgSteamDatagramCachedCredentialsForApp.private_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cert', full_name='CMsgSteamDatagramCachedCredentialsForApp.cert', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relay_tickets', full_name='CMsgSteamDatagramCachedCredentialsForApp.relay_tickets', index=2,
      number=3, type=12, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=825,
)


_CMSGSTEAMDATAGRAMGAMECOORDINATORSERVERLOGIN = _descriptor.Descriptor(
  name='CMsgSteamDatagramGameCoordinatorServerLogin',
  full_name='CMsgSteamDatagramGameCoordinatorServerLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_generated', full_name='CMsgSteamDatagramGameCoordinatorServerLogin.time_generated', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appid', full_name='CMsgSteamDatagramGameCoordinatorServerLogin.appid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='routing', full_name='CMsgSteamDatagramGameCoordinatorServerLogin.routing', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appdata', full_name='CMsgSteamDatagramGameCoordinatorServerLogin.appdata', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identity', full_name='CMsgSteamDatagramGameCoordinatorServerLogin.identity', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=964,
)


_CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN = _descriptor.Descriptor(
  name='CMsgSteamDatagramSignedGameCoordinatorServerLogin',
  full_name='CMsgSteamDatagramSignedGameCoordinatorServerLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cert', full_name='CMsgSteamDatagramSignedGameCoordinatorServerLogin.cert', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login', full_name='CMsgSteamDatagramSignedGameCoordinatorServerLogin.login', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='CMsgSteamDatagramSignedGameCoordinatorServerLogin.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=967,
  serialized_end=1103,
)


_CMSGSTEAMDATAGRAMHOSTEDSERVERADDRESSPLAINTEXT = _descriptor.Descriptor(
  name='CMsgSteamDatagramHostedServerAddressPlaintext',
  full_name='CMsgSteamDatagramHostedServerAddressPlaintext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='CMsgSteamDatagramHostedServerAddressPlaintext.ipv4', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='CMsgSteamDatagramHostedServerAddressPlaintext.ipv6', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='CMsgSteamDatagramHostedServerAddressPlaintext.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='routing_secret', full_name='CMsgSteamDatagramHostedServerAddressPlaintext.routing_secret', index=3,
      number=4, type=6, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1105,
  serialized_end=1218,
)

_CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD.containing_type = _CMSGSTEAMDATAGRAMRELAYAUTHTICKET
_CMSGSTEAMDATAGRAMRELAYAUTHTICKET.fields_by_name['extra_fields'].message_type = _CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD
_CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN.fields_by_name['cert'].message_type = steamnetworkingsockets__messages__certs__pb2._CMSGSTEAMDATAGRAMCERTIFICATESIGNED
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramRelayAuthTicket'] = _CMSGSTEAMDATAGRAMRELAYAUTHTICKET
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramSignedRelayAuthTicket'] = _CMSGSTEAMDATAGRAMSIGNEDRELAYAUTHTICKET
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramCachedCredentialsForApp'] = _CMSGSTEAMDATAGRAMCACHEDCREDENTIALSFORAPP
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramGameCoordinatorServerLogin'] = _CMSGSTEAMDATAGRAMGAMECOORDINATORSERVERLOGIN
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramSignedGameCoordinatorServerLogin'] = _CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramHostedServerAddressPlaintext'] = _CMSGSTEAMDATAGRAMHOSTEDSERVERADDRESSPLAINTEXT

CMsgSteamDatagramRelayAuthTicket = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramRelayAuthTicket', (_message.Message,), dict(

  ExtraField = _reflection.GeneratedProtocolMessageType('ExtraField', (_message.Message,), dict(
    DESCRIPTOR = _CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD,
    __module__ = 'steamdatagram_messages_auth_pb2'
    # @@protoc_insertion_point(class_scope:CMsgSteamDatagramRelayAuthTicket.ExtraField)
    ))
  ,
  DESCRIPTOR = _CMSGSTEAMDATAGRAMRELAYAUTHTICKET,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramRelayAuthTicket)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramRelayAuthTicket)
_sym_db.RegisterMessage(CMsgSteamDatagramRelayAuthTicket.ExtraField)

CMsgSteamDatagramSignedRelayAuthTicket = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramSignedRelayAuthTicket', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMSIGNEDRELAYAUTHTICKET,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramSignedRelayAuthTicket)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramSignedRelayAuthTicket)

CMsgSteamDatagramCachedCredentialsForApp = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramCachedCredentialsForApp', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMCACHEDCREDENTIALSFORAPP,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramCachedCredentialsForApp)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramCachedCredentialsForApp)

CMsgSteamDatagramGameCoordinatorServerLogin = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramGameCoordinatorServerLogin', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMGAMECOORDINATORSERVERLOGIN,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramGameCoordinatorServerLogin)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramGameCoordinatorServerLogin)

CMsgSteamDatagramSignedGameCoordinatorServerLogin = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramSignedGameCoordinatorServerLogin', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramSignedGameCoordinatorServerLogin)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramSignedGameCoordinatorServerLogin)

CMsgSteamDatagramHostedServerAddressPlaintext = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramHostedServerAddressPlaintext', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMHOSTEDSERVERADDRESSPLAINTEXT,
  __module__ = 'steamdatagram_messages_auth_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramHostedServerAddressPlaintext)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramHostedServerAddressPlaintext)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001\200\001\000'))
# @@protoc_insertion_point(module_scope)
