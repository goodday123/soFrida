import logging
import queue
from logging.handlers import QueueHandler, QueueListener

class sfLogger:
    def __init__(self):
        self.format = "%(message)s"
        self.log_queue = queue.Queue()
        self.queue_handler = QueueHandler(self.log_queue)
        logging.basicConfig(format=self.format)
        self.logger = logging.getLogger("testlogger")
        self.logger.addHandler(self.queue_handler)
        self.logger.setLevel(logging.INFO)

        self.listener = QueueListener(self.log_queue, self.queue_handler)
        self.listener.start()
        self.isStop = False

    def logprint(self):
        print (self.log_queue.get().getMessage())

    def loggenerator(self):
        while self.isStop == False:
            yield "data: "+self.log_queue.get().getMessage()+"\n\n"

    def stop(self):
        self.isStop = True