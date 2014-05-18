from threading import Timer

class Watchdog:
    def __init__(self, timeout, userHandler=None):  # timeout in seconds
        self.timeout = timeout
        self.handler = userHandler if userHandler is not None else self.defaultHandler
        self.timer = Timer(self.timeout, self.handler)

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)

    def stop(self):
        self.timer.cancel()

    def defaultHandler(self):
        raise self

watchdog = Watchdog(x)
def myHandler():
  print "Whoa! Watchdog expired. Holy heavens!"
  sys.exit()

watchdog = Watchdog(y, myHandler)

def doSomethingRegularly():
  # make sure you do not return in here or call watchdog.reset() before returning
    for i in xrange(100000):
        pass
    return "done"
    watchdog.reset()
