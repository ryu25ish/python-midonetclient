# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Midokura PTE LTD.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Tomoe Sugihara <tomoe@midokura.com>, Midokura
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

from resource_base import ResourceBase
import vendor_media_type


class HostInterfacePort(ResourceBase):

    media_type = vendor_media_type.APPLICATION_HOST_INTERFACE_PORT_JSON

    def __init__(self, uri, dto, auth):
        super(HostInterfacePort, self).__init__(uri, dto, auth)

    def get_host_id(self):
        return self.dto['hostId']

    def get_interface_name(self):
        return self.dto['interfaceName']

    def get_port_id(self):
        return self.dto['portId']

    def port_id(self, port_id):
        self.dto['portId'] = port_id
        return self

    def interface_name(self, name):
        self.dto['interfaceName'] = name
        return self
