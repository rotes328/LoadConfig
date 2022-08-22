Simple Config Loader

This is a simple configuration loader that will connect to a device by the IP specified in the hostip variable
with username in the environment variable "CiscoUser" and the password in the environment variable "CiscoPassword".
This script uses IOS-XE configuration.

In this example, a BGP configuration is loaded, a timer waits for BGP to come up, and then the BGP summary is
displayed. Lines 27-29 can be modified or commented out for other configuration validation.