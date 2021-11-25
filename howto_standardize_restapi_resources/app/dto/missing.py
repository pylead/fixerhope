class _Missing:
    def __bool__(self):
        return False


MISSING = _Missing()
