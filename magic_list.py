from collections import UserList
from dataclasses import dataclass

class MagicList(UserList):
    def __init__(self, cls_type=None):
        super().__init__()
        self._cls_type = cls_type

    # Called to implement evaluation of self[key].
    def __getitem__(self, index):
        size = len(self.data)
        if index == -1 or size == index:
            self.data.append(self._cls_type())
        return super().__getitem__(index)

    # Called to implement evaluation of self[key].
    def __setitem__(self, index, item):
        size = len(self.data)
        if index == -1 or size == index:
            self.data.append(item)
        else:
            super().__setitem__(index, item)


