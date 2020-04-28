# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steamnetworkingsockets_messages_udp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import steamnetworkingsockets_messages_certs_pb2 as steamnetworkingsockets__messages__certs__pb2
from . import steamnetworkingsockets_messages_pb2 as steamnetworkingsockets__messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steamnetworkingsockets_messages_udp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n)steamnetworkingsockets_messages_udp.proto\x1a+steamnetworkingsockets_messages_certs.proto\x1a%steamnetworkingsockets_messages.proto\"n\n%CMsgSteamSockets_UDP_ChallengeRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x14\n\x0cmy_timestamp\x18\x03 \x01(\x06\x12\x18\n\x10protocol_version\x18\x04 \x01(\r\"\x81\x01\n#CMsgSteamSockets_UDP_ChallengeReply\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x11\n\tchallenge\x18\x02 \x01(\x06\x12\x16\n\x0eyour_timestamp\x18\x03 \x01(\x06\x12\x18\n\x10protocol_version\x18\x04 \x01(\r\"\xde\x02\n#CMsgSteamSockets_UDP_ConnectRequest\x12\x1c\n\x14\x63lient_connection_id\x18\x01 \x01(\x07\x12\x11\n\tchallenge\x18\x02 \x01(\x06\x12\x14\n\x0cmy_timestamp\x18\x05 \x01(\x06\x12\x13\n\x0bping_est_ms\x18\x06 \x01(\r\x12\x37\n\x05\x63rypt\x18\x07 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x04 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x1f\n\x17legacy_protocol_version\x18\x08 \x01(\r\x12.\n\x08identity\x18\t \x01(\x0b\x32\x1c.CMsgSteamNetworkingIdentity\x12\x1e\n\x16legacy_client_steam_id\x18\x03 \x01(\x06\"\xc9\x02\n\x1e\x43MsgSteamSockets_UDP_ConnectOK\x12\x1c\n\x14\x63lient_connection_id\x18\x01 \x01(\x07\x12\x1c\n\x14server_connection_id\x18\x05 \x01(\x07\x12\x16\n\x0eyour_timestamp\x18\x03 \x01(\x06\x12\x17\n\x0f\x64\x65lay_time_usec\x18\x04 \x01(\r\x12\x37\n\x05\x63rypt\x18\x07 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x08 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12.\n\x08identity\x18\n \x01(\x0b\x32\x1c.CMsgSteamNetworkingIdentity\x12\x1e\n\x16legacy_server_steam_id\x18\x02 \x01(\x06\"\x81\x01\n%CMsgSteamSockets_UDP_ConnectionClosed\x12\x18\n\x10to_connection_id\x18\x04 \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\x05 \x01(\x07\x12\r\n\x05\x64\x65\x62ug\x18\x02 \x01(\t\x12\x13\n\x0breason_code\x18\x03 \x01(\r\"Y\n!CMsgSteamSockets_UDP_NoConnection\x12\x1a\n\x12\x66rom_connection_id\x18\x02 \x01(\x07\x12\x18\n\x10to_connection_id\x18\x03 \x01(\x07\"\xdf\x01\n\x1a\x43MsgSteamSockets_UDP_Stats\x12\x32\n\x05stats\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x18\n\x10to_connection_id\x18\t \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\n \x01(\x07\x12\x0f\n\x07seq_num\x18\x04 \x01(\r\"7\n\x05\x46lags\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04*\xa5\x02\n\x18\x45SteamNetworkingUDPMsgID\x12-\n)k_ESteamNetworkingUDPMsg_ChallengeRequest\x10 \x12+\n\'k_ESteamNetworkingUDPMsg_ChallengeReply\x10!\x12+\n\'k_ESteamNetworkingUDPMsg_ConnectRequest\x10\"\x12&\n\"k_ESteamNetworkingUDPMsg_ConnectOK\x10#\x12-\n)k_ESteamNetworkingUDPMsg_ConnectionClosed\x10$\x12)\n%k_ESteamNetworkingUDPMsg_NoConnection\x10%B\x05H\x01\x80\x01\x00')
  ,
  dependencies=[steamnetworkingsockets__messages__certs__pb2.DESCRIPTOR,steamnetworkingsockets__messages__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ESTEAMNETWORKINGUDPMSGID = _descriptor.EnumDescriptor(
  name='ESteamNetworkingUDPMsgID',
  full_name='ESteamNetworkingUDPMsgID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_ChallengeRequest', index=0, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_ChallengeReply', index=1, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_ConnectRequest', index=2, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_ConnectOK', index=3, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_ConnectionClosed', index=4, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ESteamNetworkingUDPMsg_NoConnection', index=5, number=37,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1508,
  serialized_end=1801,
)
_sym_db.RegisterEnumDescriptor(_ESTEAMNETWORKINGUDPMSGID)

ESteamNetworkingUDPMsgID = enum_type_wrapper.EnumTypeWrapper(_ESTEAMNETWORKINGUDPMSGID)
k_ESteamNetworkingUDPMsg_ChallengeRequest = 32
k_ESteamNetworkingUDPMsg_ChallengeReply = 33
k_ESteamNetworkingUDPMsg_ConnectRequest = 34
k_ESteamNetworkingUDPMsg_ConnectOK = 35
k_ESteamNetworkingUDPMsg_ConnectionClosed = 36
k_ESteamNetworkingUDPMsg_NoConnection = 37


_CMSGSTEAMSOCKETS_UDP_STATS_FLAGS = _descriptor.EnumDescriptor(
  name='Flags',
  full_name='CMsgSteamSockets_UDP_Stats.Flags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACK_REQUEST_E2E', index=0, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACK_REQUEST_IMMEDIATE', index=1, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1450,
  serialized_end=1505,
)
_sym_db.RegisterEnumDescriptor(_CMSGSTEAMSOCKETS_UDP_STATS_FLAGS)


_CMSGSTEAMSOCKETS_UDP_CHALLENGEREQUEST = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_ChallengeRequest',
  full_name='CMsgSteamSockets_UDP_ChallengeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='CMsgSteamSockets_UDP_ChallengeRequest.connection_id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_timestamp', full_name='CMsgSteamSockets_UDP_ChallengeRequest.my_timestamp', index=1,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='CMsgSteamSockets_UDP_ChallengeRequest.protocol_version', index=2,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=129,
  serialized_end=239,
)


