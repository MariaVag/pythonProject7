
import threading
from time import sleep

word = ['a', 'b', 'c', 'd', 'i', 'f', 'j']

def func_words():
    for words in word:
        sleep(1)
        print(words)
def functions():
    for i in range(10):
        sleep(1)

        print(i)


thread1 = threading.Thread(target=functions)
thread2 = threading.Thread(target=func_words)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads have finished executing!")