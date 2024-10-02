class Game:
    def __init__(self, setup=b'         ') -> None:
        self.state = setup

    def __len__(self) -> int:
        return 9 - self.state.count(' ')

    def __getitem__(self, index: int):
        if len(index) == 1:
            return self.state[index[0]]
        if len(index) == 2:
            return self.state[index[0] + index[1] * 3]
        raise IndexError(f"{len(index)}-dimensional indexation not supported")

    def value(self):
        if len(self) < 5:  # optimization: turn 5: round 3
            return 0  # too early
        _ = self.state
        _ = _[:3], _[3:6], _[6:], _[::3], _[1::3], _[2::3], _[::4], _[2:-2:2]
        if b'xxx' in _:
            return 1  # win 1
        return -(b'ooo' in _)  # lose -1 // draw 0

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, _):
        if isinstance(_, bytes) and len(_) == 9:
            self.__state = _
        elif isinstance(_, str) and len(_) == 9:
            self.__state = _.encode()
        else:
            raise ValueError

    @state.deleter
    def state(self):
        self.__state = b'         '
