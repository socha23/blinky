def setup(machine):
    machine.add_led("Latarnia", 14)
    machine.set_neopixel_strip(10)
    machine.add_neopixel("Fryzjer", 0, 2)
    machine.add_neopixel("Bar", 2, 2)
    machine.add_neopixel("Biuro detektywa", 4, 2)
    machine.add_neopixel("II poziom", 6, 2)
    machine.add_neopixel("III poziom", 8, 2)
    print("Machine loaded")
