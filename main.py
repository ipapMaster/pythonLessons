# ООП - Спецметоды
from lib import ReversedList

if __name__ == '__main__':
    lst = ReversedList([1, 2, 3])

    for i in range(len(lst)):  # __len__()
        print(lst[i])  # __getitem__(item)

# должен распечатать:
# 3
# 2
# 1
