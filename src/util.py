class array:
    def __init__(self, size, standart_value=None, **kwargs):
        self.size = size
        self.standart_value = standart_value
        self.__list = self.size * [self.standart_value]

    def __repr__(self):
        return self.__list

    def __str__(self):
        return f"{self.__list}"

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__list.__getitem__(index)

        if isinstance(index, int):
            return self.__list[index]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.__list[index] = value

    def __delitem__(self, index):
        if isinstance(index, int):
            self.__list[index] = self.standart_value

    def __iter__(self):
        for value in self.__list:
            yield value

    def __len__(self):
        return self.size

    def count(self, search_value):
        return len([True for value in self.__list if search_value == value])

    def pop(self, index):
        value = self.__list[index]
        self.__list[index] = self.standart_value
        return value

    def put(self, added_value):
        for index, value in enumerate(self.__list):
            if value == self.standart_value:
                self.__list[index] = added_value
                break
        else:
            raise Exception('Array is full!')

    def reverse(self):
        self.__list = self.list[::-1]

    def copy(self):
        return self.__list[:]

    def clear(self):
        self.__list = self.size * [self.standart_value]


def check_isinstance(value, type_, ):
    if not isinstance(value, type_):
        raise TypeError(
            f"Value must be {value.__name__} instance, not {type(value).__name__}")
