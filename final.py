from microbit import *
from ssd1306 import *
from ssd1306_text import *
while True:
    person1=int(pin2.read_digital()) 
    light_sensore=int(pin1.read_analog())
    tempe=float(temperature())
    
    if person1 == 1:
        pin0.write_analog(1023-light_sensore)
   
        if tempe > 27 :
            pin8.write_digital(1)
        else:
            pin8.write_digital(0)
    else:
        pin0.write_digital(0)
        pin8.write_digital(0)
    
    initialize()
    clear_oled()
    
    add_text(0, 0, "------")
    add_text(0, 1, str(tempe))
    add_text(0, 2, "------")
    add_text(0, 3, str(light_sensore))
    sleep(1000)
    
    
    
    
    

    
    
            