_CMSGSTEAMSOCKETS_UDP_CHALLENGEREPLY = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_ChallengeReply',
  full_name='CMsgSteamSockets_UDP_ChallengeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='CMsgSteamSockets_UDP_ChallengeReply.connection_id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='challenge', full_name='CMsgSteamSockets_UDP_ChallengeReply.challenge', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='your_timestamp', full_name='CMsgSteamSockets_UDP_ChallengeReply.your_timestamp', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='CMsgSteamSockets_UDP_ChallengeReply.protocol_version', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=242,
  serialized_end=371,
)


_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_ConnectRequest',
  full_name='CMsgSteamSockets_UDP_ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_connection_id', full_name='CMsgSteamSockets_UDP_ConnectRequest.client_connection_id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='challenge', full_name='CMsgSteamSockets_UDP_ConnectRequest.challenge', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_timestamp', full_name='CMsgSteamSockets_UDP_ConnectRequest.my_timestamp', index=2,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping_est_ms', full_name='CMsgSteamSockets_UDP_ConnectRequest.ping_est_ms', index=3,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypt', full_name='CMsgSteamSockets_UDP_ConnectRequest.crypt', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cert', full_name='CMsgSteamSockets_UDP_ConnectRequest.cert', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_protocol_version', full_name='CMsgSteamSockets_UDP_ConnectRequest.legacy_protocol_version', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identity', full_name='CMsgSteamSockets_UDP_ConnectRequest.identity', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_client_steam_id', full_name='CMsgSteamSockets_UDP_ConnectRequest.legacy_client_steam_id', index=8,
      number=3, type=6, cpp_type=4, label=1,
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
  serialized_start=374,
  serialized_end=724,
)


_CMSGSTEAMSOCKETS_UDP_CONNECTOK = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_ConnectOK',
  full_name='CMsgSteamSockets_UDP_ConnectOK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_connection_id', full_name='CMsgSteamSockets_UDP_ConnectOK.client_connection_id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_connection_id', full_name='CMsgSteamSockets_UDP_ConnectOK.server_connection_id', index=1,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='your_timestamp', full_name='CMsgSteamSockets_UDP_ConnectOK.your_timestamp', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay_time_usec', full_name='CMsgSteamSockets_UDP_ConnectOK.delay_time_usec', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypt', full_name='CMsgSteamSockets_UDP_ConnectOK.crypt', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cert', full_name='CMsgSteamSockets_UDP_ConnectOK.cert', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identity', full_name='CMsgSteamSockets_UDP_ConnectOK.identity', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legacy_server_steam_id', full_name='CMsgSteamSockets_UDP_ConnectOK.legacy_server_steam_id', index=7,
      number=2, type=6, cpp_type=4, label=1,
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
  serialized_start=727,
  serialized_end=1056,
)


_CMSGSTEAMSOCKETS_UDP_CONNECTIONCLOSED = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_ConnectionClosed',
  full_name='CMsgSteamSockets_UDP_ConnectionClosed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to_connection_id', full_name='CMsgSteamSockets_UDP_ConnectionClosed.to_connection_id', index=0,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_connection_id', full_name='CMsgSteamSockets_UDP_ConnectionClosed.from_connection_id', index=1,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='CMsgSteamSockets_UDP_ConnectionClosed.debug', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason_code', full_name='CMsgSteamSockets_UDP_ConnectionClosed.reason_code', index=3,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=1059,
  serialized_end=1188,
)


