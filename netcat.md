# NETCAT CHEATSHEET
`netcat` is a very useful tool for testing/debugging TCP/IP and UDP networking. In this cheetsheet I am sharing some useful examples of netcat usage for everyday purpose.

## Test if a particular TCP/UDP port is open
To check if a TCP port is open
```bash
    nc -v google.com 80
    # Connection to google.com port 80 [tcp/http] succeeded!
```

To check if a UDP port is open, simple add option `-u`
```bash
    nc -vu google.com 53
    # Connection to google.com port 53 [udp/domain] succeeded!
```

## Port scan
Scan UDP ports
```bash
    nc -vzu google.com 1-65535
```

To scan TCP ports simply remove the `-u`
```bash
    nc -vz google.com 1-65535
```

## Netcat client server
Open a server that listens to a particular port
```bash
    nc -l 2389
```

Open another client connecting to that port
```bash
    nc localhost 2389
```

Now you can (insecurely) chat between the 2 terminals.

## Transfer single file
On the remote server, open a port which output anything it receives to the target file
```bash
    nc -l 2389 > test
```

On the local host, send the file
```bash
    cat testfile | nc remotehost 2389
```

## Transfer whole directory
On receiver host
```bash
    nc -l 5000 | tar xvf -
```

On sender host
```bash
    tar cvf - /path/to/dir | nc remotehost.com 5000
```

## Transfer whole harddrive
On receiver host
```bash
    nc -lp 5000 | sudo dd of=/backup/sdb.img.gz
```

On sender host
```bash
    dd if=/dev/sdb | gzip -c | nc remote_server.com 5000
```

## Create a web proxy for a particular websites
The following commands redirect all incoming TCP/5000 connections to `http://www.google.com`
```bash
    mkfifo proxypipe
    while true; do nc -l 5000 0<proxypipe | nc www.google.com 80 1> proxypipe; done
```

## Launch a remote shell
On remote host
```bash
    nc -lp 5000 -e /bin/bash
```

On localhost host
```bash
    nc remotehost 5000
```

## Test network speed
* [Using netcat to test network speed][using_netcat_to_test_network_speed]




# REFERENCES
* [useful_netcat_examples_on_linux]
* [netcat_the_admin_best_friend]
* [using_netcat_to_test_network_speed]

[practical_linux_netcat_nc_command_examples]: http://www.thegeekstuff.com/2012/04/nc-command-examples/
[useful_netcat_examples_on_linux]: http://xmodulo.com/useful-netcat-examples-linux.html
[netcat_the_admin_best_friend]: http://www.admin-magazine.com/Articles/Netcat-The-Admin-s-Best-Friend
[using_netcat_to_test_network_speed]: http://deice.daug.net/netcat_speed.html
