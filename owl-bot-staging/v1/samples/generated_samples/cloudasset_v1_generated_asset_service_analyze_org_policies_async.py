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
# Generated code. DO NOT EDIT!
#
# Snippet for AnalyzeOrgPolicies
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-asset


# [START cloudasset_v1_generated_AssetService_AnalyzeOrgPolicies_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import asset_v1


async def sample_analyze_org_policies():
    # Create a client
    client = asset_v1.AssetServiceAsyncClient()

    # Initialize request argument(s)
    request = asset_v1.AnalyzeOrgPoliciesRequest(
        scope="scope_value",
        constraint="constraint_value",
    )

    # Make the request
    page_result = client.analyze_org_policies(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END cloudasset_v1_generated_AssetService_AnalyzeOrgPolicies_async]