_CMSGSTEAMSOCKETS_UDP_NOCONNECTION = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_NoConnection',
  full_name='CMsgSteamSockets_UDP_NoConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_connection_id', full_name='CMsgSteamSockets_UDP_NoConnection.from_connection_id', index=0,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_connection_id', full_name='CMsgSteamSockets_UDP_NoConnection.to_connection_id', index=1,
      number=3, type=7, cpp_type=3, label=1,
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
  serialized_start=1190,
  serialized_end=1279,
)


_CMSGSTEAMSOCKETS_UDP_STATS = _descriptor.Descriptor(
  name='CMsgSteamSockets_UDP_Stats',
  full_name='CMsgSteamSockets_UDP_Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats', full_name='CMsgSteamSockets_UDP_Stats.stats', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='CMsgSteamSockets_UDP_Stats.flags', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_connection_id', full_name='CMsgSteamSockets_UDP_Stats.to_connection_id', index=2,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_connection_id', full_name='CMsgSteamSockets_UDP_Stats.from_connection_id', index=3,
      number=10, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq_num', full_name='CMsgSteamSockets_UDP_Stats.seq_num', index=4,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CMSGSTEAMSOCKETS_UDP_STATS_FLAGS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1282,
  serialized_end=1505,
)

_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST.fields_by_name['crypt'].message_type = steamnetworkingsockets__messages__pb2._CMSGSTEAMDATAGRAMSESSIONCRYPTINFOSIGNED
_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST.fields_by_name['cert'].message_type = steamnetworkingsockets__messages__certs__pb2._CMSGSTEAMDATAGRAMCERTIFICATESIGNED
_CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST.fields_by_name['identity'].message_type = steamnetworkingsockets__messages__certs__pb2._CMSGSTEAMNETWORKINGIDENTITY
_CMSGSTEAMSOCKETS_UDP_CONNECTOK.fields_by_name['crypt'].message_type = steamnetworkingsockets__messages__pb2._CMSGSTEAMDATAGRAMSESSIONCRYPTINFOSIGNED
_CMSGSTEAMSOCKETS_UDP_CONNECTOK.fields_by_name['cert'].message_type = steamnetworkingsockets__messages__certs__pb2._CMSGSTEAMDATAGRAMCERTIFICATESIGNED
_CMSGSTEAMSOCKETS_UDP_CONNECTOK.fields_by_name['identity'].message_type = steamnetworkingsockets__messages__certs__pb2._CMSGSTEAMNETWORKINGIDENTITY
_CMSGSTEAMSOCKETS_UDP_STATS.fields_by_name['stats'].message_type = steamnetworkingsockets__messages__pb2._CMSGSTEAMDATAGRAMCONNECTIONQUALITY
_CMSGSTEAMSOCKETS_UDP_STATS_FLAGS.containing_type = _CMSGSTEAMSOCKETS_UDP_STATS
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_ChallengeRequest'] = _CMSGSTEAMSOCKETS_UDP_CHALLENGEREQUEST
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_ChallengeReply'] = _CMSGSTEAMSOCKETS_UDP_CHALLENGEREPLY
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_ConnectRequest'] = _CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_ConnectOK'] = _CMSGSTEAMSOCKETS_UDP_CONNECTOK
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_ConnectionClosed'] = _CMSGSTEAMSOCKETS_UDP_CONNECTIONCLOSED
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_NoConnection'] = _CMSGSTEAMSOCKETS_UDP_NOCONNECTION
DESCRIPTOR.message_types_by_name['CMsgSteamSockets_UDP_Stats'] = _CMSGSTEAMSOCKETS_UDP_STATS
DESCRIPTOR.enum_types_by_name['ESteamNetworkingUDPMsgID'] = _ESTEAMNETWORKINGUDPMSGID

CMsgSteamSockets_UDP_ChallengeRequest = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_ChallengeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_CHALLENGEREQUEST,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_ChallengeRequest)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_ChallengeRequest)

CMsgSteamSockets_UDP_ChallengeReply = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_ChallengeReply', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_CHALLENGEREPLY,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_ChallengeReply)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_ChallengeReply)

CMsgSteamSockets_UDP_ConnectRequest = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_CONNECTREQUEST,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_ConnectRequest)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_ConnectRequest)

CMsgSteamSockets_UDP_ConnectOK = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_ConnectOK', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_CONNECTOK,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_ConnectOK)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_ConnectOK)

CMsgSteamSockets_UDP_ConnectionClosed = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_ConnectionClosed', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_CONNECTIONCLOSED,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_ConnectionClosed)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_ConnectionClosed)

CMsgSteamSockets_UDP_NoConnection = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_NoConnection', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_NOCONNECTION,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_NoConnection)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_NoConnection)

CMsgSteamSockets_UDP_Stats = _reflection.GeneratedProtocolMessageType('CMsgSteamSockets_UDP_Stats', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMSOCKETS_UDP_STATS,
  __module__ = 'steamnetworkingsockets_messages_udp_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamSockets_UDP_Stats)
  ))
_sym_db.RegisterMessage(CMsgSteamSockets_UDP_Stats)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001\200\001\000'))
# @@protoc_insertion_point(module_scope)