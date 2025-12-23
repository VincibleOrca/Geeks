# Декоратор для логирования действий
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f" Вызов метода: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class User:
    total_users = 0  # счётчик всех пользователей

    def __init__(self, name):
        self.name = name
        User.total_users += 1

    # Обычный метод экземпляра
    @log_action
    def say_hello(self):
        print(f"Привет, меня зовут {self.name}")

    # Метод класса
    @classmethod
    def show_total_users(cls):
        print(f"Всего пользователей: {cls.total_users}")

    # Статический метод
    @staticmethod
    def info():
        print(" Класс User представляет пользователя системы")


user1 = User("Alice")
user2 = User("Bob")

user1.say_hello()
user2.say_hello()

User.show_total_users()
User.info()
