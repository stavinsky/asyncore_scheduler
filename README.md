asyncore_scheduler
==================



What is this?
-------------

This is a two  python classes, used to run some functions with asyncore with delay or repeat functions with interval. 



Task
----

Task describes what function we need to run, how often and when start. 


Scheduler
---------

Scheduler used to run with every asyncore loop iterate. 


How to use
----------

Look at example.py. 


### The key strings is:

defining task1:
```
self.task1=asyncore_scheduler.Task(start=0, repeatable=True, interval=1, function=self.test_func1)
```
adding to scheduler:
```
scheduler.addTask(self.task1)
```

Define scheduler object:
```
scheduler=asyncore_scheduler.Scheduler()
```

The MAIN loop:
```
scheduler.asyncoreLoop(timeout=0.01)
```
Here two important things. 
+  First - We unfortunately have to use custom asyncore.loop()
+  Second - timeout have to  be not a big 
