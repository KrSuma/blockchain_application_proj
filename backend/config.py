NANOSECONDS = 1
MICROSECONDS = 1000 * NANOSECONDS
MILLISECONDS = 1000 * MICROSECONDS
SECONDS = 1000 * MILLISECONDS

MINE_RATE = 4 * SECONDS

"""
MINE_RATE is the time set for consistent mining rate of new blocks.

comparison is as follows:
if a new block was created within the MINE_RATE, then the difficulty to mine a new block is increased.
Else, the difficulty is decreased to dynamically adjust the new block mining rate to make the creation of 
new blocks consistent. 
"""