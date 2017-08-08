# Redis simple queue


Very simple implementation from article : http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html


## usage

```shell
    pip install redis_simple_queue
```

### The sender
```python
from redis_simple_queue import RedisQueue

queue = RedisQueue('my_queue')
queue.put('my message')
```

### The worker

```python
from redis_simple_queue import Worker, RedisQueue

class MyWorker(Worker):

    def run(self, msg):
        print(msg)
        return msg

queue = RedisQueue('my_queue')
worker = MyWorker(queue)
worker.dequeue()
```
