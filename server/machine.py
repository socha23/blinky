from base_machine import BaseMachine

Machine = BaseMachine()

Machine.set_neopixel_strip(10)

Machine.add_neopixel("Fryzjer", 0, 2)
Machine.add_neopixel("Bar", 2, 2)
Machine.add_neopixel("Biuro detektywa", 4, 2)
Machine.add_neopixel("II poziom", 6, 2)
Machine.add_neopixel("III poziom", 8, 2)

print("Machine loaded")
