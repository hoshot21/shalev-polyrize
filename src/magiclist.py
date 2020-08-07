class MagicList(list):
    """MagicList class

    Allows:
    1.  l = MagicList()
        l[0] = 5 (even if l[0] doesn't exist)
    2.  l = MagicList(cls_type=Person)
        l[0].age = 5 (inits the assigned type when provided)

    Doesn't allow:
    1.  l = MagicList()
        l[1] = 5 (enforces indexes continuity)
    """
    def __init__(self, cls_type=None):
        super(MagicList, self).__init__()
        self.cls_type = cls_type

    def __getitem__(self, key):
        length = super(MagicList, self).__len__()
        if key == length:
            if self.cls_type:
                self.__setitem__(key, self.cls_type())
        return super(MagicList, self).__getitem__(key)

    def __setitem__(self, key, obj):
        length = super(MagicList, self).__len__()
        if key == length:
            self.append(obj)
        super(MagicList, self).__setitem__(key, obj)
