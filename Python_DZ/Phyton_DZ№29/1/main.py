# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

class Computer:
    def _init_(self):
        self.processor = None
        self.ram = None
        self.hard_drive = None

    def _str_(self):
        return f"Computer: Processor={self.processor}, RAM={self.ram}, Hard Drive={self.hard_drive}"


class ComputerBuilder:
    def _init_(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.processor = processor

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_hard_drive(self, hard_drive):
        self.computer.hard_drive = hard_drive

    def get_computer(self):
        return self.computer


builder = ComputerBuilder()
builder.set_processor("Intel Core i7")
builder.set_ram("16GB")
builder.set_hard_drive("1TB SSD")

computer = builder.get_computer()
print(computer)
