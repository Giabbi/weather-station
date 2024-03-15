import os, glob, time

class DS18B20(object):
    def __init__(self):
        self.device_file = glob.glob("/sys/bus/w1/devices/28*")[0] + "/w1_slave" 

    def read_temp_raw(self):
        while True:
            f = open(self.device_file, "r") # Read input file
            lines = f.readlines()
            f.close()
            if len(lines) != 0: # Check if there is content in the reading to prevent exceptions 
                break
        return lines

    def crc_check(self, lines):
        yes = ["YES"]
        return lines[0].strip()[-3:] == yes[0]

    def read_temp(self):
        temp_c = -255
        attempts = 0

        lines = self.read_temp_raw()
        success = self.crc_check(lines)

        while not success and attempts < 3:
            time.sleep(.2)
            lines = self.read_temp_raw()
            success = self.crc_check(lines)
            attempts += 1

        if success:
            temp_line = lines[1]
            equal_pos = temp_line.find("t=")
            if equal_pos != -1:
                temp_string = temp_line[equal_pos+2:]
                temp_c = float(temp_string)/1000.0

        return temp_c

if __name__ == "__main__":
    obj = DS18B20()
    print("Temp: %s C" % obj.read_temp())