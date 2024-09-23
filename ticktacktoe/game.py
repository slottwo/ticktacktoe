class Game:
    def __init__(self, setup: str = " " * 9) -> None:
        self.data: str = setup
        self.data2: list[list]

    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        return sum(i != " " for i in self.data)
        return sum(i != " " for j in self.data2 for i in j)
        return 9 - ("".join(self.data2)).count(" ")

    def __getitem__(self, *index: int):
        if len(index) == 1:
            return self.game[index]
        if len(index) == 2:
            return self.game[index[0] + index[1] * 3]
        raise IndexError

    def value(self) -> bool:
        if len(self) >= 5:
            h = any("xxx" == self.data[i : i + 3 : 3] for i in range(3))
            v = any("xxx" == self.data[i::3] for i in range(3))
            d = "xxx" == self.data[::4] or "xxx" == self.data[2:-2:2]
            return h or v or d
        return False
