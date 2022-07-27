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

__manifest__ = (
    "AnalyzeIamPolicyRequest",
    "ExportIamPolicyAnalysisRequest",
)


class AnalyzeIamPolicyRequest(proto.Message):
    r"""A request message for
    [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1p4beta1.AssetService.AnalyzeIamPolicy].

    Attributes:
        analysis_query (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery):
            Required. The request query.
        options (google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyRequest.Options):
            Optional. The request options.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    class Options(proto.Message):
        r"""Contains request options.

        Attributes:
            expand_groups (bool):
                Optional. If true, the identities section of the result will
                expand any Google groups appearing in an IAM policy binding.

                If [identity_selector][] is specified, the identity in the
                result will be determined by the selector, and this flag
                will have no effect.

                Default is false.
            expand_roles (bool):
                Optional. If true, the access section of result will expand
                any roles appearing in IAM policy bindings to include their
                permissions.

                If [access_selector][] is specified, the access section of
                the result will be determined by the selector, and this flag
                will have no effect.

                Default is false.
            expand_resources (bool):
                Optional. If true, the resource section of the result will
                expand any resource attached to an IAM policy to include
                resources lower in the resource hierarchy.

                For example, if the request analyzes for which resources
                user A has permission P, and the results include an IAM
                policy with P on a GCP folder, the results will also include
                resources in that folder with permission P.

                If [resource_selector][] is specified, the resource section
                of the result will be determined by the selector, and this
                flag will have no effect. Default is false.
            output_resource_edges (bool):
                Optional. If true, the result will output
                resource edges, starting from the policy
                attached resource, to any expanded resources.
                Default is false.
            output_group_edges (bool):
                Optional. If true, the result will output
                group identity edges, starting from the
                binding's group members, to any expanded
                identities. Default is false.
            analyze_service_account_impersonation (bool):
                Optional. If true, the response will include access analysis
                from identities to resources via service account
                impersonation. This is a very expensive operation, because
                many derived queries will be executed. We highly recommend
                you use ExportIamPolicyAnalysis rpc instead.

                For example, if the request analyzes for which resources
                user A has permission P, and there's an IAM policy states
                user A has iam.serviceAccounts.getAccessToken permission to
                a service account SA, and there's another IAM policy states
                service account SA has permission P to a GCP folder F, then
                user A potentially has access to the GCP folder F. And those
                advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Another example, if the request analyzes for who has
                permission P to a GCP folder F, and there's an IAM policy
                states user A has iam.serviceAccounts.actAs permission to a
                service account SA, and there's another IAM policy states
                service account SA has permission P to the GCP folder F,
                then user A potentially has access to the GCP folder F. And
                those advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Default is false.
            execution_timeout (google.protobuf.duration_pb2.Duration):
                Optional. Amount of time executable has to complete. See
                JSON representation of
                `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

                If this field is set with a value less than the RPC
                deadline, and the execution of your query hasn't finished in
                the specified execution timeout, you will get a response
                with partial result. Otherwise, your query's execution will
                continue until the RPC deadline. If it's not finished until
                then, you will get a DEADLINE_EXCEEDED error.

                Default is empty.
        """
        __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

        expand_groups = proto.Field(
            proto.BOOL,
            number=1,
        )
        expand_roles = proto.Field(
            proto.BOOL,
            number=2,
        )
        expand_resources = proto.Field(
            proto.BOOL,
            number=3,
        )
        output_resource_edges = proto.Field(
            proto.BOOL,
            number=4,
        )
        output_group_edges = proto.Field(
            proto.BOOL,
            number=5,
        )
        analyze_service_account_impersonation = proto.Field(
            proto.BOOL,
            number=6,
        )
        execution_timeout = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )

    analysis_query = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IamPolicyAnalysisQuery",
    )
    options = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Options,
    )


class ExportIamPolicyAnalysisRequest(proto.Message):
    r"""A request message for
    [AssetService.ExportIamPolicyAnalysis][google.cloud.asset.v1p4beta1.AssetService.ExportIamPolicyAnalysis].

    Attributes:
        analysis_query (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery):
            Required. The request query.
        options (google.cloud.asset_v1p4beta1.types.ExportIamPolicyAnalysisRequest.Options):
            Optional. The request options.
        output_config (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisOutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    class Options(proto.Message):
        r"""Contains request options.

        Attributes:
            expand_groups (bool):
                Optional. If true, the identities section of the result will
                expand any Google groups appearing in an IAM policy binding.

                If [identity_selector][] is specified, the identity in the
                result will be determined by the selector, and this flag
                will have no effect.

                Default is false.
            expand_roles (bool):
                Optional. If true, the access section of result will expand
                any roles appearing in IAM policy bindings to include their
                permissions.

                If [access_selector][] is specified, the access section of
                the result will be determined by the selector, and this flag
                will have no effect.

                Default is false.
            expand_resources (bool):
                Optional. If true, the resource section of the result will
                expand any resource attached to an IAM policy to include
                resources lower in the resource hierarchy.

                For example, if the request analyzes for which resources
                user A has permission P, and the results include an IAM
                policy with P on a GCP folder, the results will also include
                resources in that folder with permission P.

                If [resource_selector][] is specified, the resource section
                of the result will be determined by the selector, and this
                flag will have no effect. Default is false.
            output_resource_edges (bool):
                Optional. If true, the result will output
                resource edges, starting from the policy
                attached resource, to any expanded resources.
                Default is false.
            output_group_edges (bool):
                Optional. If true, the result will output
                group identity edges, starting from the
                binding's group members, to any expanded
                identities. Default is false.
            analyze_service_account_impersonation (bool):
                Optional. If true, the response will include access analysis
                from identities to resources via service account
                impersonation. This is a very expensive operation, because
                many derived queries will be executed.

                For example, if the request analyzes for which resources
                user A has permission P, and there's an IAM policy states
                user A has iam.serviceAccounts.getAccessToken permission to
                a service account SA, and there's another IAM policy states
                service account SA has permission P to a GCP folder F, then
                user A potentially has access to the GCP folder F. And those
                advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Another example, if the request analyzes for who has
                permission P to a GCP folder F, and there's an IAM policy
                states user A has iam.serviceAccounts.actAs permission to a
                service account SA, and there's another IAM policy states
                service account SA has permission P to the GCP folder F,
                then user A potentially has access to the GCP folder F. And
                those advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Default is false.
        """
        __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

        expand_groups = proto.Field(
            proto.BOOL,
            number=1,
        )
        expand_roles = proto.Field(
            proto.BOOL,
            number=2,
        )
        expand_resources = proto.Field(
            proto.BOOL,
            number=3,
        )
        output_resource_edges = proto.Field(
            proto.BOOL,
            number=4,
        )
        output_group_edges = proto.Field(
            proto.BOOL,
            number=5,
        )
        analyze_service_account_impersonation = proto.Field(
            proto.BOOL,
            number=6,
        )

    analysis_query = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IamPolicyAnalysisQuery",
    )
    options = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Options,
    )
    output_config = proto.Field(
        proto.MESSAGE,
        number=3,
        message="IamPolicyAnalysisOutputConfig",
    )


__all__ = tuple(sorted(__manifest__))
