
class Propeller(object):
    def __init__(self):
        self.count = 0
        self.pitch = 0
        # self.type = 0 ASSUMED STANDARD???
        self.bladeCount = 0
        return

class Thrust(object):
    def __init__(self, rpm, propeller):
        self.propeller = propeller
        self.temperature = 21.1111 # deg C ~= 70.0F
        self.rpm = rpm
        return
    
    
    def staticThust(self):
        return
    
    
    ## m/s
    def perimiterSpeed(self):
        return
    
    
    ## watts
    def power(self):
        return