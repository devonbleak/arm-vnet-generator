#!/usr/bin/env python

import netaddr


def cidr_subtract(supernet_cidr, subnet_cidr):
    supernet = netaddr.IPNetwork(supernet_cidr)
    subnet = netaddr.IPNetwork(subnet_cidr)

    if subnet not in supernet:
        return [supernet]

    supernet_subnets = list(supernet.subnet(subnet.prefixlen))
    supernet_subnets.remove(subnet)

    return netaddr.cidr_merge(supernet_subnets)


def main():
    import argparse
    import json

    parser = argparse.ArgumentParser(description='return the set of CIDR '
                                     'blocks from supernet minus the subnet '
                                     'CIDR block')

    parser.add_argument('supernet_cidr', help='CIDR block of the supernet')
    parser.add_argument('subnet_cidr', help='CIDR block of the subnet')

    args = parser.parse_args()

    print json.dumps([str(net) for net in cidr_subtract(args.supernet_cidr, args.subnet_cidr)], indent=4)



if __name__ == '__main__':
    main()
