from abc import ABCMeta, abstractmethod


class Worker(metaclass=ABCMeta):
    """ Another simple worker abstract class """

    def __init__(self, redis_queue):
        self.__queue = redis_queue

    def dequeue(self):
        """ Dequeue messages and put into run """
        while True:
            msg = self.__queue.get()
            self.run(msg)

    @abstractmethod
    def run(self, msg):
        pass

