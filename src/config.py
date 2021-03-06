# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_python_tutorial_ffmpeg.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME = ''
_BATCH_ACCOUNT_KEY = ''
_BATCH_ACCOUNT_URL = ''
_STORAGE_ACCOUNT_NAME = ''
_STORAGE_ACCOUNT_KEY = ''
_INPUT_BLOB_PREFIX = '' # E.g. if files in container/READS/ then put 'READS'. Keep blank if files are directly in container and not in a sub-directory
_INPUT_CONTAINER = ''
_OUTPUT_CONTAINER = ''
_POOL_ID = ''
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 1
_POOL_VM_SIZE = 'STANDARD_D64_v3'
_JOB_ID = ''
