# 10，银行卡类（BankCard）有余额（balance）属性和存款（deposit）取款（draw）的方法，
# 只要取款金额小于余额即可完成取款操作
# 信用卡类（CreditCard）继承自银行卡类，信用卡多了透支额度（overdraft）属性，
# 如果卡中余额和透支额度的和大于取款金额即可完成取款。如果透支，显示透支金额

class BankCard():
    def __init__(self,balance,is_CreditCard = False):
        self.balance = balance
        self.is_CreditCard = is_CreditCard

    def deposit(self,amount):
        self.balance += amount
        print(f'已存款：{amount},当前余额：{self.balance}')

    def draw(self,amount):
        if self.is_CreditCard == False:
            print(self.balance)
            if amount <= self.balance:
                self.balance -= amount
                print(f'已取款{amount},当前余额：{self.balance}')
            else:
                print('余额不足')

        elif self.is_CreditCard == True:
            if amount <= self.balance:
                self.balance -= amount
                print(f'已取款{amount},当前余额：{self.balance},当前透支金额：{self.overdraft_amount}')
            elif amount > self.balance and amount < self.overdraft:
                owe = amount - self.balance
                self.balance = 0
                self.overdraft_amount += owe
                self.overdraft -= owe
                print(f'已取款{amount},当前余额：{self.balance},当前透支金额：{self.overdraft_amount}')
            else:
                print('余额和透支金额都不足')


class CreditCard(BankCard):
    def __init__(self,balance,overdraft):
        super().__init__(balance,is_CreditCard=True)
        self.overdraft = overdraft
        #super().__init__(self)
        self.overdraft_amount = 0


cardtype = input('请选1：择储蓄卡，2：信用卡')
if int(cardtype) == 1:
    card = BankCard(1000)
    while True:
        data = input('请选1：存钱，2：取钱')
        if int(data) == 1:
            data = input('请输入金额')
            card.deposit(int(data))
        elif int(data) == 2:
            data = input('请输入金额')
            card.draw(int(data))
elif int(cardtype) == 2:
    ccard = CreditCard(1000, 5000)
    while True:
        data = input('请选1：存钱，2：取钱')
        if int(data) == 1:
            data = input('请输入金额')
            ccard.deposit(int(data))
        elif int(data) == 2:
            data = input('请输入金额')
            ccard.draw(int(data))




