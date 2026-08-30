from typing import List

def read_integers() -> List[int]:
    number_strings = input().split(",")
    return list(map(int, number_strings))

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
