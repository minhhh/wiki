## API Design

http://www.infoq.com/research/api-management?utm_source=infoqresearch&utm_campaign=rr-content
http://www.programmableweb.com/news/how-to-maximize-developer-adoption/analysis/2014/11/17

* Credibility: “If a developer doesn’t believe you, then good luck getting them to use your product.”
* Support: “Developers are looking for signs of support. Something at some point is going to go wrong, so developers want to know they can solve their problems quickly.”
* Success: “Look to share details about how your API can help them achieve something. A lot of companies don’t have that understanding that providing an API is going to create a win for both of you.”

### Best practices

http://www.cutter.com/content-and-analysis/resource-centers/agile-project-management/sample-our-research/apmu1306.html

- Documentation - current, accurate, easy, guide/tutorial/directed (management tool generated)
- SDKs/Samples in developer preferred languages
- Any SDK is just libraries to access REST/SOAP API, nothing more. Potentially an impediment to simply making use of the straight API.
- Direct access (no SDK required)
  - e.g., through Postman or curl (say, curl -L http://127.0.0.1:4001/v2/keys/message-XPUT -d value=“Hello world”)
- Simple SDK (programmatic API over REST/SOAP etc) requirements - straightforward install and use
- Free/Freemium use for developers
- Instant API keys
- Simple sandbox to try things out for developers
- Before API available, establish API landing page on web to discover interest and potential user types

http://www.programmableweb.com/news/developer-experience-dx-key-to-successful-api/analysis/2014/06/05

- Management - availability, documentation, meta-data
- Ecosystem - hackathons/hackdays (see how well apis work…identify new uses)
- RESTful approaches much more successful than XML/SOAP - mobile big driver
- Monitoring - who is using it (to improve it), who's using what version

[How to design intuitive RESTful JSON APIs](https://www.youtube.com/watch?v=hdSrT4yjS1g) - Les Hazlewood, CTO of Stormpath and PMC of Apache Shiro

- Catalogs (e.g., API Commons, ProgrammableWeb, documentation etc)
- Service descriptions (discover and understand the capabilities of the service)
- Swagger, API Blueprint or RAML
- [Usage limits](http://www.programmableweb.com//news/companies-revisit-api-usage-limits-markets-change/analysis/2014/07/23)


## API Versioning
  - What does version refer to? When break client. Approach is to never break client (within major version). So if “major” change, redesign, aimed at humans
  - Two schools of thought on versions:
    - Clean breaks; within version backward/forward compatibility
      * means have to support a number of interface permutations - range on service x range on client
    - Any breaking change
      * means have many versions, and clients have to pick or accept range
      * "Late last year, Facebook announced its move to an API versioning model. Facebook has now adopted a versioning and migration strategy for its Marketing API. The approach allows app builders to roll out changes over time. Breaking changes are rolled into a newer version, which allows multiple versions of an API to exist at the same time with different functionality in each version. Under the versioning scheme, developers can better manage when to migrate to a newer version." [Facebook versioning strategy](http://www.programmableweb.com/news/facebook-applies-versioning-strategy-to-marketing-api)
  - Caching - want different versions cached differently
  - Number or name? No correlation between versions - may as well be name as they are clean breaks, so not guaranteed to be backward compatible...
  - Representation format - backward compatible, must-ignore
  - Resource format - keep backward compatible - need forward compatible if advance producer (must-ignore)
  - Testing - how to test all the client-service interfaces?
  - Internal vs External - not much difference in practice - don’t want to introduce internal dependencies

  * Three approaches to specifying API version in request
    * Request (URL) - semantically messy (implies version refers to version of object)
      * Amazon, NetFlix is ?v=xx.xx, or ?version=xx.xx
      * in URI (e.g., /v1/)
    * Custom request header - duplicates accept header function
    * Accept header - hard to test - can't just click on link or type URL

### Use cases - loose coupling of versions
[W3C Versioning](http://www.w3.org/2001/tag/doc/versioning) - forward, backward...

  * Consumer backward compatibility
    * Consumer upgrades (or give API version)
    * Producer downgrades - e.g., rollback
  * Consumer forward compatibility
    * Producer upgrades (or continue to support earlier versions)
    * Support a given range of clients
     * Forward compatibility (handle incomprehensible sections of response)
       * //Must Ignore// pattern
       * Assume don't change semantics, just add or subtract

### Compatibility
From client perspective: API is backward compatible if client can continue through service changes; forward compatible if client can be changed without needing service change.

Need both forward and backward on producer (service). Backward so can upgrade service without breaking consumers; forward so that consumers can work against older producers (different deployment states; rollbacks).

No interaction between services - except through endpoints. So can ignore interface permutations between services - each is independent.

Assume clients written to particular set of APIs - that understood at time-of-writing. Defined by test results, not by versions. If work then should continue to work within that major version. Implies that rather than explicit versioning, implicit versioning by parameters (same name = same semantics), and service endpoints, and backwards compatibility.
