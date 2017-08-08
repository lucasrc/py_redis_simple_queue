from abc import ABCMeta


class Worker(metaclass=ABCMeta):
    """ Another simple worker abstract class """

    def __init__(self, redis_queue):
        self.__queue = redis_queue

    def dequeue(self):
        """ Enqueue messages and put into run """
        while True:
            msg = self.__queue.get()
            self.run(msg)

    def run(self, msg):
        pass

