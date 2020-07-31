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

import os

import quickstart_searchalliampolicies

PROJECT = os.environ['GOOGLE_CLOUD_PROJECT']


def test_search_all_iam_policies(capsys):
    scope = "projects/{}".format(PROJECT)
    query = "policy:roles/owner"
    quickstart_searchalliampolicies.search_all_iam_policies(scope, query=query)
    out, _ = capsys.readouterr()
    assert "roles/owner" in out
