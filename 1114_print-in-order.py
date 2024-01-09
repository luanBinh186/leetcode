from threading import *


class Foo:
    sem_first = Semaphore(0)
    sem_second = Semaphore(0)

    def __init__(self):
        self.sem_first = Semaphore(0)
        self.sem_second = Semaphore(0)
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sem_first.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.sem_first.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.sem_second.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.sem_second.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()