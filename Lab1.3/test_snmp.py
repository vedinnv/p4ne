from pysnmp.hlapi import *

snmp_var_version = ObjectIdentity('SNMPv2-MIB','sysDescr',0)

result = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(('10.31.70.107', 161)), ContextData(), ObjectType(snmp_var_version))

for r in result:
    for s in r[3]:
        print(s)

snmp_var_version_next= ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
result_next = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(('10.31.70.107', 161)), ContextData(), ObjectType(snmp_var_version_next), lexicographicMode=False)

for r in result_next:
    for s in r[3]:
        print(s)

