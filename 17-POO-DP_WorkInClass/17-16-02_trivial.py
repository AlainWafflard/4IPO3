from time import sleep

class Observable:
    """ sujet """

    def __init__(self):
        self.__observer_l = []

    def subscribe(self, observer):
        self.__observer_l.append(observer)

    def notify_observer(self, msg):
        for obs in self.__observer_l:
            obs.notify(msg)

    def unsubscribe(self, observer):
        self.__observer_l.remove(observer)


class Observer:
    """ observateur """

    def __init__(self, observable, name):
        self.name = name
        observable.subscribe(self)

    def notify( self, message ):
        print (f' {self.name} got this message from Observable : {message}')


"""
Demonstrating the Observer pattern implementation
"""
# Initializing the subject
subject = Observable()

# Initializing two observers with the subject object
observerFoo = Observer(subject, "Foo")
observerBar = Observer(subject, "Bar")

# The following message will be notified to 2 observers
subject.notify_observer('1st broadcast')
sleep(5)

observerBarFoo = Observer(subject, "BarFoo")

subject.unsubscribe(observerBar)

# The following message will be notified to just 1 observer since
# the observer has been unsubscribed
subject.notify_observer('2nd broadcast')

