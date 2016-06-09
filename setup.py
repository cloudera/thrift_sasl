# Copyright 2015 Cloudera Inc.
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

from __future__ import absolute_import

import sys

from setuptools import setup


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


description = ("Thrift SASL Python module that implements SASL transports for "
               "Thrift (`TSaslClientTransport`).")
requirements = ['sasl>=0.2.1']

if PY2:
    requirements.append('thrift')
if PY3:
    # Apache Thrift does not yet support Python 3 (see THRIFT-1857).  We use
    # thriftpy as a stopgap replacement
    requirements.append('thriftpy')


setup(
    name='thrift_sasl',
    version='0.2.1',
    description=description,
    long_description=description,
    author='Uri Laserson',
    author_email='laserson@cloudera.com',
    maintainer='Wes McKinney',
    maintainer_email='wes@cloudera.com',
    url='https://github.com/cloudera/thrift_sasl',
    install_requires=requirements,
    packages=['thrift_sasl'],
    keywords='thrift sasl transport',
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4']
)
