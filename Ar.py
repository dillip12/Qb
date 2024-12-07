import serial
import time

class ArduinoController:
    def __init__(self, port: str, baud_rate: int = 9600):
        self.serial = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset

    def read_analog(self):
        self.serial.write(b'R')  # Send command to read A0
        time.sleep(0.1)
        if self.serial.in_waiting:
            return int(self.serial.readline().decode().strip())
        return None

    def set_digital(self, state: str):
        if state.upper() == "HIGH":
            self.serial.write(b'H')
        elif state.upper() == "LOW":
            self.serial.write(b'L')
        else:
            raise ValueError("State must be 'HIGH' or 'LOW'")

    def close(self):
        self.serial.close()
