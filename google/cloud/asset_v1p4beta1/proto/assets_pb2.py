# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1p4beta1/proto/assets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/asset_v1p4beta1/proto/assets.proto",
    package="google.cloud.asset.v1p4beta1",
    syntax="proto3",
    serialized_options=b"\n com.google.cloud.asset.v1p4beta1B\nAssetProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p4beta1;asset\370\001\001\252\002\034Google.Cloud.Asset.V1P4Beta1\312\002\034Google\\Cloud\\Asset\\V1p4beta1",
    serialized_pb=b'\n/google/cloud/asset_v1p4beta1/proto/assets.proto\x12\x1cgoogle.cloud.asset.v1p4beta1\x1a\x1agoogle/iam/v1/policy.proto\x1a\x15google/rpc/code.proto\x1a\x1cgoogle/api/annotations.proto"\x95\n\n\x17IamPolicyAnalysisResult\x12#\n\x1b\x61ttached_resource_full_name\x18\x01 \x01(\t\x12+\n\x0biam_binding\x18\x02 \x01(\x0b\x32\x16.google.iam.v1.Binding\x12\x65\n\x14\x61\x63\x63\x65ss_control_lists\x18\x03 \x03(\x0b\x32G.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList\x12Y\n\ridentity_list\x18\x04 \x01(\x0b\x32\x42.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.IdentityList\x12\x16\n\x0e\x66ully_explored\x18\x05 \x01(\x08\x1a>\n\rAnalysisState\x12\x1e\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x10.google.rpc.Code\x12\r\n\x05\x63\x61use\x18\x02 \x01(\t\x1a\x83\x01\n\x08Resource\x12\x1a\n\x12\x66ull_resource_name\x18\x01 \x01(\t\x12[\n\x0e\x61nalysis_state\x18\x02 \x01(\x0b\x32\x43.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState\x1a\x9b\x01\n\x06\x41\x63\x63\x65ss\x12\x0e\n\x04role\x18\x01 \x01(\tH\x00\x12\x14\n\npermission\x18\x02 \x01(\tH\x00\x12[\n\x0e\x61nalysis_state\x18\x03 \x01(\x0b\x32\x43.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisStateB\x0e\n\x0coneof_access\x1a\x30\n\x04\x45\x64ge\x12\x13\n\x0bsource_node\x18\x01 \x01(\t\x12\x13\n\x0btarget_node\x18\x02 \x01(\t\x1au\n\x08Identity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12[\n\x0e\x61nalysis_state\x18\x02 \x01(\x0b\x32\x43.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState\x1a\x8a\x02\n\x11\x41\x63\x63\x65ssControlList\x12Q\n\tresources\x18\x01 \x03(\x0b\x32>.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Resource\x12N\n\x08\x61\x63\x63\x65sses\x18\x02 \x03(\x0b\x32<.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access\x12R\n\x0eresource_edges\x18\x03 \x03(\x0b\x32:.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge\x1a\xb3\x01\n\x0cIdentityList\x12R\n\nidentities\x18\x01 \x03(\x0b\x32>.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Identity\x12O\n\x0bgroup_edges\x18\x02 \x03(\x0b\x32:.google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.EdgeB\xb4\x01\n com.google.cloud.asset.v1p4beta1B\nAssetProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p4beta1;asset\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.Asset.V1P4Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p4beta1b\x06proto3',
    dependencies=[
        google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,
        google_dot_rpc_dot_code__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_IAMPOLICYANALYSISRESULT_ANALYSISSTATE = _descriptor.Descriptor(
    name="AnalysisState",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState.code",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cause",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState.cause",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=490,
    serialized_end=552,
)

_IAMPOLICYANALYSISRESULT_RESOURCE = _descriptor.Descriptor(
    name="Resource",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Resource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="full_resource_name",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Resource.full_resource_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis_state",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Resource.analysis_state",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=555,
    serialized_end=686,
)

_IAMPOLICYANALYSISRESULT_ACCESS = _descriptor.Descriptor(
    name="Access",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="role",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access.role",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="permission",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access.permission",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis_state",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access.analysis_state",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="oneof_access",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access.oneof_access",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=689,
    serialized_end=844,
)

_IAMPOLICYANALYSISRESULT_EDGE = _descriptor.Descriptor(
    name="Edge",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="source_node",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge.source_node",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target_node",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge.target_node",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=846,
    serialized_end=894,
)

_IAMPOLICYANALYSISRESULT_IDENTITY = _descriptor.Descriptor(
    name="Identity",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Identity",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Identity.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis_state",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Identity.analysis_state",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=896,
    serialized_end=1013,
)

_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST = _descriptor.Descriptor(
    name="AccessControlList",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="resources",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList.resources",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accesses",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList.accesses",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="resource_edges",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList.resource_edges",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1016,
    serialized_end=1282,
)

_IAMPOLICYANALYSISRESULT_IDENTITYLIST = _descriptor.Descriptor(
    name="IdentityList",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.IdentityList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="identities",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.IdentityList.identities",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="group_edges",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.IdentityList.group_edges",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1285,
    serialized_end=1464,
)

_IAMPOLICYANALYSISRESULT = _descriptor.Descriptor(
    name="IamPolicyAnalysisResult",
    full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="attached_resource_full_name",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.attached_resource_full_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="iam_binding",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.iam_binding",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="access_control_lists",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.access_control_lists",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="identity_list",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.identity_list",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fully_explored",
            full_name="google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.fully_explored",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _IAMPOLICYANALYSISRESULT_ANALYSISSTATE,
        _IAMPOLICYANALYSISRESULT_RESOURCE,
        _IAMPOLICYANALYSISRESULT_ACCESS,
        _IAMPOLICYANALYSISRESULT_EDGE,
        _IAMPOLICYANALYSISRESULT_IDENTITY,
        _IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST,
        _IAMPOLICYANALYSISRESULT_IDENTITYLIST,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=163,
    serialized_end=1464,
)

_IAMPOLICYANALYSISRESULT_ANALYSISSTATE.fields_by_name[
    "code"
].enum_type = google_dot_rpc_dot_code__pb2._CODE
_IAMPOLICYANALYSISRESULT_ANALYSISSTATE.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_RESOURCE.fields_by_name[
    "analysis_state"
].message_type = _IAMPOLICYANALYSISRESULT_ANALYSISSTATE
_IAMPOLICYANALYSISRESULT_RESOURCE.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_ACCESS.fields_by_name[
    "analysis_state"
].message_type = _IAMPOLICYANALYSISRESULT_ANALYSISSTATE
_IAMPOLICYANALYSISRESULT_ACCESS.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_ACCESS.oneofs_by_name["oneof_access"].fields.append(
    _IAMPOLICYANALYSISRESULT_ACCESS.fields_by_name["role"]
)
_IAMPOLICYANALYSISRESULT_ACCESS.fields_by_name[
    "role"
].containing_oneof = _IAMPOLICYANALYSISRESULT_ACCESS.oneofs_by_name["oneof_access"]
_IAMPOLICYANALYSISRESULT_ACCESS.oneofs_by_name["oneof_access"].fields.append(
    _IAMPOLICYANALYSISRESULT_ACCESS.fields_by_name["permission"]
)
_IAMPOLICYANALYSISRESULT_ACCESS.fields_by_name[
    "permission"
].containing_oneof = _IAMPOLICYANALYSISRESULT_ACCESS.oneofs_by_name["oneof_access"]
_IAMPOLICYANALYSISRESULT_EDGE.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_IDENTITY.fields_by_name[
    "analysis_state"
].message_type = _IAMPOLICYANALYSISRESULT_ANALYSISSTATE
_IAMPOLICYANALYSISRESULT_IDENTITY.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST.fields_by_name[
    "resources"
].message_type = _IAMPOLICYANALYSISRESULT_RESOURCE
_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST.fields_by_name[
    "accesses"
].message_type = _IAMPOLICYANALYSISRESULT_ACCESS
_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST.fields_by_name[
    "resource_edges"
].message_type = _IAMPOLICYANALYSISRESULT_EDGE
_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT_IDENTITYLIST.fields_by_name[
    "identities"
].message_type = _IAMPOLICYANALYSISRESULT_IDENTITY
_IAMPOLICYANALYSISRESULT_IDENTITYLIST.fields_by_name[
    "group_edges"
].message_type = _IAMPOLICYANALYSISRESULT_EDGE
_IAMPOLICYANALYSISRESULT_IDENTITYLIST.containing_type = _IAMPOLICYANALYSISRESULT
_IAMPOLICYANALYSISRESULT.fields_by_name[
    "iam_binding"
].message_type = (
    google_dot_iam_dot_v1_dot_policy__pb2.google_dot_iam_dot_v1_dot_policy__pb2._BINDING
)
_IAMPOLICYANALYSISRESULT.fields_by_name[
    "access_control_lists"
].message_type = _IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST
_IAMPOLICYANALYSISRESULT.fields_by_name[
    "identity_list"
].message_type = _IAMPOLICYANALYSISRESULT_IDENTITYLIST
DESCRIPTOR.message_types_by_name["IamPolicyAnalysisResult"] = _IAMPOLICYANALYSISRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IamPolicyAnalysisResult = _reflection.GeneratedProtocolMessageType(
    "IamPolicyAnalysisResult",
    (_message.Message,),
    {
        "AnalysisState": _reflection.GeneratedProtocolMessageType(
            "AnalysisState",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_ANALYSISSTATE,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """Represents analysis state of each node in the result graph or
    non-critical errors in the response.
    
    
    Attributes:
        code:
            The Google standard error code that best describes the state.
            For example: - OK means the node has been successfully
            explored; - PERMISSION_DENIED means an access denied error is
            encountered; - DEADLINE_EXCEEDED means the node hasn’t been
            explored in time;
        cause:
            The human-readable description of the cause of failure.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AnalysisState)
            },
        ),
        "Resource": _reflection.GeneratedProtocolMessageType(
            "Resource",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_RESOURCE,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """A GCP resource that appears in an access control list.
    
    
    Attributes:
        full_resource_name:
            The `full resource name <https://aip.dev/122#full-resource-
            names>`__.
        analysis_state:
            The analysis state of this resource node.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Resource)
            },
        ),
        "Access": _reflection.GeneratedProtocolMessageType(
            "Access",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_ACCESS,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """A role or permission that appears in an access control
    list.
    
    
    Attributes:
        role:
            The role.
        permission:
            The permission.
        analysis_state:
            The analysis state of this access node.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Access)
            },
        ),
        "Edge": _reflection.GeneratedProtocolMessageType(
            "Edge",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_EDGE,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """A directional edge.
    
    
    Attributes:
        source_node:
            The source node of the edge.
        target_node:
            The target node of the edge.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge)
            },
        ),
        "Identity": _reflection.GeneratedProtocolMessageType(
            "Identity",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_IDENTITY,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """An identity that appears in an access control list.
    
    
    Attributes:
        name:
            The identity name in any form of members appear in `IAM policy
            binding
            <https://cloud.google.com/iam/reference/rest/v1/Binding>`__,
            such as: - user:foo@google.com - group:group1@google.com -
            serviceAccount:s1@prj1.iam.gserviceaccount.com -
            projectOwner:some_project_id - domain:google.com - allUsers -
            etc.
        analysis_state:
            The analysis state of this identity node.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Identity)
            },
        ),
        "AccessControlList": _reflection.GeneratedProtocolMessageType(
            "AccessControlList",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """An access control list, derived from the above IAM policy
    binding, which contains a set of resources and accesses. May include one
    item from each set to compose an access control entry.
    
    NOTICE that there could be multiple access control lists for one IAM
    policy binding. The access control lists are created based on resource
    and access combinations.
    
    For example, assume we have the following cases in one IAM policy
    binding: - Permission P1 and P2 apply to resource R1 and R2; -
    Permission P3 applies to resource R2 and R3;
    
    This will result in the following access control lists: -
    AccessControlList 1: [R1, R2], [P1, P2] - AccessControlList 2: [R2, R3],
    [P3]
    
    
    Attributes:
        resources:
            The resources that match one of the following conditions: -
            The resource_selector, if it is specified in request; -
            Otherwise, resources reachable from the policy attached
            resource.
        accesses:
            The accesses that match one of the following conditions: - The
            access_selector, if it is specified in request; - Otherwise,
            access specifiers reachable from the policy binding’s role.
        resource_edges:
            Resource edges of the graph starting from the policy attached
            resource to any descendant resources. The [Edge.source_node][g
            oogle.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.Edge.sourc
            e_node] contains the full resource name of a parent resource
            and [Edge.target_node][google.cloud.asset.v1p4beta1.IamPolicyA
            nalysisResult.Edge.target_node] contains the full resource
            name of a child resource. This field is present only if the
            output_resource_edges option is enabled in request.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.AccessControlList)
            },
        ),
        "IdentityList": _reflection.GeneratedProtocolMessageType(
            "IdentityList",
            (_message.Message,),
            {
                "DESCRIPTOR": _IAMPOLICYANALYSISRESULT_IDENTITYLIST,
                "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
                "__doc__": """
    Attributes:
        identities:
            Only the identities that match one of the following conditions
            will be presented: - The identity_selector, if it is specified
            in request; - Otherwise, identities reachable from the policy
            binding’s members.
        group_edges:
            Group identity edges of the graph starting from the binding’s
            group members to any node of the [identities][google.cloud.ass
            et.v1p4beta1.IamPolicyAnalysisResult.IdentityList.identities].
            The [Edge.source_node][google.cloud.asset.v1p4beta1.IamPolicyA
            nalysisResult.Edge.source_node] contains a group, such as
            “group:parent@google.com”. The [Edge.target_node][google.cloud
            .asset.v1p4beta1.IamPolicyAnalysisResult.Edge.target_node]
            contains a member of the group, such as
            “group:child@google.com” or “user:foo@google.com”. This field
            is present only if the output_group_edges option is enabled in
            request.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.IdentityList)
            },
        ),
        "DESCRIPTOR": _IAMPOLICYANALYSISRESULT,
        "__module__": "google.cloud.asset_v1p4beta1.proto.assets_pb2",
        "__doc__": """IAM Policy analysis result, consisting of one IAM policy
  binding and derived access control lists.
  
  
  Attributes:
      attached_resource_full_name:
          The full name of the resource to which the [iam_binding][googl
          e.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.iam_binding]
          policy attaches.
      iam_binding:
          The Cloud IAM policy binding under analysis.
      access_control_lists:
          The access control lists derived from the [iam_binding][google
          .cloud.asset.v1p4beta1.IamPolicyAnalysisResult.iam_binding]
          that match or potentially match resource and access selectors
          specified in the request.
      identity_list:
          The identity list derived from members of the [iam_binding][go
          ogle.cloud.asset.v1p4beta1.IamPolicyAnalysisResult.iam_binding
          ] that match or potentially match identity selector specified
          in the request.
      fully_explored:
          Represents whether all nodes in the transitive closure of the 
          [iam_binding][google.cloud.asset.v1p4beta1.IamPolicyAnalysisRe
          sult.iam_binding] node have been explored.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult)
    },
)
_sym_db.RegisterMessage(IamPolicyAnalysisResult)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.AnalysisState)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.Resource)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.Access)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.Edge)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.Identity)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.AccessControlList)
_sym_db.RegisterMessage(IamPolicyAnalysisResult.IdentityList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
