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

from google.cloud.asset_v1.types import assets as gca_assets
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from google.type import expr_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.asset.v1",
    manifest={
        "ContentType",
        "AnalyzeIamPolicyLongrunningMetadata",
        "ExportAssetsRequest",
        "ExportAssetsResponse",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "BatchGetAssetsHistoryRequest",
        "BatchGetAssetsHistoryResponse",
        "CreateFeedRequest",
        "GetFeedRequest",
        "ListFeedsRequest",
        "ListFeedsResponse",
        "UpdateFeedRequest",
        "DeleteFeedRequest",
        "OutputConfig",
        "OutputResult",
        "GcsOutputResult",
        "GcsDestination",
        "BigQueryDestination",
        "PartitionSpec",
        "PubsubDestination",
        "FeedOutputConfig",
        "Feed",
        "SearchAllResourcesRequest",
        "SearchAllResourcesResponse",
        "SearchAllIamPoliciesRequest",
        "SearchAllIamPoliciesResponse",
        "IamPolicyAnalysisQuery",
        "AnalyzeIamPolicyRequest",
        "AnalyzeIamPolicyResponse",
        "IamPolicyAnalysisOutputConfig",
        "AnalyzeIamPolicyLongrunningRequest",
        "AnalyzeIamPolicyLongrunningResponse",
        "SavedQuery",
        "CreateSavedQueryRequest",
        "GetSavedQueryRequest",
        "ListSavedQueriesRequest",
        "ListSavedQueriesResponse",
        "UpdateSavedQueryRequest",
        "DeleteSavedQueryRequest",
        "AnalyzeMoveRequest",
        "AnalyzeMoveResponse",
        "MoveAnalysis",
        "MoveAnalysisResult",
        "MoveImpact",
        "BatchGetEffectiveIamPoliciesRequest",
        "BatchGetEffectiveIamPoliciesResponse",
    },
)


from .requests import (
    ExportAssetsRequest,
    ListAssetsRequest,
    BatchGetAssetsHistoryRequest,
    CreateFeedRequest,
    GetFeedRequest,
    ListFeedsRequest,
    UpdateFeedRequest,
    DeleteFeedRequest,
    SearchAllResourcesRequest,
    SearchAllIamPoliciesRequest,
    AnalyzeIamPolicyRequest,
    AnalyzeIamPolicyLongrunningRequest,
    CreateSavedQueryRequest,
    GetSavedQueryRequest,
    ListSavedQueriesRequest,
    UpdateSavedQueryRequest,
    DeleteSavedQueryRequest,
    AnalyzeMoveRequest,
    BatchGetEffectiveIamPoliciesRequest,
)

from .responses import (
    ExportAssetsResponse,
    ListAssetsResponse,
    BatchGetAssetsHistoryResponse,
    ListFeedsResponse,
    SearchAllResourcesResponse,
    SearchAllIamPoliciesResponse,
    AnalyzeIamPolicyResponse,
    AnalyzeIamPolicyLongrunningResponse,
    ListSavedQueriesResponse,
    AnalyzeMoveResponse,
    BatchGetEffectiveIamPoliciesResponse,
)


class ContentType(proto.Enum):
    r"""Asset content type."""
    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2
    ORG_POLICY = 4
    ACCESS_POLICY = 5
    OS_INVENTORY = 6
    RELATIONSHIP = 7


class AnalyzeIamPolicyLongrunningMetadata(proto.Message):
    r"""Represents the metadata of the longrunning operation for the
    AnalyzeIamPolicyLongrunning rpc.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class OutputConfig(proto.Message):
    r"""Output configuration for export assets destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.asset_v1.types.GcsDestination):
            Destination on Cloud Storage.

            This field is a member of `oneof`_ ``destination``.
        bigquery_destination (google.cloud.asset_v1.types.BigQueryDestination):
            Destination on BigQuery. The output table
            stores the fields in asset Protobuf as columns
            in BigQuery.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )
    bigquery_destination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="BigQueryDestination",
    )


