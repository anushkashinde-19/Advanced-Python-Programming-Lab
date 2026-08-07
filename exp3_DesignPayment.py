from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
        
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Paypal")
        
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")
        
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy=strategy
        
    def set_strategy(self,strategy):
        self.strategy=strategy
        
    def process_payment(self, amount):
        self.strategy.pay(amount)
    
processor= PaymentProcessor(CreditCardPayment())
processor.process_payment(10000)

processor.set_strategy(PayPalPayment())
processor.process_payment(20000)

processor.set_strategy(BitcoinPayment())
processor.process_payment(30000)                       