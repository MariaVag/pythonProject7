class EvenNumbers:

    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        if self.a <= 30:
            x = self.a
            self.a +=2
            return x
        else:
            raise StopIteration



en = EvenNumbers()
itera = iter(en)
for x in itera:
    print(x)