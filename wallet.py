class Wallet:
  def __init__(self):
    self.balance = 0
   
  def depositMoney(self, money):
    self.balance = money
  
  def queryMoney(self):
    return self.balance
  
  def withdrawal(self, money):
    print('Test')
    if self.balance >= money:
      self.balance -= money
      return 'Done'
    return 'Low Balance'
