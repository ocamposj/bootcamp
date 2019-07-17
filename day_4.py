def space():
    print("--------------------------------------------------------------------------------")

# Librerías estrictamente necesarias para la utilización de RoDI
import rodi
import time
from random import randint
robot = rodi.RoDI()

# robot.pixel(50,0,0)
# time.sleep(1)
# robot.pixel(0,50,0)
# time.sleep(1)
# robot.pixel(0,0,50)
# time.sleep(1)
# robot.pixel(0,0,0)
# time.sleep(1)
# robot.pixel(0,50,50)
# time.sleep(1)
# robot.pixel(50,0,50)
# time.sleep(1)
# robot.pixel(50,50,0)
# time.sleep(1)
# robot.pixel(0,0,0)
# time.sleep(1)

# robot.pixel(50,0,0)
# time.sleep(1)
# robot.pixel(50,50,0)
# time.sleep(1)
# robot.pixel(0,50,0)
# time.sleep(1)
# robot.pixel(0,0,0)

# for sqr_move in range(4):
#     robot.move_forward()    # Adelante
#     time.sleep(2)
#     robot.move_stop()       # Stop
#     robot.move_left()       # Izquierda
#     time.sleep(0.5)
#     robot.move_stop()       # Stop

# while True:
#     print("Distancia igual a",robot.see())

# try:
#     while True:
#         print("Distancia igual a",robot.see())
# #       robot.move_forward()
# except KeyboardInterrupt:
#     print("Finalizado")
# #   robot.move_stop()

# try:
#     while True:
#         if robot.see() > 10:
#             robot.pixel(0,50,0)
#             robot.move_forward()
#         else:
#             robot.pixel(50,0,0)
#             robot.move_backward()
#             time.sleep(1)
#             robot.move_left()
#             time.sleep(0.5)
#             robot.move_stop()
# except KeyboardInterrupt:
#     robot.move_stop()
#     robot.pixel(0,0,0)

# try:
#     while True:
#         if robot.see() < 10:
#             robot.move(100,100)
#             robot.pixel(50,0,0)
            
#         else:
#             tiempo=0
#             while tiempo < 20:
#                 robot.pixel(randint(0,100),randint(0,100),randint(0,100))
#                 robot.move(50,-50)
#                 tiempo = tiempo + 1
#             robot.move_forward()
#             time.sleep(1)

# except KeyboardInterrupt:
#     robot.move_stop()
#     robot.pixel(0,0,0)

# while True:
#     print(robot.sense())

# def beep(tone, time):
#     for key in tone_values:
#         if key == tone:
#             value = tone_values[key]
#     pwm = PWM(pin_piezo, freq=value, duty = 512)
#     sleep(time)
#     pwm.deinit()
#     sleep(1/20)

robot.sing(220, 5000)
time.sleep(0.5)
robot.sing(220, 5000)
time.sleep(0.5)
robot.sing(220, 5000)
time.sleep(0.5)
robot.sing(174, 3340)
time.sleep(0.5)
robot.sing(261, 1670)
time.sleep(0.5)
robot.sing(220, 5000)
time.sleep(0.5)
robot.sing(174, 3340)
time.sleep(0.5)
robot.sing(261, 1670)
time.sleep(0.5)
robot.sing(220, 5000)

time.sleep(1)
robot.sing(329, 5000)
time.sleep(0.5)
robot.sing(329, 5000)
time.sleep(0.5)
robot.sing(329, 5000)
time.sleep(0.5)
robot.sing(349, 3340)
time.sleep(0.5)
robot.sing(261, 1670)
time.sleep(0.5)
robot.sing(207, 5000)
time.sleep(0.5)
robot.sing(174, 3340)
time.sleep(0.5)
robot.sing(261, 1670)
time.sleep(0.5)
robot.sing(220, 5000)

time.sleep(1)
robot.sing(440, 5000)
time.sleep(0.5)
robot.sing(220, 3340)
time.sleep(0.5)
robot.sing(220, 1670)
time.sleep(0.5)
robot.sing(440, 5000)
time.sleep(0.5)
robot.sing(415, 3340)
time.sleep(0.5)
robot.sing(392, 1670)
time.sleep(0.5)
robot.sing(370, 1000)
time.sleep(0.5)
robot.sing(329, 1000)
time.sleep(0.5)
robot.sing(349, 1000)

time.sleep(1)
robot.sing(233, 1670)
time.sleep(0.5)
robot.sing(311, 5000)
time.sleep(0.5)
robot.sing(293, 3340)
time.sleep(0.5)
robot.sing(277, 1670)
time.sleep(0.5)
robot.sing(261, 1000)
time.sleep(0.5)
robot.sing(247, 1000)
time.sleep(0.5)
robot.sing(261, 1000)
time.sleep(0.5)