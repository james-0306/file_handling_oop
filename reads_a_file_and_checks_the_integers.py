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