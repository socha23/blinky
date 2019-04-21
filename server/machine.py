from base_machine import BaseMachine

Machine = BaseMachine()

Machine.set_neopixel_strip(10)

Machine.add_neopixel("I", 0, 2)
Machine.add_neopixel("II", 2, 2)
Machine.add_neopixel("III", 4, 2)
Machine.add_neopixel("IV", 6, 2)
Machine.add_neopixel("V", 8, 2)

print("Machine loaded")
