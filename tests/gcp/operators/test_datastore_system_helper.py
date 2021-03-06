#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import os

from tests.contrib.utils.logging_command_executor import LoggingCommandExecutor

BUCKET = os.environ.get("GCP_DATASTORE_BUCKET", "datastore-system-test")


class GcpDatastoreSystemTestHelper(LoggingCommandExecutor):
    def create_bucket(self):
        self.execute_cmd(
            [
                "gsutil",
                "mb",
                "-l",
                "europe-north1",
                "gs://{bucket}".format(bucket=BUCKET),
            ]
        )

    def delete_bucket(self):
        self.execute_cmd(["gsutil", "rm", "-r", "gs://{bucket}".format(bucket=BUCKET)])
