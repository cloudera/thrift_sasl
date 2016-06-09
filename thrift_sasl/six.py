# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

import sys


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


if PY2:
  from cStringIO import StringIO
  from thrift.transport.TTransport import (
    TTransportException, TTransportBase, CReadableTransport)

  is_open_compat = lambda trans: trans.isOpen()
  read_all_compat = lambda trans, sz: trans.readAll(sz)


if PY3:
  # TODO: consider contributing this to thriftpy instead
  class CReadableTransport(object):
    @property
    def cstringio_buf(self):
      pass
    def cstringio_refill(self, partialread, reqlen):
      pass

  # TODO: make this more explicit for maintainability sake
  from io import BytesIO as StringIO
  from thriftpy.transport import TTransportException, TTransportBase, readall

  def is_open_compat(trans):
    try:
      is_open = trans.is_open()
    except AttributeError:
      is_open = trans.isOpen()
    return is_open

  read_all_compat = lambda trans, sz: readall(trans.read, sz)
