#!/usr/bin/env python
import time
import socket
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server
from cmd import Calico

PORT_NUMBER = 9200

class CalicoCollector(object):

  def __init__(self):
    self.host = socket.gethostname()
    self.local_ip = socket.gethostbyname(self.host)
    self.calico_obj = Calico()

  def collect(self):

    calico_ipam_data = GaugeMetricFamily("calico_ipam", "Total available IP count")
    free_ipam = self.calico_obj.get_free_ipam()
    calico_ipam_data.add_metric(free_ipam)

    yield calico_ipam_data

if __name__ == '__main__':
    start_http_server(PORT_NUMBER)
    registry = REGISTRY.register(CalicoCollector())
    while True:
      time.sleep(1)

