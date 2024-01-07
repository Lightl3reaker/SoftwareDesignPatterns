class PaymentStrategy:
    def pay(self,amount):
        pass
class Kpay(PaymentStrategy):
    def pay(self,amount):
        self.amount=amount
        print(f"Paid {self.amount}$ with KBZpay.")

class Wavepay(PaymentStrategy):
    def pay(self,amount):
        self.amount=amount
        print(f"Paid {self.amount}$ with Wavemoney.")

class Ayapay(PaymentStrategy):
    def pay(self,amount):
        self.amount=amount
        print(f"Paid {self.amount}$ with Ayapay.")

class ShoppingCart:
    def __init__(self,payment):
        self.payment=payment
    def checkout(self,amount):
        self.payment.pay(amount)

KPay=Kpay()
WavePay=Wavepay()
AyaPay=Ayapay()

x=int(input("How would you like to checkout--> 1 for Kpay, 2 for Wavepay and 3 for Ayapay:"))
y=int(input("Amount:"))
match(x):
    case 1:
        cart=ShoppingCart(KPay)
        cart.checkout(y)
    case 2:
        cart=ShoppingCart(WavePay)
        cart.checkout(y)
    case 3:
        cart=ShoppingCart(AyaPay)
        cart.checkout(y)








