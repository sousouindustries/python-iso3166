# COPYRIGHT 2015-2016 Sousou Industries
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from os.path import abspath
from os.path import dirname
from os.path import join
import json


ISO3166_MAP = {}
for element in json.load(open(abspath(join(dirname(__file__), 'iso3166.json')))):
    ISO3166_MAP[element.get('alpha2')] = element
    ISO3166_MAP[element.get('alpha3')] = element
    ISO3166_MAP[element.get('numeric3')] = element
