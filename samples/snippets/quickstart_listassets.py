#!/usr/bin/env python

# Copyright 2020 Google LLC.
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


import argparse


def list_assets(project_id, asset_types, page_size):
    # [START asset_quickstart_list_assets]
    from google.cloud import asset_v1p5beta1
    from google.cloud.asset_v1p5beta1 import enums

    # TODO project_id = 'Your Google Cloud Project ID'
    # TODO asset_types = 'Your asset type list, e.g.,
    # ["storage.googleapis.com/Bucket","bigquery.googleapis.com/Table"]'
    # TODO page_size = 'Num of assets in one page, which must be between 1 and
    # 1000 (both inclusively)'

    project_resource = 'projects/{}'.format(project_id)
    content_type = enums.ContentType.RESOURCE
    client = asset_v1p5beta1.AssetServiceClient()

    # Call ListAssets v1p5beta1 to list assets.
    response = client.list_assets(
        parent=project_resource, read_time=None, asset_types=asset_types,
        content_type=content_type, page_size=page_size)

    for page in response.pages:
        for asset in page:
            print(asset)
    # [END asset_quickstart_list_assets]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('project_id', help='Your Google Cloud project ID')
    parser.add_argument(
        'asset_types',
        help='The types of the assets to list, comma delimited, e.g., '
        'storage.googleapis.com/Bucket')
    parser.add_argument(
        'page_size',
        help='Num of assets in one page, which must be between 1 and 1000 '
        '(both inclusively)')

    args = parser.parse_args()

    asset_type_list = args.asset_types.split(',')

    list_assets(args.project_id, asset_type_list, int(args.page_size))
