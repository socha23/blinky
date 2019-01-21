from base_machine import BaseMachine

Machine = BaseMachine()

Machine.add_led(24, "Czerwony")
Machine.add_led(25, "Bialy")

print("Machine loaded")