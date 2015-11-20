# miniThreadPool
An minimal Python thread pool class. 

The main idea of this demo is show you how a threadpool works and setup a simple useful threadpool tool. 

In `test.py` is a simple test file:

> tp = ThreadPool(3)

Initialization with 3 threads

> tp.add_job(func, args)

add your self-defined fuction that you want to parallelize and arguments for your function

>tp.begin_to_finish()

Tell the thread begin to run and finish automatically.


