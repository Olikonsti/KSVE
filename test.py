import random

import KSVE
engine = KSVE.Engine(debug=True)

test_screen = KSVE.View()

for i in range(100):
    KSVE.Entity(test_screen, "test.png", start_pos=(190 + random.randint(-10, 10), 0), fixed=False, width=20, height=20)
KSVE.Entity(test_screen, "test.png", start_pos=(100, 400), width=1000)

KSVE.Event(None, 100, lambda:engine.set_active_view(None))

engine.set_active_view(test_screen)

engine.mainloop()