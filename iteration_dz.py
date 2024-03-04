class EvenNumbers:
    def __init__(self, start=0, end=30):
        self.start = start
        self.end = end


    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 2
            return self.start

        else:
            raise StopIteration


en = EvenNumbers()
itera = iter(en)
for x in itera:
    print(x)
