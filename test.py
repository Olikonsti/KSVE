import KSVE
engine = KSVE.Engine(debug=True)

test_screen = KSVE.View()


KSVE.Entity(test_screen, "test.png", start_pos=(190, 0), fixed=False)
KSVE.Entity(test_screen, "test.png", start_pos=(100, 400))

KSVE.Event(None, 10000, lambda:print("leee"))

engine.set_active_view(test_screen)

engine.mainloop()