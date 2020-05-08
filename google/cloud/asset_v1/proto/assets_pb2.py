# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1/proto/assets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.orgpolicy.v1 import orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.identity.accesscontextmanager.v1 import access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2
from google.identity.accesscontextmanager.v1 import access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2
from google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/asset_v1/proto/assets.proto',
  package='google.cloud.asset.v1',
  syntax='proto3',
  serialized_options=b'\n\031com.google.cloud.asset.v1B\nAssetProtoP\001Z:google.golang.org/genproto/googleapis/cloud/asset/v1;asset\370\001\001\252\002\025Google.Cloud.Asset.V1\312\002\025Google\\Cloud\\Asset\\V1',
  serialized_pb=b'\n(google/cloud/asset_v1/proto/assets.proto\x12\x15google.cloud.asset.v1\x1a\x19google/api/resource.proto\x1a)google/cloud/orgpolicy/v1/orgpolicy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x80\x01\n\rTemporalAsset\x12\x31\n\x06window\x18\x01 \x01(\x0b\x32!.google.cloud.asset.v1.TimeWindow\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12+\n\x05\x61sset\x18\x03 \x01(\x0b\x32\x1c.google.cloud.asset.v1.Asset\"j\n\nTimeWindow\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x89\x04\n\x05\x41sset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x31\n\x08resource\x18\x03 \x01(\x0b\x32\x1f.google.cloud.asset.v1.Resource\x12)\n\niam_policy\x18\x04 \x01(\x0b\x32\x15.google.iam.v1.Policy\x12\x35\n\norg_policy\x18\x06 \x03(\x0b\x32!.google.cloud.orgpolicy.v1.Policy\x12N\n\raccess_policy\x18\x07 \x01(\x0b\x32\x35.google.identity.accesscontextmanager.v1.AccessPolicyH\x00\x12L\n\x0c\x61\x63\x63\x65ss_level\x18\x08 \x01(\x0b\x32\x34.google.identity.accesscontextmanager.v1.AccessLevelH\x00\x12V\n\x11service_perimeter\x18\t \x01(\x0b\x32\x39.google.identity.accesscontextmanager.v1.ServicePerimeterH\x00\x12\x11\n\tancestors\x18\n \x03(\t:\'\xea\x41$\n\x1f\x63loudasset.googleapis.com/Asset\x12\x01*B\x17\n\x15\x61\x63\x63\x65ss_context_policy\"\xa0\x01\n\x08Resource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x16\x64iscovery_document_uri\x18\x02 \x01(\t\x12\x16\n\x0e\x64iscovery_name\x18\x03 \x01(\t\x12\x14\n\x0cresource_url\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12%\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\x98\x01\n\x19\x63om.google.cloud.asset.v1B\nAssetProtoP\x01Z:google.golang.org/genproto/googleapis/cloud/asset/v1;asset\xf8\x01\x01\xaa\x02\x15Google.Cloud.Asset.V1\xca\x02\x15Google\\Cloud\\Asset\\V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_TEMPORALASSET = _descriptor.Descriptor(
  name='TemporalAsset',
  full_name='google.cloud.asset.v1.TemporalAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='google.cloud.asset.v1.TemporalAsset.window', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='google.cloud.asset.v1.TemporalAsset.deleted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.cloud.asset.v1.TemporalAsset.asset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=600,
)


_TIMEWINDOW = _descriptor.Descriptor(
  name='TimeWindow',
  full_name='google.cloud.asset.v1.TimeWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.asset.v1.TimeWindow.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.asset.v1.TimeWindow.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=602,
  serialized_end=708,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='google.cloud.asset.v1.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.asset.v1.Asset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='google.cloud.asset.v1.Asset.asset_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.cloud.asset.v1.Asset.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iam_policy', full_name='google.cloud.asset.v1.Asset.iam_policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org_policy', full_name='google.cloud.asset.v1.Asset.org_policy', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_policy', full_name='google.cloud.asset.v1.Asset.access_policy', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_level', full_name='google.cloud.asset.v1.Asset.access_level', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_perimeter', full_name='google.cloud.asset.v1.Asset.service_perimeter', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ancestors', full_name='google.cloud.asset.v1.Asset.ancestors', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A$\n\037cloudasset.googleapis.com/Asset\022\001*',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='access_context_policy', full_name='google.cloud.asset.v1.Asset.access_context_policy',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=711,
  serialized_end=1232,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='google.cloud.asset.v1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.asset.v1.Resource.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_document_uri', full_name='google.cloud.asset.v1.Resource.discovery_document_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_name', full_name='google.cloud.asset.v1.Resource.discovery_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='google.cloud.asset.v1.Resource.resource_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.asset.v1.Resource.parent', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.cloud.asset.v1.Resource.data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1235,
  serialized_end=1395,
)

