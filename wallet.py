class Wallet:
  def __init__(self):
    self.b = 10
    
  def depositMoney(self, money):
    self.b = money
  
  def queryMoney(self):
    return self.b
  
  def withdrawal(self, money):
    print('Test')
    if self.b >= money:
      self.b -= money
      return 'Done'
    return 'Low Balance'
