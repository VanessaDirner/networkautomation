import os
from ping3 import ping

print("why isn't this printing")

try:
    pings = ping('10.1.1.1')
    print("pinging", pings)
except:
    print("unknown error")