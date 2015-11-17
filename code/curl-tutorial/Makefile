## Helper

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*: #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

01: # make a simple request
	curl http://echo.httpkit.com

02: # make POST , DELETE request
	curl -X POST echo.httpkit.com
	curl -X DELETE echo.httpkit.com

03: # set request header
	curl -H "Authorization: OAuth 2c4419d1aabeec" http://echo.httpkit.com
	curl -H "Accept: application/json" \
		-H "Authorization: OAuth 2c3455d1aeffc" \
		http://echo.httpkit.com

04: # send request body
	curl -X PUT -H 'Content-Type: application/json' \
		-d '{"firstName":"Kris", "lastName":"Jordan"}' echo.httpkit.com

05: # use file as request body
	curl -X PUT -H 'Content-Type: application/json' \
		-d @example.json echo.httpkit.com

06: # post html form data
	curl -d "firstName=Kris" \
		-d "lastName=Jordan" \
		echo.httpkit.com

07: # post html multipart / file forms
	curl -F "firstName=Kris" \
		-F "publicKey=@idrsa.pub;type=text/plain" \
		echo.httpkit.com

08: # test virtual host avoid DNS
	curl -H "Host: google.com" 216.58.221.46

09: # View Response Headers
	curl -i echo.httpkit.com
	curl -I echo.httpkit.com # view only header

httpie-01: # make a simple request
	http echo.httpkit.com

httpie-02: # make POST , DELETE request
	http POST echo.httpkit.com
	http DELETE echo.httpkit.com

httpie-03: # set request header
	http http://echo.httpkit.com Authorization:"OAuth 2c4419d1aabeec"
	http http://echo.httpkit.com "Accept: application/json" "Authorization: OAuth 2c3455d1aeffc"

httpie-04: # send request body as json
	http PUT echo.httpkit.com 'Content-Type: application/json' name=John email=john@example.org
	printf '{"firstName":"Kris", "lastName":"Jordan"}' | http PUT echo.httpkit.com 'Content-Type: application/json'

httpie-05: # use file as request body
	http PUT echo.httpkit.com 'Content-Type: application/json' @example.json

httpie-06: # post html form data
	http -f echo.httpkit.com firstName="Kris" lastName="Jordan"

httpie-07: # post html multipart / file forms
	http -f echo.httpkit.com firstName="Kris" publicKey@idrsa.pub

httpie-08: # test virtual host avoid DNS
	http 216.58.221.46 'Host: google.com'

httpie-09: # View Response Headers
	http echo.httpkit.com
