# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.asset_v1p4beta1.types import assets
from google.protobuf import duration_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.asset.v1p4beta1",
    manifest={
        "IamPolicyAnalysisQuery",
        "AnalyzeIamPolicyRequest",
        "AnalyzeIamPolicyResponse",
        "IamPolicyAnalysisOutputConfig",
        "ExportIamPolicyAnalysisRequest",
        "ExportIamPolicyAnalysisResponse",
    },
)


from .requests import (
    AnalyzeIamPolicyRequest,
    ExportIamPolicyAnalysisRequest,
)

from .responses import (
    AnalyzeIamPolicyResponse,
    ExportIamPolicyAnalysisResponse,
)


class IamPolicyAnalysisQuery(proto.Message):
    r"""IAM policy analysis query message.

    Attributes:
        parent (str):
            Required. The relative name of the root
            asset. Only resources and IAM policies within
            the parent will be analyzed. This can only be an
            organization number (such as
            "organizations/123") or a folder number (such as
            "folders/123").
        resource_selector (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery.ResourceSelector):
            Optional. Specifies a resource for analysis.
            Leaving it empty means ANY.
        identity_selector (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery.IdentitySelector):
            Optional. Specifies an identity for analysis.
            Leaving it empty means ANY.
        access_selector (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery.AccessSelector):
            Optional. Specifies roles or permissions for
            analysis. Leaving it empty means ANY.
    """

    class ResourceSelector(proto.Message):
        r"""Specifies the resource to analyze for access policies, which may be
        set directly on the resource, or on ancestors such as organizations,
        folders or projects. At least one of
        [ResourceSelector][google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.ResourceSelector],
        [IdentitySelector][google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.IdentitySelector]
        or
        [AccessSelector][google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.AccessSelector]
        must be specified in a request.

        Attributes:
            full_resource_name (str):
                Required. The `full resource
                name <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
                .
        """

        full_resource_name = proto.Field(
            proto.STRING,
            number=1,
        )

    class IdentitySelector(proto.Message):
        r"""Specifies an identity for which to determine resource access,
        based on roles assigned either directly to them or to the groups
        they belong to, directly or indirectly.

        Attributes:
            identity (str):
                Required. The identity appear in the form of members in `IAM
                policy
                binding <https://cloud.google.com/iam/reference/rest/v1/Binding>`__.
        """

        identity = proto.Field(
            proto.STRING,
            number=1,
        )

    class AccessSelector(proto.Message):
        r"""Specifies roles and/or permissions to analyze, to determine
        both the identities possessing them and the resources they
        control. If multiple values are specified, results will include
        identities and resources matching any of them.

        Attributes:
            roles (Sequence[str]):
                Optional. The roles to appear in result.
            permissions (Sequence[str]):
                Optional. The permissions to appear in
                result.
        """

        roles = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        permissions = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_selector = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ResourceSelector,
    )
    identity_selector = proto.Field(
        proto.MESSAGE,
        number=3,
        message=IdentitySelector,
    )
    access_selector = proto.Field(
        proto.MESSAGE,
        number=4,
        message=AccessSelector,
    )


class IamPolicyAnalysisOutputConfig(proto.Message):
    r"""Output configuration for export IAM policy analysis
    destination.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisOutputConfig.GcsDestination):
            Destination on Cloud Storage.

            This field is a member of `oneof`_ ``destination``.
    """

    class GcsDestination(proto.Message):
        r"""A Cloud Storage location.

        Attributes:
            uri (str):
                Required. The uri of the Cloud Storage object. It's the same
                uri that is used by gsutil. For example:
                "gs://bucket_name/object_name". See `Viewing and Editing
                Object
                Metadata <https://cloud.google.com/storage/docs/viewing-editing-metadata>`__
                for more information.
        """

        uri = proto.Field(
            proto.STRING,
            number=1,
        )

    gcs_destination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message=GcsDestination,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
