# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014 Midokura PTE LTD.
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
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

import logging
import sys

from midonetclient.httpclient import HttpClient

LOG = logging.getLogger(__name__)


class MediaType(object):

    APP = "application/vnd.org.midonet.Application-v3+json"
    NEUTRON = "application/vnd.org.midonet.neutron.Neutron-v1+json"
    NETWORK = "application/vnd.org.midonet.neutron.Network-v1+json"
    NETWORKS = "application/vnd.org.midonet.neutron.collection.Network-v1+json"


class UrlProvider(object):

    def __init__(self):
        self.app = None
        self.neutron = None
        self.cache = {}

    def _get_application(self):
        if self.app is None:
            self.app = self.client.get(self.base_uri, MediaType.APP)
        return self.app

    def _get_neutron(self):
        if self.neutron is None:
            app = self._get_application()
            self.neutron = self.client.get(app["neutron"], MediaType.NEUTRON)
        return self.neutron

    def network_url(self, id):
        return self._get_neutron()["network_template"].replace("{id}", id)

    def networks_url(self):
        return self._get_neutron()["networks"]


class MidonetClient(UrlProvider):

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri
        self.client = HttpClient(base_uri, username, password,
                                 project_id=project_id)
        super(MidonetClient, self).__init__()

    def create_network(self, network):
        LOG.info("create_network %r", network)
        return self.client.post(self.networks_url(), MediaType.NETWORK,
                                body=network)

    def delete_network(self, id):
        LOG.info("delete_network %r", id)
        self.client.delete(self.network_url(id))

    def get_network(self, id):
        LOG.info("get_network %r", id)
        return self.client.get(self.network_url(id), MediaType.NETWORK)

    def list_networks(self):
        LOG.info("list_networks")
        return self.client.get(self.networks_url(), MediaType.NETWORKS)

    def update_network(self, id, network):
        LOG.info("update_network %r", network)
        self.client.put(self.network_url(id), MediaType.NETWORK, network)
