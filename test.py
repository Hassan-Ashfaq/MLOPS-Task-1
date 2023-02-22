from wallet import Wallet

def test_getAmount():
  a = Wallet()
  a.depositMoney(1000)
  assert a.queryMoney()==1000
  
def test_getAmount_2():
  a = Wallet()
  a.depositMoney(100)
  assert a.queryMoney()==100
  
def test_removeAmount_pass():
  a = Wallet()
  a.depositMoney(1000)
  assert a.withdrawal(100)=='Done'

def test_removeAmount_low():
  a = Wallet()
  a.depositMoney(1000)
  assert a.withdrawal(2000)=='Low Balance'
