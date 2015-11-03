# DAEMONS
* [Unix and Linux startup scripts, Part 1](http://aplawrence.com/Basics/unix-startup-scripts-1.html)
* Things to remember:
    * Copy your bashscript to `/etc/init.d`
    * Use `chkconfig`. The bashscript should be of the correct format for chkconfig to work.
    * Sample script

```bash
    #!/bin/bash
    #
    # startsvn        Startup script for OSQA scgi
    #
    # chkconfig: - 85 15
    # description: Description
    # processname: startscgi
    /opt/ActivePython-2.6/bin/python /opt/OSQA/django-scgi.py --projects=/opt/OSQA/ --settings=settings --host=localhost --port=8080 --maxspare=5 --maxchildren=5 --daemon
```
<br/>

* [xinetd](http://www.cyberciti.biz/faq/linux-how-do-i-configure-xinetd-service/)
* [Becoming a daemon](https://www.youtube.com/watch?v=qMyj0Yujb8k)

## Daemontools
* [Manage your services with Daemontools](http://isotope11.com/blog/manage-your-services-with-daemontools)
* [daemontools](http://thedjbway.b0llix.net/daemontools.html)
* [Daemontools: Tutorial](http://blog.teksol.info/pages/daemontools/tutorial)
* [Daemontools: Best Practices](http://blog.teksol.info/pages/daemontools/best-practices.html)

