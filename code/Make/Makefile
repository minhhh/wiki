## Helper
define HELP_multiline
To use Make multiline, we can use the same trick that is used\n\
to create this help
endef
export HELP_multiline

define HELP_use_password
To use password or personal stuff. define it in your environment\n\
and use it in the Makefile. For example this will output your PASSWORD
endef
export HELP_use_password

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:[0-9a-zA-Z\-]* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

all:multiline-text #
	@echo

multiline-text: #
	@echo $$HELP_multiline

use-password: # Use password with Make
	@echo $$HELP_use_password
	@echo "Your password is \"$(PASSWORD)\""


