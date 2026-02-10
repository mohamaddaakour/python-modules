from abc import ABC, abstractmethod

class PaymentMethod(ABC):

	# abstract method will be implemented later by a child of this class

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCard(PaymentMethod):

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using PayPal")


payment1 = CreditCard()
payment2 = PayPal()

payment1.pay(100)
payment2.pay(50)

# process_payment(payment1, 100)
# process_payment(payment2, 50)

# output:
# Paid $100 using Credit Card
# Paid $50 using PayPal
