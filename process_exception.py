# Copyright 2019 Novartis Institutes for BioMedical Research Inc. Licensed
# under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0. Unless
# required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

class ProcessException(Exception):
    def __init__(self, message, stdout, stderr, http_status):
        Exception.__init__(self)
        self.message = message
        self.stdout = stdout
        self.stderr = stderr
        self.http_status = http_status

    @classmethod
    def from_pid_object(cls, pid_object):
        return cls(
            pid_object.message,
            pid_object.all_output,
            pid_object.stderr,
            pid_object.http_status,
        )