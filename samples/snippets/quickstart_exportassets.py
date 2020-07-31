#!/usr/bin/env python

# Copyright 2018 Google LLC.
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


def export_assets(project_id, dump_file_path):
    # [START asset_quickstart_export_assets]
    from google.cloud import asset_v1
    from google.cloud.asset_v1.proto import asset_service_pb2

    # TODO project_id = 'Your Google Cloud Project ID'
    # TODO dump_file_path = 'Your asset dump file path'

    client = asset_v1.AssetServiceClient()
    parent = client.project_path(project_id)
    output_config = asset_service_pb2.OutputConfig()
    output_config.gcs_destination.uri = dump_file_path
    response = client.export_assets(parent, output_config)
    print(response.result())
    # [END asset_quickstart_export_assets]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('project_id', help='Your Google Cloud project ID')
    parser.add_argument(
        'dump_file_path',
        help='The file ExportAssets API will dump assets to, '
        'e.g.: gs://<bucket-name>/asset_dump_file')

    args = parser.parse_args()

    export_assets(args.project_id, args.dump_file_path)
