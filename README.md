# miniThreadPool

### What is miniThreadPool?

An minimal Python thread pool class. 

The main idea of this demo is show you how a threadpool works and setup a simple useful threadpool tool. 

### How to use?

In `test.py` is a simple test file, which shows how to use the class ThreadPool:

> tp = ThreadPool(3)   

Initialize with 3 threads

> tp.add_job(func, args)    

Add your self-defined fuction that you want to parallelize and arguments for your function

>tp.begin_to_finish()     

Tell threads begin to run and finish automatically.