class OutputResult(proto.Message):
    r"""Output result of export assets.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_result (google.cloud.asset_v1.types.GcsOutputResult):
            Export result on Cloud Storage.

            This field is a member of `oneof`_ ``result``.
    """

    gcs_result = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message="GcsOutputResult",
    )


class GcsOutputResult(proto.Message):
    r"""A Cloud Storage output result.

    Attributes:
        uris (Sequence[str]):
            List of uris of the Cloud Storage objects. Example:
            "gs://bucket_name/object_name".
    """

    uris = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class GcsDestination(proto.Message):
    r"""A Cloud Storage location.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            The uri of the Cloud Storage object. It's the same uri that
            is used by gsutil. Example: "gs://bucket_name/object_name".
            See `Viewing and Editing Object
            Metadata <https://cloud.google.com/storage/docs/viewing-editing-metadata>`__
            for more information.

            If the specified Cloud Storage object already exists and
            there is no
            `hold <https://cloud.google.com/storage/docs/object-holds>`__,
            it will be overwritten with the exported result.

            This field is a member of `oneof`_ ``object_uri``.
        uri_prefix (str):
            The uri prefix of all generated Cloud Storage objects.
            Example: "gs://bucket_name/object_name_prefix". Each object
            uri is in format: "gs://bucket_name/object_name_prefix// and
            only contains assets for that type. starts from 0. Example:
            "gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0"
            is the first shard of output objects containing all
            compute.googleapis.com/Disk assets. An INVALID_ARGUMENT
            error will be returned if file with the same name
            "gs://bucket_name/object_name_prefix" already exists.

            This field is a member of `oneof`_ ``object_uri``.
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
        oneof="object_uri",
    )
    uri_prefix = proto.Field(
        proto.STRING,
        number=2,
        oneof="object_uri",
    )


class BigQueryDestination(proto.Message):
    r"""A BigQuery destination for exporting assets to.

    Attributes:
        dataset (str):
            Required. The BigQuery dataset in format
            "projects/projectId/datasets/datasetId", to which the
            snapshot result should be exported. If this dataset does not
            exist, the export call returns an INVALID_ARGUMENT error.
            Setting the ``contentType`` for ``exportAssets`` determines
            the
            `schema </asset-inventory/docs/exporting-to-bigquery#bigquery-schema>`__
            of the BigQuery table. Setting
            ``separateTablesPerAssetType`` to ``TRUE`` also influences
            the schema.
        table (str):
            Required. The BigQuery table to which the
            snapshot result should be written. If this table
            does not exist, a new table with the given name
            will be created.
        force (bool):
            If the destination table already exists and this flag is
            ``TRUE``, the table will be overwritten by the contents of
            assets snapshot. If the flag is ``FALSE`` or unset and the
            destination table already exists, the export call returns an
            INVALID_ARGUMEMT error.
        partition_spec (google.cloud.asset_v1.types.PartitionSpec):
            [partition_spec] determines whether to export to partitioned
            table(s) and how to partition the data.

            If [partition_spec] is unset or
            [partition_spec.partition_key] is unset or
            ``PARTITION_KEY_UNSPECIFIED``, the snapshot results will be
            exported to non-partitioned table(s). [force] will decide
            whether to overwrite existing table(s).

            If [partition_spec] is specified. First, the snapshot
            results will be written to partitioned table(s) with two
            additional timestamp columns, readTime and requestTime, one
            of which will be the partition key. Secondly, in the case
            when any destination table already exists, it will first try
            to update existing table's schema as necessary by appending
            additional columns. Then, if [force] is ``TRUE``, the
            corresponding partition will be overwritten by the snapshot
            results (data in different partitions will remain intact);
            if [force] is unset or ``FALSE``, it will append the data.
            An error will be returned if the schema update or data
            appension fails.
        separate_tables_per_asset_type (bool):
            If this flag is ``TRUE``, the snapshot results will be
            written to one or multiple tables, each of which contains
            results of one asset type. The [force] and [partition_spec]
            fields will apply to each of them.

            Field [table] will be concatenated with "*" and the asset
            type names (see
            https://cloud.google.com/asset-inventory/docs/supported-asset-types
            for supported asset types) to construct per-asset-type table
            names, in which all non-alphanumeric characters like "." and
            "/" will be substituted by "*". Example: if field [table] is
            "mytable" and snapshot results contain
            "storage.googleapis.com/Bucket" assets, the corresponding
            table name will be "mytable_storage_googleapis_com_Bucket".
            If any of these tables does not exist, a new table with the
            concatenated name will be created.

            When [content_type] in the ExportAssetsRequest is
            ``RESOURCE``, the schema of each table will include
            RECORD-type columns mapped to the nested fields in the
            Asset.resource.data field of that asset type (up to the 15
            nested level BigQuery supports
            (https://cloud.google.com/bigquery/docs/nested-repeated#limitations)).
            The fields in >15 nested levels will be stored in JSON
            format string as a child column of its parent RECORD column.

            If error occurs when exporting to any table, the whole
            export call will return an error but the export results that
            already succeed will persist. Example: if exporting to
            table_type_A succeeds when exporting to table_type_B fails
            during one export call, the results in table_type_A will
            persist and there will not be partial results persisting in
            a table.
    """

    dataset = proto.Field(
        proto.STRING,
        number=1,
    )
    table = proto.Field(
        proto.STRING,
        number=2,
    )
    force = proto.Field(
        proto.BOOL,
        number=3,
    )
    partition_spec = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PartitionSpec",
    )
    separate_tables_per_asset_type = proto.Field(
        proto.BOOL,
        number=5,
    )


class PartitionSpec(proto.Message):
    r"""Specifications of BigQuery partitioned table as export
    destination.

    Attributes:
        partition_key (google.cloud.asset_v1.types.PartitionSpec.PartitionKey):
            The partition key for BigQuery partitioned
            table.
    """

    class PartitionKey(proto.Enum):
        r"""This enum is used to determine the partition key column when
        exporting assets to BigQuery partitioned table(s). Note that, if the
        partition key is a timestamp column, the actual partition is based
        on its date value (expressed in UTC. see details in
        https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables).
        """
        PARTITION_KEY_UNSPECIFIED = 0
        READ_TIME = 1
        REQUEST_TIME = 2

    partition_key = proto.Field(
        proto.ENUM,
        number=1,
        enum=PartitionKey,
    )


class PubsubDestination(proto.Message):
    r"""A Pub/Sub destination.

    Attributes:
        topic (str):
            The name of the Pub/Sub topic to publish to. Example:
            ``projects/PROJECT_ID/topics/TOPIC_ID``.
    """

    topic = proto.Field(
        proto.STRING,
        number=1,
    )


class FeedOutputConfig(proto.Message):
    r"""Output configuration for asset feed destination.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub_destination (google.cloud.asset_v1.types.PubsubDestination):
            Destination on Pub/Sub.

            This field is a member of `oneof`_ ``destination``.
    """

    pubsub_destination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="PubsubDestination",
    )


class Feed(proto.Message):
    r"""An asset feed used to export asset updates to a destinations.
    An asset feed filter controls what updates are exported. The
    asset feed must be created within a project, organization, or
    folder. Supported destinations are:
    Pub/Sub topics.

    Attributes:
        name (str):
            Required. The format will be
            projects/{project_number}/feeds/{client-assigned_feed_identifier}
            or
            folders/{folder_number}/feeds/{client-assigned_feed_identifier}
            or
            organizations/{organization_number}/feeds/{client-assigned_feed_identifier}

            The client-assigned feed identifier must be unique within
            the parent project/folder/organization.
        asset_names (Sequence[str]):
            A list of the full names of the assets to receive updates.
            You must specify either or both of asset_names and
            asset_types. Only asset updates matching specified
            asset_names or asset_types are exported to the feed.
            Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            For a list of the full names for supported asset types, see
            `Resource name
            format </asset-inventory/docs/resource-name-format>`__.
        asset_types (Sequence[str]):
            A list of types of the assets to receive updates. You must
            specify either or both of asset_names and asset_types. Only
            asset updates matching specified asset_names or asset_types
            are exported to the feed. Example:
            ``"compute.googleapis.com/Disk"``

            For a list of all supported asset types, see `Supported
            asset
            types </asset-inventory/docs/supported-asset-types>`__.
        content_type (google.cloud.asset_v1.types.ContentType):
            Asset content type. If not specified, no
            content but the asset name and type will be
            returned.
        feed_output_config (google.cloud.asset_v1.types.FeedOutputConfig):
            Required. Feed output configuration defining
            where the asset updates are published to.
        condition (google.type.expr_pb2.Expr):
            A condition which determines whether an asset update should
            be published. If specified, an asset will be returned only
            when the expression evaluates to true. When set,
            ``expression`` field in the ``Expr`` must be a valid [CEL
            expression] (https://github.com/google/cel-spec) on a
            TemporalAsset with name ``temporal_asset``. Example: a Feed
            with expression ("temporal_asset.deleted == true") will only
            publish Asset deletions. Other fields of ``Expr`` are
            optional.

            See our `user
            guide <https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition>`__
            for detailed instructions.
        relationship_types (Sequence[str]):
            A list of relationship types to output, for example:
            ``INSTANCE_TO_INSTANCEGROUP``. This field should only be
            specified if content_type=RELATIONSHIP.

            -  If specified: it outputs specified relationship updates
               on the [asset_names] or the [asset_types]. It returns an
               error if any of the [relationship_types] doesn't belong
               to the supported relationship types of the [asset_names]
               or [asset_types], or any of the [asset_names] or the
               [asset_types] doesn't belong to the source types of the
               [relationship_types].
            -  Otherwise: it outputs the supported relationships of the
               types of [asset_names] and [asset_types] or returns an
               error if any of the [asset_names] or the [asset_types]
               has no replationship support. See `Introduction to Cloud
               Asset
               Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
               for all supported asset types and relationship types.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_names = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    asset_types = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    content_type = proto.Field(
        proto.ENUM,
        number=4,
        enum="ContentType",
    )
    feed_output_config = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FeedOutputConfig",
    )
    condition = proto.Field(
        proto.MESSAGE,
        number=6,
        message=expr_pb2.Expr,
    )
    relationship_types = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class IamPolicyAnalysisQuery(proto.Message):
    r"""IAM policy analysis query message.

    Attributes:
        scope (str):
            Required. The relative name of the root asset. Only
            resources and IAM policies within the scope will be
            analyzed.

            This can only be an organization number (such as
            "organizations/123"), a folder number (such as
            "folders/123"), a project ID (such as
            "projects/my-project-id"), or a project number (such as
            "projects/12345").

            To know how to get organization id, visit
            `here <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.

            To know how to get folder or project id, visit
            `here <https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects>`__.
        resource_selector (google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ResourceSelector):
            Optional. Specifies a resource for analysis.
        identity_selector (google.cloud.asset_v1.types.IamPolicyAnalysisQuery.IdentitySelector):
            Optional. Specifies an identity for analysis.
        access_selector (google.cloud.asset_v1.types.IamPolicyAnalysisQuery.AccessSelector):
            Optional. Specifies roles or permissions for
            analysis. This is optional.
        options (google.cloud.asset_v1.types.IamPolicyAnalysisQuery.Options):
            Optional. The query options.
        condition_context (google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ConditionContext):
            Optional. The hypothetical context for IAM
            conditions evaluation.
    """

    class ResourceSelector(proto.Message):
        r"""Specifies the resource to analyze for access policies, which
        may be set directly on the resource, or on ancestors such as
        organizations, folders or projects.

        Attributes:
            full_resource_name (str):
                Required. The [full resource name]
                (https://cloud.google.com/asset-inventory/docs/resource-name-format)
                of a resource of `supported resource
                types <https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types>`__.
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
                Required. The identity appear in the form of principals in
                `IAM policy
                binding <https://cloud.google.com/iam/reference/rest/v1/Binding>`__.

                The examples of supported forms are:
                "user:mike@example.com", "group:admins@example.com",
                "domain:google.com",
                "serviceAccount:my-project-id@appspot.gserviceaccount.com".

                Notice that wildcard characters (such as \* and ?) are not
                supported. You must give a specific identity.
        """

        identity = proto.Field(
            proto.STRING,
            number=1,
        )

    class AccessSelector(proto.Message):
        r"""Specifies roles and/or permissions to analyze, to determine
        both the identities possessing them and the resources they
        control. If multiple values are specified, results will include
        roles or permissions matching any of them. The total number of
        roles and permissions should be equal or less than 10.

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

    class Options(proto.Message):
        r"""Contains query options.

        Attributes:
            expand_groups (bool):
                Optional. If true, the identities section of the result will
                expand any Google groups appearing in an IAM policy binding.

                If
                [IamPolicyAnalysisQuery.identity_selector][google.cloud.asset.v1.IamPolicyAnalysisQuery.identity_selector]
                is specified, the identity in the result will be determined
                by the selector, and this flag is not allowed to set.

                If true, the default max expansion per group is 1000 for
                AssetService.AnalyzeIamPolicy][].

                Default is false.
            expand_roles (bool):
                Optional. If true, the access section of result will expand
                any roles appearing in IAM policy bindings to include their
                permissions.

                If
                [IamPolicyAnalysisQuery.access_selector][google.cloud.asset.v1.IamPolicyAnalysisQuery.access_selector]
                is specified, the access section of the result will be
                determined by the selector, and this flag is not allowed to
                set.

                Default is false.
            expand_resources (bool):
                Optional. If true and
                [IamPolicyAnalysisQuery.resource_selector][google.cloud.asset.v1.IamPolicyAnalysisQuery.resource_selector]
                is not specified, the resource section of the result will
                expand any resource attached to an IAM policy to include
                resources lower in the resource hierarchy.

                For example, if the request analyzes for which resources
                user A has permission P, and the results include an IAM
                policy with P on a GCP folder, the results will also include
                resources in that folder with permission P.

                If true and
                [IamPolicyAnalysisQuery.resource_selector][google.cloud.asset.v1.IamPolicyAnalysisQuery.resource_selector]
                is specified, the resource section of the result will expand
                the specified resource to include resources lower in the
                resource hierarchy. Only project or lower resources are
                supported. Folder and organization resource cannot be used
                together with this option.

                For example, if the request analyzes for which users have
                permission P on a GCP project with this option enabled, the
                results will include all users who have permission P on that
                project or any lower resource.

                If true, the default max expansion per resource is 1000 for
                AssetService.AnalyzeIamPolicy][] and 100000 for
                AssetService.AnalyzeIamPolicyLongrunning][].

                Default is false.
            output_resource_edges (bool):
                Optional. If true, the result will output the
                relevant parent/child relationships between
                resources. Default is false.
            output_group_edges (bool):
                Optional. If true, the result will output the
                relevant membership relationships between groups
                and other groups, and between groups and
                principals. Default is false.
            analyze_service_account_impersonation (bool):
                Optional. If true, the response will include access analysis
                from identities to resources via service account
                impersonation. This is a very expensive operation, because
                many derived queries will be executed. We highly recommend
                you use
                [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning]
                rpc instead.

                For example, if the request analyzes for which resources
                user A has permission P, and there's an IAM policy states
                user A has iam.serviceAccounts.getAccessToken permission to
                a service account SA, and there's another IAM policy states
                service account SA has permission P to a GCP folder F, then
                user A potentially has access to the GCP folder F. And those
                advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Another example, if the request analyzes for who has
                permission P to a GCP folder F, and there's an IAM policy
                states user A has iam.serviceAccounts.actAs permission to a
                service account SA, and there's another IAM policy states
                service account SA has permission P to the GCP folder F,
                then user A potentially has access to the GCP folder F. And
                those advanced analysis results will be included in
                [AnalyzeIamPolicyResponse.service_account_impersonation_analysis][google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis].

                Only the following permissions are considered in this
                analysis:

                -  ``iam.serviceAccounts.actAs``
                -  ``iam.serviceAccounts.signBlob``
                -  ``iam.serviceAccounts.signJwt``
                -  ``iam.serviceAccounts.getAccessToken``
                -  ``iam.serviceAccounts.getOpenIdToken``
                -  ``iam.serviceAccounts.implicitDelegation``

                Default is false.
        """

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

    class ConditionContext(proto.Message):
        r"""The IAM conditions context.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            access_time (google.protobuf.timestamp_pb2.Timestamp):
                The hypothetical access timestamp to evaluate IAM
                conditions. Note that this value must not be earlier than
                the current time; otherwise, an INVALID_ARGUMENT error will
                be returned.

                This field is a member of `oneof`_ ``TimeContext``.
        """

        access_time = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="TimeContext",
            message=timestamp_pb2.Timestamp,
        )

    scope = proto.Field(
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
    options = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Options,
    )
    condition_context = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ConditionContext,
    )


class IamPolicyAnalysisOutputConfig(proto.Message):
    r"""Output configuration for export IAM policy analysis
    destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.GcsDestination):
            Destination on Cloud Storage.

            This field is a member of `oneof`_ ``destination``.
        bigquery_destination (google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.BigQueryDestination):
            Destination on BigQuery.

            This field is a member of `oneof`_ ``destination``.
    """

    class GcsDestination(proto.Message):
        r"""A Cloud Storage location.

        Attributes:
            uri (str):
                Required. The uri of the Cloud Storage object. It's the same
                uri that is used by gsutil. Example:
                "gs://bucket_name/object_name". See `Viewing and Editing
                Object
                Metadata <https://cloud.google.com/storage/docs/viewing-editing-metadata>`__
                for more information.

                If the specified Cloud Storage object already exists and
                there is no
                `hold <https://cloud.google.com/storage/docs/object-holds>`__,
                it will be overwritten with the analysis result.
        """

        uri = proto.Field(
            proto.STRING,
            number=1,
        )

    class BigQueryDestination(proto.Message):
        r"""A BigQuery destination.

        Attributes:
            dataset (str):
                Required. The BigQuery dataset in format
                "projects/projectId/datasets/datasetId", to which the
                analysis results should be exported. If this dataset does
                not exist, the export call will return an INVALID_ARGUMENT
                error.
            table_prefix (str):
                Required. The prefix of the BigQuery tables to which the
                analysis results will be written. Tables will be created
                based on this table_prefix if not exist:

                -  <table_prefix>_analysis table will contain export
                   operation's metadata.
                -  <table_prefix>_analysis_result will contain all the
                   [IamPolicyAnalysisResult][google.cloud.asset.v1.IamPolicyAnalysisResult].
                   When [partition_key] is specified, both tables will be
                   partitioned based on the [partition_key].
            partition_key (google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey):
                The partition key for BigQuery partitioned
                table.
            write_disposition (str):
                Optional. Specifies the action that occurs if the
                destination table or partition already exists. The following
                values are supported:

                -  WRITE_TRUNCATE: If the table or partition already exists,
                   BigQuery overwrites the entire table or all the
                   partitions data.
                -  WRITE_APPEND: If the table or partition already exists,
                   BigQuery appends the data to the table or the latest
                   partition.
                -  WRITE_EMPTY: If the table already exists and contains
                   data, an error is returned.

                The default value is WRITE_APPEND. Each action is atomic and
                only occurs if BigQuery is able to complete the job
                successfully. Details are at
                https://cloud.google.com/bigquery/docs/loading-data-local#appending_to_or_overwriting_a_table_using_a_local_file.
        """

        class PartitionKey(proto.Enum):
            r"""This enum determines the partition key column for the
            bigquery tables. Partitioning can improve query performance and
            reduce query cost by filtering partitions. Refer to
            https://cloud.google.com/bigquery/docs/partitioned-tables for
            details.
            """
            PARTITION_KEY_UNSPECIFIED = 0
            REQUEST_TIME = 1

        dataset = proto.Field(
            proto.STRING,
            number=1,
        )
        table_prefix = proto.Field(
            proto.STRING,
            number=2,
        )
        partition_key = proto.Field(
            proto.ENUM,
            number=3,
            enum="IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey",
        )
        write_disposition = proto.Field(
            proto.STRING,
            number=4,
        )

    gcs_destination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message=GcsDestination,
    )
    bigquery_destination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message=BigQueryDestination,
    )


