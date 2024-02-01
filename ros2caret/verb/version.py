# Copyright 2021 Research Institute of Systems Planning, Inc.
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

from ros2caret.verb import VerbExtension

import os.path
import codecs
import re


class CaretVersionVerb(VerbExtension):

    def main(self, *, args):
        version_path = '../../setup.py'
        version = self.get_version(version_path)
        print('v' + version)

    def read(self,rel_path):
        here_path = os.path.dirname(os.path.realpath(__file__))
        with codecs.open(os.path.join(here_path, rel_path), 'r') as fp:
            return fp.read()

    def get_version(self,rel_path):
        version_pattern = re.compile(r"\s*version=\'\d+\.\d+\.\d\'")
        for line in self.read(rel_path).splitlines():
            match = version_pattern.search(line)
            if match:
                st = match.group(0).split('=')
                return st[1][1:-1]
        else:
            raise RuntimeError("Unable to find version string.")
