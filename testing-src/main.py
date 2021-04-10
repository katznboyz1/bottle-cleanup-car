print('STARTUP: STARTING')

import time

MAX_SPEED_VALUE = 1
MIN_SPEED_VALUE = 0
MAX_SPEEDTIME_TIMEOUT = 2 # the timeout in seconds for the speedtime file (ex: if this is 1, then after 1 second of no updates, then the speedtime file is deemed invalid)

ERROR_CODES = {
    1: 'MAX_SPEED_VALUE is less than MIN_SPEED_VALUE',
    2: 'Speed status expired', # meaning that the last logged time in ./.speedtime is more than the limit for speed updates, meaning that possibly something has gone wrong with the program and it is no longer responding
}

# returns [bool status, int[] errors]
def sanityCheck() -> list:

    # if true, then it passed, if false, then it failed
    checkPassed = True
    # each index is an integer that contains the error code for the failures that happened
    checkErrors = []

    if (MAX_SPEED_VALUE < MIN_SPEED_VALUE):
        checkErrors.append(1)
    if (float(open('.speedtime').read()) <= time.time() - MAX_SPEEDTIME_TIMEOUT):
        checkErrors.append(2)

    return [
        (len(checkErrors) <= 0),
        checkErrors
    ]

print('STARTUP: CONDUCTING SANITY CHECK')
initialSanityCheckResults = sanityCheck()
print('STARTUP: SANITY CHECK RESULTS:')

if (initialSanityCheckResults[0]):
    print('STARTUP: SANITY CHECK PASSED')

else:
    for each in initialSanityCheckResults[1]:
        print('STARTUP: SANITY CHECK ERROR "{}"'.format(ERROR_CODES[each]))
    print('STARTUP: CONTINUING WITH STARTUP - SANITY CHECK ERRORS SHOULD BE CORRECTED BY THE MONITORING THREAD, OR ELSE THE PROGRAM WILL KILL ITSELF')
    exit()