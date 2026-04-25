class NumberSeperator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.input_numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def read_numbers(self):
        file = open(self.file_name, "r")
        data = file.read()
        file.close()

        for num in data.split():
            self.input_numbers.append(num)

    def separate_the_integers(self):
        for num in self.input_numbers:
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)

    




