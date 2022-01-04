from KSVE.GLOBAL import *
from KSVE.UTILS.logger import *


class Event():
    def __init__(self, view, ticks, command):
        loginfo(f"Event created; executing '{str(command)}' in {ticks} ticks")
        self.view = view
        self.in_ticks = ticks

        self.command = command
        self.engine = KSVE_ENGINE_INSTANCE[0]

        if view != None:
            view.events.append(self)
            self.ticks_start = view.tick
        else:
            self.engine.events.append(self)
            self.ticks_start = self.engine.tick

    def kill(self):
        if self.view != None:
            self.view.events.remove(self)
        else:
            self.engine.events.remove(self)
        loginfo(f"Event finished by executing '{self.command}' after {self.in_ticks} ticks")

    def check(self):
        if self.view != None:
            if self.view.tick - self.ticks_start > self.in_ticks:
                self.execute()
        else:
            if self.engine.tick - self.ticks_start > self.in_ticks:
                self.execute()

    def execute(self):
        self.command()
        self.kill()