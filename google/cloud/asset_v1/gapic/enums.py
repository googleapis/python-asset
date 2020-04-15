# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class ContentType(enum.IntEnum):
    """
    Asset content type.

    Attributes:
      CONTENT_TYPE_UNSPECIFIED (int): Unspecified content type.
      RESOURCE (int): Resource metadata.
      IAM_POLICY (int): The actual IAM policy set on a resource.
      ORG_POLICY (int): The Cloud Organization Policy set on an asset.
      ACCESS_POLICY (int): The Cloud Access context mananger Policy set on an asset.
    """

    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2
    ORG_POLICY = 4
    ACCESS_POLICY = 5


class DeviceEncryptionStatus(enum.IntEnum):
    """
    The encryption state of the device.

    Attributes:
      ENCRYPTION_UNSPECIFIED (int): The encryption status of the device is not specified or not known.
      ENCRYPTION_UNSUPPORTED (int): The device does not support encryption.
      UNENCRYPTED (int): The device supports encryption, but is currently unencrypted.
      ENCRYPTED (int): The device is encrypted.
    """

    ENCRYPTION_UNSPECIFIED = 0
    ENCRYPTION_UNSUPPORTED = 1
    UNENCRYPTED = 2
    ENCRYPTED = 3


class DeviceManagementLevel(enum.IntEnum):
    """
    The degree to which the device is managed by the Cloud organization.

    Attributes:
      MANAGEMENT_UNSPECIFIED (int): The device's management level is not specified or not known.
      NONE (int): The device is not managed.
      BASIC (int): Basic management is enabled, which is generally limited to monitoring and
      wiping the corporate account.
      COMPLETE (int): Complete device management. This includes more thorough monitoring and the
      ability to directly manage the device (such as remote wiping). This can be
      enabled through the Android Enterprise Platform.
    """

    MANAGEMENT_UNSPECIFIED = 0
    NONE = 1
    BASIC = 2
    COMPLETE = 3


class NullValue(enum.IntEnum):
    """
    A time window specified by its "start_time" and "end_time".

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class OsType(enum.IntEnum):
    """
    The operating system type of the device.
    Next id: 7

    Attributes:
      OS_UNSPECIFIED (int): The operating system of the device is not specified or not known.
      DESKTOP_MAC (int): A desktop Mac operating system.
      DESKTOP_WINDOWS (int): A desktop Windows operating system.
      DESKTOP_LINUX (int): A desktop Linux operating system.
      DESKTOP_CHROME_OS (int): A desktop ChromeOS operating system.
      ANDROID (int): An Android operating system.
      IOS (int): An iOS operating system.
    """

    OS_UNSPECIFIED = 0
    DESKTOP_MAC = 1
    DESKTOP_WINDOWS = 2
    DESKTOP_LINUX = 3
    DESKTOP_CHROME_OS = 6
    ANDROID = 4
    IOS = 5


class BasicLevel(object):
    class ConditionCombiningFunction(enum.IntEnum):
        """
        Starts asynchronous cancellation on a long-running operation. The
        server makes a best effort to cancel the operation, but success is not
        guaranteed. If the server doesn't support this method, it returns
        ``google.rpc.Code.UNIMPLEMENTED``. Clients can use
        ``Operations.GetOperation`` or other methods to check whether the
        cancellation succeeded or whether the operation completed despite
        cancellation. On successful cancellation, the operation is not deleted;
        instead, it becomes an operation with an ``Operation.error`` value with
        a ``google.rpc.Status.code`` of 1, corresponding to ``Code.CANCELLED``.

        Attributes:
          AND (int): Represents a repeated ``Value``.
          OR (int): Optional. The relative resource name pattern associated with this
          resource type. The DNS prefix of the full resource name shouldn't be
          specified here.

          The path pattern must follow the syntax, which aligns with HTTP binding
          syntax:

          ::

              Template = Segment { "/" Segment } ;
              Segment = LITERAL | Variable ;
              Variable = "{" LITERAL "}" ;

          Examples:

          ::

              - "projects/{project}/topics/{topic}"
              - "projects/{project}/knowledgeBases/{knowledge_base}"

          The components in braces correspond to the IDs for each resource in the
          hierarchy. It is expected that, if multiple patterns are provided, the
          same component name (e.g. "project") refers to IDs of the same type of
          resource.
        """

        AND = 0
        OR = 1


class Policy(object):
    class ListPolicy(object):
        class AllValues(enum.IntEnum):
            """
            Additional HTTP bindings for the selector. Nested bindings must not
            contain an ``additional_bindings`` field themselves (that is, the
            nesting may only be one level deep).

            Attributes:
              ALL_VALUES_UNSPECIFIED (int): A URL/resource name that uniquely identifies the type of the
              serialized protocol buffer message. This string must contain at least
              one "/" character. The last segment of the URL's path must represent the
              fully qualified name of the type (as in
              ``path/google.protobuf.Duration``). The name should be in a canonical
              form (e.g., leading "." is not accepted).

              In practice, teams usually precompile into the binary all types that
              they expect it to use in the context of Any. However, for URLs which use
              the scheme ``http``, ``https``, or no scheme, one can optionally set up
              a type server that maps type URLs to message definitions as follows:

              -  If no scheme is provided, ``https`` is assumed.
              -  An HTTP GET on the URL must yield a ``google.protobuf.Type`` value in
                 binary format, or produce an error.
              -  Applications are allowed to cache lookup results based on the URL, or
                 have them precompiled into a binary to avoid any lookup. Therefore,
                 binary compatibility needs to be preserved on changes to types. (Use
                 versioned type names to manage breaking changes.)

              Note: this functionality is not currently available in the official
              protobuf release, and it is not used for type URLs beginning with
              type.googleapis.com.

              Schemes other than ``http``, ``https`` (or the empty scheme) might be
              used with implementation specific semantics.
              ALLOW (int): A policy with this set allows all values.
              DENY (int): A policy with this set denies all values.
            """

            ALL_VALUES_UNSPECIFIED = 0
            ALLOW = 1
            DENY = 2


class ServicePerimeter(object):
    class PerimeterType(enum.IntEnum):
        """
        Specifies the type of the Perimeter. There are two types: regular and
        bridge. Regular Service Perimeter contains resources, access levels, and
        restricted services. Every resource can be in at most ONE
        regular Service Perimeter.

        In addition to being in a regular service perimeter, a resource can also
        be in zero or more perimeter bridges.  A perimeter bridge only contains
        resources.  Cross project operations are permitted if all effected
        resources share some perimeter (whether bridge or regular). Perimeter
        Bridge does not contain access levels or services: those are governed
        entirely by the regular perimeter that resource is in.

        Perimeter Bridges are typically useful when building more complex toplogies
        with many independent perimeters that need to share some data with a common
        perimeter, but should not be able to share data among themselves.

        Attributes:
          PERIMETER_TYPE_REGULAR (int): Regular Perimeter.
          PERIMETER_TYPE_BRIDGE (int): Perimeter Bridge.
        """

        PERIMETER_TYPE_REGULAR = 0
        PERIMETER_TYPE_BRIDGE = 1
