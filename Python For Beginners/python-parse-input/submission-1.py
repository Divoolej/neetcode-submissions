from typing import List

def read_integers() -> List[int]:
    number_strings = input().split(",")
    def to_int(n: str) -> int:
        return int(n)
    ints = map(int, number_strings)
    return list(ints)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
