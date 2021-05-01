from gpiozero import OutputDevice,CPUTemperature
import time

class RpiFanControll:
    ON_THRESHOLD = 65  # (degrees Celsius) Fan kicks on at this temperature.
    OFF_THRESHOLD = 35  # (degress Celsius) Fan shuts off at this temperature.
    SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
    GPIO_PIN = 17  # Which GPIO pin you're using to control the fan.

    def controll(self):
        temp = self.get_temp()
        if temp > self.ON_THRESHOLD and not self.fan.value:
            self.fan.on()
        elif self.fan.value and temp < self.OFF_THRESHOLD:
            self.fan.off()

    def get_temp(self):
        return self.cpu_temp.temperature

    def __init__(self):
        self.cpu_temp = CPUTemperature()
        self.fan = OutputDevice(self.GPIO_PIN)
        while True:
            self.controll()
            time.sleep(self.SLEEP_INTERVAL)

try:
    RpiFanControll()
except KeyboardInterrupt:
    pass
finally:
    pass


