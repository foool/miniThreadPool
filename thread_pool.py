# !/usr/bin/env python
# -*- coding:utf-8 -*-

import Queue
import threading
import time

class ThreadPool(object):
    def __init__(self, thread_num=7):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.thread_num=7

    def __init_thread_pool(self,thread_num):
        for i in range(thread_num):
            self.threads.append(MyThread(self.work_queue))

    def add_job(self, func, *args):
        self.work_queue.put((func, args))

    def begin_to_finish(self):
        self.__init_thread_pool(self.thread_num)
        for item in self.threads:
            if item.isAlive():item.join()

class MyThread(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(*args)
                self.work_queue.task_done()
            except Queue.Empty:
                break