class SavedQuery(proto.Message):
    r"""A saved query which can be shared with others or used later.

    Attributes:
        name (str):
            The resource name of the saved query. The format must be:

            -  projects/project_number/savedQueries/saved_query_id
            -  folders/folder_number/savedQueries/saved_query_id
            -  organizations/organization_number/savedQueries/saved_query_id
        description (str):
            The description of this saved query. This
            value should be fewer than 255 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of this saved
            query.
        creator (str):
            Output only. The account's email address who
            has created this saved query.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of this
            saved query.
        last_updater (str):
            Output only. The account's email address who
            has updated this saved query most recently.
        labels (Mapping[str, str]):
            Labels applied on the resource.
            This value should not contain more than 10
            entries. The key and value of each entry must be
            non-empty and fewer than 64 characters.
        content (google.cloud.asset_v1.types.SavedQuery.QueryContent):
            The query content.
    """

    class QueryContent(proto.Message):
        r"""The query content.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            iam_policy_analysis_query (google.cloud.asset_v1.types.IamPolicyAnalysisQuery):
                An IAM Policy Analysis query, which could be used in the
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy]
                rpc or the
                [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning]
                rpc.

                This field is a member of `oneof`_ ``query_content``.
        """

        iam_policy_analysis_query = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="query_content",
            message="IamPolicyAnalysisQuery",
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    creator = proto.Field(
        proto.STRING,
        number=4,
    )
    last_update_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_updater = proto.Field(
        proto.STRING,
        number=6,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    content = proto.Field(
        proto.MESSAGE,
        number=8,
        message=QueryContent,
    )


class MoveAnalysis(proto.Message):
    r"""A message to group the analysis information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            The user friendly display name of the
            analysis. E.g. IAM, Organization Policy etc.
        analysis (google.cloud.asset_v1.types.MoveAnalysisResult):
            Analysis result of moving the target
            resource.

            This field is a member of `oneof`_ ``result``.
        error (google.rpc.status_pb2.Status):
            Description of error encountered when
            performing the analysis.

            This field is a member of `oneof`_ ``result``.
    """

    display_name = proto.Field(
        proto.STRING,
        number=1,
    )
    analysis = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="result",
        message="MoveAnalysisResult",
    )
    error = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=status_pb2.Status,
    )


class MoveAnalysisResult(proto.Message):
    r"""An analysis result including blockers and warnings.

    Attributes:
        blockers (Sequence[google.cloud.asset_v1.types.MoveImpact]):
            Blocking information that would prevent the
            target resource from moving to the specified
            destination at runtime.
        warnings (Sequence[google.cloud.asset_v1.types.MoveImpact]):
            Warning information indicating that moving
            the target resource to the specified destination
            might be unsafe. This can include important
            policy information and configuration changes,
            but will not block moves at runtime.
    """

    blockers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MoveImpact",
    )
    warnings = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MoveImpact",
    )


class MoveImpact(proto.Message):
    r"""A message to group impacts of moving the target resource.

    Attributes:
        detail (str):
            User friendly impact detail in a free form
            message.
    """

    detail = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
