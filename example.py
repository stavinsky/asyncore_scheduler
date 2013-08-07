import asyncore_scheduler
import asyncore
import socket
import time


class Handler(asyncore.dispatcher_with_send):
    def __init__(self,sock=None,map=None):
        asyncore.dispatcher_with_send.__init__(self, sock, map)
        
        self.task1=asyncore_scheduler.Task(start=0, repeatable=True, interval=1, function=self.test_func1)   
        scheduler.addTask(self.task1)
        
    def test_func1(self):
        self.send("test_func1, now time is %s\r\n" % time.time())
        

        
    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)


        
        
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = Handler(sock)


scheduler=asyncore_scheduler.Scheduler()



server = EchoServer('localhost', 9999)
scheduler.asyncoreLoop(timeout=0.01)