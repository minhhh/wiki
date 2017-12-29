## Helper

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*: #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

01: # make a simple request
	curl http://httpbin.org

02: # make POST , DELETE request
	curl -X POST http://httpbin.org/post
	curl -X DELETE http://httpbin.org/delete

03: # set request header
	curl -H "Authorization: OAuth 2c4419d1aabeec" http://httpbin.org/headers
	curl -H "Accept: application/json" \
		-H "Authorization: OAuth 2c3455d1aeffc" \
		http://httpbin.org/headers

04: # send request body
	curl -X PUT -H 'Content-Type: application/json' \
		-d '{"firstName":"Kris", "lastName":"Jordan"}' http://httpbin.org/put

05: # use file as request body
	curl -X PUT -H 'Content-Type: application/json' \
		-d @example.json http://httpbin.org/put

06: # post html form data
	curl -d "firstName=Kris" \
		-d "lastName=Jordan" \
		http://httpbin.org/post

07: # post html multipart / file forms
	curl -F "firstName=Kris" \
		-F "publicKey=@idrsa.pub;type=text/plain" \
		http://httpbin.org/post

08: # test virtual host avoid DNS
	curl -H "Host: google.com" 216.58.221.46

09: # View Response Headers
	curl -i http://httpbin.org
	curl -I http://httpbin.org # view only header

httpie-01: # make a simple request
	http http://httpbin.org

httpie-02: # make POST , DELETE request
	http POST http://httpbin.org/post
	http DELETE http://httpbin.org/delete

httpie-03: # set request header
	http http://httpbin.org/headers Authorization:"OAuth 2c4419d1aabeec"
	http http://httpbin.org/headers "Accept: application/json" "Authorization: OAuth 2c3455d1aeffc"

httpie-04: # send request body as json
	http PUT http://httpbin.org/put 'Content-Type: application/json' name=John email=john@example.org
	http POST http://httpbin.org/post 'Content-Type: application/json' name=John email=john@example.org
	printf '{"firstName":"Kris", "lastName":"Jordan"}' | http PUT http://httpbin.org/put 'Content-Type: application/json'

httpie-05: # use file as request body
	http PUT http://httpbin.org/put @example.json
	http PUT http://httpbin.org/put 'Content-Type: application/json' @example.json

httpie-06: # post html form data
	http -f http://httpbin.org/post firstName="Kris" lastName="Jordan"

httpie-07: # post html multipart / file forms
	http -f http://httpbin.org/post firstName="Kris" publicKey@idrsa.pub
	# http POST http://httpbin.org/post firstName="Kris" publicKey@idrsa.pub
	# Cannot post json data and upload file at the same time

httpie-08: # test virtual host avoid DNS
	http 216.58.221.46 'Host: google.com'

