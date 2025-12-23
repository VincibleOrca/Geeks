from faker import Faker     #Библиотека Faker в Python нужна для генерации фейковых (случайных) данных,
                            #которые выглядят как настоящие.
                            #Её часто используют для тестирования, обучения, заполнения баз данных,
                            # примеров кода и учебных проектов.

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
# в файле requirements появилась tzdata==2025.3 я не знаю что это
# оно появилось само во время установки Faker
