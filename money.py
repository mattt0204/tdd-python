from abc import ABC


class Expression(ABC):
    pass


class Money(Expression):
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency: str = currency

    @staticmethod
    def dollor(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    @property
    def currency(self):
        return self._currency

    def __eq__(self, __o: object):
        return self._amount == __o._amount and self.currency == __o.currency

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"

    def times(self, multiplier):
        return Money(self._amount * multiplier, self.currency)

    def __add__(self, __o: object) -> Expression:
        return Sum(self, __o)


class Bank:
    def reduce(self, source: Money, to: str):
        return Money.dollor(10)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    pass


if __name__ == "__main__":
    five_dollor = Money(5, "USD")
    five_franc = Money(5, "CHF")

    print(five_dollor.__class__.__name__)
