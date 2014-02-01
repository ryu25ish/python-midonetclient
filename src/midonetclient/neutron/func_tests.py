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
import uuid

from midonetclient.neutron.client import MidonetClient


logging.basicConfig(format="%(asctime)-15s %(name)s %(message)s")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


def test_network_crud(client):
    net_id = str(uuid.uuid4())
    net = {"id": net_id,
           "name": net_id + "name",
           "tenant_id": "foo",
           "admin_state_up:": True}
    net = client.create_network(net)
    assert net_id == net["id"]

    net["admin_state_up"] = False
    client.update_network(net_id, net)

    net = client.get_network(net_id)
    assert net["admin_state_up"] is False

    client.delete_network(net_id)


def main():

    if len(sys.argv) < 4:
        print >> sys.stderr, "Functional testing "
        print >> sys.stderr, "Usage: " + sys.argv[0] \
            + " <URI> <username> <password> [project_id]"
        sys.exit(-1)

    uri = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    if len(sys.argv) > 4:
        project_id = sys.argv[4]
    else:
        project_id = None

    client = MidonetClient(uri, username, password, project_id=project_id)
    test_network_crud(client)


if __name__ == "__main__":
    main()
