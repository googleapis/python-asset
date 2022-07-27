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
    "AnalyzeIamPolicyResponse",
    "ExportIamPolicyAnalysisResponse",
)


class AnalyzeIamPolicyResponse(proto.Message):
    r"""A response message for
    [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1p4beta1.AssetService.AnalyzeIamPolicy].

    Attributes:
        main_analysis (google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis):
            The main analysis that matches the original
            request.
        service_account_impersonation_analysis (Sequence[google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis]):
            The service account impersonation analysis if
            [AnalyzeIamPolicyRequest.analyze_service_account_impersonation][]
            is enabled.
        fully_explored (bool):
            Represents whether all entries in the
            [main_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.main_analysis]
            and
            [service_account_impersonation_analysis][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis]
            have been fully explored to answer the query in the request.
        non_critical_errors (Sequence[google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisResult.AnalysisState]):
            A list of non-critical errors happened during the request
            handling to explain why ``fully_explored`` is false, or
            empty if no error happened.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    class IamPolicyAnalysis(proto.Message):
        r"""An analysis message to group the query and results.

        Attributes:
            analysis_query (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery):
                The analysis query.
            analysis_results (Sequence[google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisResult]):
                A list of
                [IamPolicyAnalysisResult][google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult]
                that matches the analysis query, or empty if no result is
                found.
            fully_explored (bool):
                Represents whether all entries in the
                [analysis_results][google.cloud.asset.v1p4beta1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.analysis_results]
                have been fully explored to answer the query.
        """
        __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

        analysis_query = proto.Field(
            proto.MESSAGE,
            number=1,
            message="IamPolicyAnalysisQuery",
        )
        analysis_results = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=assets.IamPolicyAnalysisResult,
        )
        fully_explored = proto.Field(
            proto.BOOL,
            number=3,
        )

    main_analysis = proto.Field(
        proto.MESSAGE,
        number=1,
        message=IamPolicyAnalysis,
    )
    service_account_impersonation_analysis = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=IamPolicyAnalysis,
    )
    fully_explored = proto.Field(
        proto.BOOL,
        number=3,
    )
    non_critical_errors = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=assets.IamPolicyAnalysisResult.AnalysisState,
    )


class ExportIamPolicyAnalysisResponse(proto.Message):
    r"""The export IAM policy analysis response. This message is returned by
    the [google.longrunning.Operations.GetOperation][] method in the
    returned [google.longrunning.Operation.response][] field.

    Attributes:
        output_config (google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisOutputConfig):
            Output configuration indicating where the
            results were output to.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    output_config = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IamPolicyAnalysisOutputConfig",
    )


__all__ = tuple(sorted(__manifest__))
