#!/usr/bin/python

import asyncore, socket
import time

class Task():
    def __init__(self,start=0, repeatable=False, interval=0, function=None):
        self.start=start                        #seconds before first start
        self.repeatable=repeatable              #repeat task or run only one time
        self.interval=interval                  
        self.last_run=None
        self.function=function                  #link to custom function
        self.executed=False
        self.first_run=time.time()
        
        
    def run(self):
        self.last_run=time.time()
        self.function()
        
        
        
    def runCheck(self):
        now=time.time()
        if now-self.first_run<self.start:
            return
        if not self.repeatable:
            if not self.executed:
                self.executed=True
                self.run()
                
            else:
                return
        else:
            if not self.last_run:
                self.run()
                return
            else:
                if now-self.last_run >= self.interval:
                    self.run()
                else:
                    return
        
    
class Scheduler():
    def __init__(self):
        self.tasks=[]
        
    def run(self):
        pass
    
    def scheduler(self):
        if len(self.tasks)>0:
            for task in self.tasks:
                task.runCheck()

    def asyncoreLoop(self,timeout=30.0, use_poll=False, map=None, count=None):
        """This is just asyncore.loop but with added scheduler """
        if map is None:
            map = asyncore.socket_map

        if use_poll and hasattr(asyncore.select, 'poll'):
            poll_fun = asyncore.poll2
        else:
            poll_fun = asyncore.poll

        if count is None:
            while map:
                poll_fun(timeout, map)
                self.scheduler()

        else:
            while map and count > 0:
                poll_fun(timeout, map)
                count = count - 1
                self.scheduler()


    def addTask(self, task):
        self.tasks.append(task)
