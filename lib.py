class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m, s)

    def __str__(self):
        return f'Время {self.minutes}:{self.seconds}'

    def __repr__(self):
        return f'Time({self.minutes}:{self.seconds})'

    def time_info(self):
        return f'{self.minutes}:{self.seconds}'

class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[len(self.lst) - 1 - item]