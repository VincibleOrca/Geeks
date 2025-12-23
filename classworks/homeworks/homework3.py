from abc import ABC, abstractmethod



class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.__discount = 0

    def get_price(self):

        return self._price * (1 - self.__discount / 100)

    def set_discount(self, percent):

        if percent <= 50:
            self.__discount = percent
        else:
            raise ValueError("Ошибка: Скидка не может превышать 50%")

    def apply_extra_discount(self, secret_code):

        if secret_code == "VIP123":

            discounted_price = self.get_price()

            self._price = discounted_price * 0.95

            self.__discount = 0
        else:
            print("Неверный код")



class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")
        return True

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")
        return True


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")
        return True

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")
        return True


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        payment_info = {
            "type": "crypto",
            "amount": amount,
            "currency": "USDT"
        }
        print(payment_info)
        return True

    def refund(self, amount):
        refund_info = {
            "type": "crypto",
            "refund_amount": amount,
            "currency": "USDT"
        }
        print(refund_info)
        return True


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):

        return self.payment_method.pay(amount)



if __name__ == "__main__":
    print("=" * 50)
    print("Часть 1: Инкапсуляция (класс Product)")
    print("=" * 50)


    p = Product("Iphone", 1000)
    print(f"Товар: {p.name}")
    print(f"Начальная цена: {p._price}")


    p.set_discount(20)
    print("Цена со скидкой:", p.get_price())


    p.apply_extra_discount("VIP123")
    print("Цена после VIP:", p.get_price())


    p.apply_extra_discount("wrong")
    print("Цена итоговая:", p.get_price())

    print("\n" + "=" * 50)
    print("Часть 2: Абстракция (система оплаты)")
    print("=" * 50)


    processor = PaymentProcessor(CardPayment())
    processor.process(100)

    processor = PaymentProcessor(CashPayment())
    processor.process(50)

    processor = PaymentProcessor(CryptoPayment())
    processor.process(200)

    print("\n" + "=" * 50)
    print("Дополнительные тесты")
    print("=" * 50)


    try:
        p2 = Product("Ноутбук", 1500)
        p2.set_discount(60)  # Должно вызвать ошибку
    except ValueError as e:
        print(f"Тест скидки >50%: {e}")


    print("\nТест возврата средств:")
    card = CardPayment()
    card.refund(30)

    crypto = CryptoPayment()
    crypto.refund(50)