_TEMPORALASSET.fields_by_name['window'].message_type = _TIMEWINDOW
_TEMPORALASSET.fields_by_name['asset'].message_type = _ASSET
_TIMEWINDOW.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEWINDOW.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSET.fields_by_name['resource'].message_type = _RESOURCE
_ASSET.fields_by_name['iam_policy'].message_type = google_dot_iam_dot_v1_dot_policy__pb2.google_dot_iam_dot_v1_dot_policy__pb2._POLICY
_ASSET.fields_by_name['org_policy'].message_type = google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2._POLICY
_ASSET.fields_by_name['access_policy'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2._ACCESSPOLICY
_ASSET.fields_by_name['access_level'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2._ACCESSLEVEL
_ASSET.fields_by_name['service_perimeter'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2._SERVICEPERIMETER
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['access_policy'])
_ASSET.fields_by_name['access_policy'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['access_level'])
_ASSET.fields_by_name['access_level'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['service_perimeter'])
_ASSET.fields_by_name['service_perimeter'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_RESOURCE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['TemporalAsset'] = _TEMPORALASSET
DESCRIPTOR.message_types_by_name['TimeWindow'] = _TIMEWINDOW
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemporalAsset = _reflection.GeneratedProtocolMessageType('TemporalAsset', (_message.Message,), {
  'DESCRIPTOR' : _TEMPORALASSET,
  '__module__' : 'google.cloud.asset_v1.proto.assets_pb2'
  ,
  '__doc__': """An asset in Google Cloud and its temporal metadata,
  including the time window when it was observed and its status during
  that window.
  
  
  Attributes:
      window:
          The time window when the asset data and state was observed.
      deleted:
          Whether the asset has been deleted or not.
      asset:
          An asset in Google Cloud.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1.TemporalAsset)
  })
_sym_db.RegisterMessage(TemporalAsset)

TimeWindow = _reflection.GeneratedProtocolMessageType('TimeWindow', (_message.Message,), {
  'DESCRIPTOR' : _TIMEWINDOW,
  '__module__' : 'google.cloud.asset_v1.proto.assets_pb2'
  ,
  '__doc__': """A time window specified by its “start_time” and
  “end_time”.
  
  
  Attributes:
      start_time:
          Start time of the time window (exclusive).
      end_time:
          End time of the time window (inclusive). If not specified, the
          current timestamp is used instead.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1.TimeWindow)
  })
_sym_db.RegisterMessage(TimeWindow)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'google.cloud.asset_v1.proto.assets_pb2'
  ,
  '__doc__': """An asset in Google Cloud. An asset can be any resource in the Google
  Cloud `resource
  hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
  a resource outside the Google Cloud resource hierarchy (such as Google
  Kubernetes Engine clusters and objects), or a Cloud IAM policy.
  
  
  Attributes:
      name:
          The full name of the asset. For example: “//compute.googleapis
          .com/projects/my_project_123/zones/zone1/instances/instance1”
          See `Resource names <https://cloud.google.com/apis/design/reso
          urce_names#full_resource_name>`__ for more information.
      asset_type:
          The type of the asset. For example:
          “compute.googleapis.com/Disk”  See `Supported asset types
          <https://cloud.google.com/asset-inventory/docs/supported-
          asset-types>`__ for more information.
      resource:
          A representation of the resource.
      iam_policy:
          A representation of the Cloud IAM policy set on a Google Cloud
          resource. There can be a maximum of one Cloud IAM policy set
          on any given resource. In addition, Cloud IAM policies inherit
          their granted access scope from any policies set on parent
          resources in the resource hierarchy. Therefore, the
          effectively policy is the union of both the policy set on this
          resource and each policy set on all of the resource’s ancestry
          resource levels in the hierarchy. See `this topic
          <https://cloud.google.com/iam/docs/policies#inheritance>`__
          for more information.
      org_policy:
          A representation of an `organization policy
          <https://cloud.google.com/resource-manager/docs/organization-
          policy/overview#organization_policy>`__. There can be more
          than one organization policy with different constraints set on
          a given resource.
      access_context_policy:
          A representation of an `access policy
          <https://cloud.google.com/access-context-
          manager/docs/overview#access-policies>`__.
      ancestors:
          The ancestry path of an asset in Google Cloud `resource
          hierarchy <https://cloud.google.com/resource-
          manager/docs/cloud-platform-resource-hierarchy>`__,
          represented as a list of relative resource names. An ancestry
          path starts with the closest ancestor in the hierarchy and
          ends at root. If the asset is a project, folder, or
          organization, the ancestry path starts from the asset itself.
          For example: ``["projects/123456789", "folders/5432",
          "organizations/1234"]``
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1.Asset)
  })
_sym_db.RegisterMessage(Asset)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'google.cloud.asset_v1.proto.assets_pb2'
  ,
  '__doc__': """A representation of a Google Cloud resource.
  
  
  Attributes:
      version:
          The API version. For example: “v1”
      discovery_document_uri:
          The URL of the discovery document containing the resource’s
          JSON schema. For example:
          “https://www.googleapis.com/discovery/v1/apis/compute/v1/rest”
          This value is unspecified for resources that do not have an
          API based on a discovery document, such as Cloud Bigtable.
      discovery_name:
          The JSON schema name listed in the discovery document. For
          example: “Project”  This value is unspecified for resources
          that do not have an API based on a discovery document, such as
          Cloud Bigtable.
      resource_url:
          The REST URL for accessing the resource. An HTTP ``GET``
          request using this URL returns the resource itself. For
          example:
          “https://cloudresourcemanager.googleapis.com/v1/projects/my-
          project-123”  This value is unspecified for resources without
          a REST API.
      parent:
          The full name of the immediate parent of this resource. See
          `Resource Names <https://cloud.google.com/apis/design/resource
          _names#full_resource_name>`__ for more information.  For
          Google Cloud assets, this value is the parent resource defined
          in the `Cloud IAM policy hierarchy <https://cloud.google.com/i
          am/docs/overview#policy_hierarchy>`__. For example: “//cloudre
          sourcemanager.googleapis.com/projects/my_project_123”  For
          third-party assets, this field may be set differently.
      data:
          The content of the resource, in which some sensitive fields
          are removed and may not be present.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1.Resource)
  })
_sym_db.RegisterMessage(Resource)


DESCRIPTOR._options = None
_ASSET._options = None
# @@protoc_insertion_point(module_scope)
