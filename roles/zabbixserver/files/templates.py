#!/usr/bin/python
from pyzabbix import ZabbixAPI, ZabbixAPIException
import pprint, glob

zapi = ZabbixAPI("http://zabbix/zabbix")
zapi.login("Admin", "zabbix")
print "Connected to Zabbix API Version %s" % zapi.api_version()
host = zapi.host.get(output='extend',
  #                  hostid = '10120',
                    )
#pprint.pprint (host)
rules = {'templates':{'createMissing':'true','updateExisting':'true'},
        'discoveryRules':{'createMissing':'true','updateExisting':'true'},
        'graphs':{'createMissing':'true','updateExisting':'true'},
        'groups':{'createMissing':'true'},
        'hosts':{'createMissing':'true','updateExisting':'true'},
        'images':{'createMissing':'true','updateExisting':'true'},
        'items':{'createMissing':'true','updateExisting':'true'},
        'maps': {'createMissing':'true','updateExisting':'true'},
        'screens':{'createMissing':'true','updateExisting':'true'},
        'templateLinkage':{'createMissing':'true','updateExisting':'true'},
        'templates':{'createMissing':'true','updateExisting':'true'},
        'templateScreens':{'createMissing':'true','updateExisting':'true'},
        'triggers':{'createMissing':'true','updateExisting':'true'}
}
src = './*.xml'
list_src = glob.glob(src)

for h in list_src:
    with open(h, 'r') as f:
        template = f.read()
        try:
            zapi.confimport('xml', template, rules)
        except ZabbixAPIException as err:
            print err

