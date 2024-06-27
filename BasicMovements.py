from djitellopy import tello
from time import sleep

me = tello. Tello()
me.connect()
print(me.get_battery())

me.takeoff()
# move forward -> - would be backwards
me.send_rc_control(0, 50, 0, 0)
sleep (2)
# right movement -> - would be left
me.send_rc_control(50, 0, 0, 0)
sleep(2)

#so that it does not need to land while moving (better not break it)
me.send_rc_control(0, 0, 0, 0)
sleep (2)
me.land()
