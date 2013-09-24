"""
Copyright 2013 Rackspace, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import structlog
import twisted

CONFIGURED_LOGGING = False


def configure():
    """
    Configure logging subsystem.
    """
    global CONFIGURED_LOGGING

    if CONFIGURED_LOGGING:
        return

    CONFIGURED_LOGGING = True

    twisted.python.log.startLogging(sys.stderr)
    structlog.configure(
        context_class=dict,
        cache_logger_on_first_use=True)


def get_logger():
    """
    Get a logger instance.
    """
    return structlog.get_logger()
