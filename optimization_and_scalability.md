# SCALABILITY
* [Web application performance and scalability](http://www.webforefront.com/performance/) INCREDIBLE articles about all the fundamental concepts and practical solutions for web application performance and scalability.

**[Scalable Web Architecture and Distributed Systems](http://aosabook.org/en/distsys.html)**

* [The performance of opensource application](http://aosabook.org/en/index.html)

* [Scaling a High Traffic Web Application: Our Journey from Java to PHP](https://www.youtube.com/watch?v=oS1D1W6eTwg)
    * Think about scaling before
    * Devil is in the detail
    * Complexity: Magic, pattern, overly complex object model
    * Database
        * ORM is the problem
        * Developer must understand how database work
        * ORM is hard to scale
        * Scaling DB is a understood problem
    * Sessions
        * 2 choices to scale
        * Session replication: does not scale very much. chatty on the network
        * Sticky session
            * Work but becareful
    * Cache
        * If you need to cache for performance reason, you need to look at your architecture again
    * Guiding Architectural Principles
        * Initial deployment on 3 machines
        * Servers must be stateless
        * The database owns all the data
        * Caching has to be an explicit choice
        * Use the right tool for the job
        * Minimize complexity
    * PHP Downsides
        * Error detection and reporting is a must
        * Coding standards are a must
            * Naming is super important

* TODO [Best Practices for Scaling Web Apps](https://www.youtube.com/watch?v=tQ2V9QSv48M)
    * load balancer
    * db cluster

* TODO [Building and scaling web applications](http://www.youtube.com/watch?v=2Lq3ACxfLGc)

* TODO [One Million Clicks per Minute with Kafka and Clojure - Devon Peticolas](https://www.youtube.com/watch?v=VC_MTD68erY)

* [Comparison between framework](http://www.techempower.com/benchmarks/#section=data-r6&hw=i7&test=json) - Interesting benchmark of different web technology.

* [The Secret to 10 Million Concurrent Connections](http://highscalability.com/blog/2013/5/13/the-secret-to-10-million-concurrent-connections-the-kernel-i.html)

* [12 Million Concurrent Connections with MigratoryData WebSocket Server](http://mrotaru.wordpress.com/2013/06/20/12-million-concurrent-connections-with-migratorydata-websocket-server/)

* [A Million Connections...and Beyond! - Node.js at Scale](https://www.youtube.com/watch?v=AH7kw8sKefg)

* [How We've Scaled Dropbox](https://www.youtube.com/watch?v=PE4gwstWhmc)

* [1000000 daily users and no cache](http://www.infoq.com/presentations/1000000-Daily-Users-and-No-Cache) provides great insides into a real development environment of several games at Wooga. Through their experiences struggling to achieve a large number of users, we learn how to optimize app server, database, using new/faster technology to scale our game up.

* [C10K](http://www.kegel.com/c10k.html#strategies)




# PERFORMANCE OPTIMIZATION
* [How to Speed up a Python Program](https://www.youtube.com/watch?v=e08kOj2kISU)

* [cpu caches and why you care](https://www.youtube.com/watch?v=WDIkqP4JbkE)

* [Understanding CPU caching and performance](http://arstechnica.com/gadgets/2002/07/caching/1/)

* [How to write performance benchmark code](https://github.com/spion/async-compare/tree/blog)

* [Optimizing optimizing: some insights that led to a 400% speedup of PowerDNS](https://hackernoon.com/optimizing-optimizing-some-insights-that-led-to-a-400-speedup-of-powerdns-5e1a44b58f1c#.rx648ea3z)




# WEBSERVER OPTIMIZATION
* [Web Application Metrics](http://docs.oracle.com/cd/E24628_01/em.121/e25162/website.htm)

* [Web Site Acceleration](http://www.seoconsultants.com/articles/1000/server-performance) Study how to optimize web server performance with affordable, easy, unobtrusive software. 3 strategies: Code Optimization, Cache Control, and HTTP Compression

## Web cache
* [Caching Tutorial](https://www.mnot.net/cache_docs/), [other link](http://www.web-caching.com/mnot_tutorial/how.html)
* [Web cache in mobile](http://www2.research.att.com/~sen/pub/Caching_mobisys12.pdf)
* There are two ways
    * Use the Expire headers (somewhat limited)
    * Use Cache-Control HTTP headers

## Performance benchmarks: apache benchmark http perf httpperf
* [weighttp](http://redmine.lighttpd.net/projects/weighttp/wiki)
    * Weighttp is by far the best stress tool we know today: it uses the clean AB interface and works reasonably well. It could be made even faster by using leaner code, but there are not many serious coders investing their time to write decent client tools, it seems.
* [Howto: Performance Benchmarks a Webserver](http://www.cyberciti.biz/tips/howto-performance-benchmarks-a-web-server.html)
* [ApacheBench & HTTPerf](http://gwan.com/en_apachebench_httperf.html)
    * HTTPPerf seems not very realiable. DONT use it.
