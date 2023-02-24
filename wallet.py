class Wallet:
  balance=0
  def setBalance(self,i):
    self.balance=i
  def getBalance(self):
    return self.balance
  def removeBalance(self,i):
    self.balance=self.balance-i
