# ib_data_loader
A python script to download daily futures market data (5 sec bars) from Interactive Brokers using IbPy.

Usage: python main.py symbol exchange expiry date

symbol   - ES, NQ, CL, NG, GC, etc.

exchange - GLOBEX (for ES, NQ) or NYMEX (for commodity futures)

expiry   - YYYYMM format (e.g., 201506)

date     - YYYYMMDD format (e.g., 20150428)

Saves 5 sec bar data as a text file date.bars

The columns are:

timestamp, open, high, low, close, volume, count, WAP, hasGaps

!! This software is provided AS IS. NO WARRANTY is expressed or implied. !!
