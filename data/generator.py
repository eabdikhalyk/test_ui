import random


class GeneratorData:
    def phone_number(self):
        prefix = random.choice(['708', '707', '747', '700'])
        number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return prefix + number

    def invoice(self):
        invoice = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        return invoice

    def iin(self):
        iin = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        return iin

    def account(self):
        account = ''.join([str(random.randint(0, 9)) for _ in range(20)])
        return account