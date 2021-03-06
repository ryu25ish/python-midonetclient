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

import port_type
import vendor_media_type
import resource_base


class BridgePort(resource_base.ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORT_JSON

    def __init__(self, uri, dto, auth):
        super(BridgePort, self).__init__(uri, dto, auth)

    def get_id(self):
        return self.dto['id']

    def get_type(self):
        return self.dto['type']

    def get_device_id(self):
        return self.dto['deviceId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def get_vif_id(self):
        return self.dto['vifId']

    def get_peer_id(self):
        return self.dto['peerId']

    def inbound_filter_id(self, id_):
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_):
        self.dto['outboundFilterId'] = id_
        return self

    def vif_id(self, id_):
        self.dto['vifId'] = id_
        return self

    def link(self, peer_uuid):
        self.dto['peerId'] = peer_uuid
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self._do_request(self.dto['link'], 'POST', self.dto, headers=headers)

        self.get()
        return self

    def unlink(self):
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self._do_request(self.dto['link'], 'DELETE')
        self.get()
        return self
