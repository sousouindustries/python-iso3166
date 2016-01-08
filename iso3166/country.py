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
from iso3166.const import ISO3166_MAP


class ISO3166(object):
    """Represents an ISO 3166 data element."""

    @property
    def alpha2(self):
        return self._alpha2

    @property
    def numeric3(self):
        return self._numeric3

    @classmethod
    def fromcode(cls, code):
        return cls(**ISO3166_MAP[code])\
            if not isinstance(code, cls)\
            else code

    def __init__(self, name, alpha2, alpha3, numeric3, fips):
        self._name = name
        self._alpha2 = alpha2
        self._alpha3 = alpha3
        self._numeric3 = numeric3
        self._fips = fips

    def __int__(self):
        return int(self._numeric3)

    def __str__(self):
        return self._name

    def __repr__(self):
        return "ISO3166(name={0}, alpha2={1}, alpha3={2}, numeric3={3})".format(
            repr(self._name),
            repr(self._alpha2),
            repr(self._alpha3),
            repr(self._numeric3)
        )
