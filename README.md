# arm-vnet-generator

ARM template for generating a vnet with a local gateway that has routes back
to a supernet that contains the vnet.

Sample parameters file would create a vnet hub with CIDR 10.1.0.0/24 that
allows attaching other vnets in the range 10.1.0.0/20.  The local gateway
includes all routes for 10/8 except 10.1.0.0/20.

cidr_subtract.py is a small tool for calculating the CIDR routes for local
gateways.
