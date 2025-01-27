# -*- coding: utf-8 -*-

# from datetime import datetime
from .errors import (ArgumentError, AuthenticationError, BadGatewayError,
                     BadRequestError, HttpError, IntercomError,
                     MultipleMatchingContactsError, MultipleMatchingUsersError,
                     RateLimitExceeded, ResourceNotFound, ServerError,
                     ServiceUnavailableError, TokenUnauthorizedError,
                     UnexpectedError)

__version__ = '4.0.1'


RELATED_DOCS_TEXT = "See https://github.com/jkeyes/python-intercom \
for usage examples."
COMPATIBILITY_WARNING_TEXT = f"It looks like you are upgrading from \
an older version of python-intercom. Please note that this new version \
({__version__}) is not backwards compatible."
COMPATIBILITY_WORKAROUND_TEXT = "To get rid of this error please set \
Intercom.app_api_key and don't set Intercom.api_key."
CONFIGURATION_REQUIRED_TEXT = "You must set both Intercom.app_id and \
Intercom.app_api_key to use this client."
