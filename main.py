import sys

import pandas as pd

import datacol
from ib.ext.Contract import Contract


def main():
  symbol = sys.argv[1]
  exch = sys.argv[2]
  expiry = sys.argv[3]
  date = sys.argv[4]
  d = pd.to_datetime(date) - pd.DateOffset(1)
  prev_date = '%04d%02d%02d' % (d.year, d.month, d.day)

  contract = Contract()
  contract.m_symbol = symbol
  contract.m_secType = 'FUT'
  contract.m_exchange = exch
  contract.m_currency = 'USD'
  contract.m_expiry = expiry
  print 'Collecting', date, 'data for', contract.m_symbol, 'expiration', contract.m_expiry

  outfile = open(date+'.bars', 'w')

  for h in xrange(20,24,2):
    broker = datacol.Datacol(contract, prev_date, ('%02d:00:00' % h), 7200, outfile)
    broker.close()

  for h in xrange(0,18,2):
    broker = datacol.Datacol(contract, date, ('%02d:00:00' % h), 7200, outfile)
    broker.close()

  broker = datacol.Datacol(contract, date, '17:15:00', 4500, outfile)
  broker.close()

  outfile.close()


if __name__ == "__main__":
  main()
