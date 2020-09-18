import machine


class Pins:
    """define pin configurations"""

    def __init__(self):

        # digital output
        self.dout25 = machine.Pin(25, machine.Pin.OUT)
        self.dout26 = machine.Pin(26, machine.Pin.OUT)
        self.dout32 = machine.Pin(32, machine.Pin.OUT)
        self.dout33 = machine.Pin(33, machine.Pin.OUT)

        # digital input
        self.din12 = machine.Pin(12, machine.Pin.IN)
        self.din13 = machine.Pin(13, machine.Pin.IN)
        self.din14 = machine.Pin(14, machine.Pin.IN)
        self.din27 = machine.Pin(15, machine.Pin.IN)

        # analog inputs # MAX 3.3V should be used!
        self.adc35 = machine.ADC(35)#currently A0 is pin 34.
        self.adc35.atten(machine.ADC.ATTN_11DB)   # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        self.adc36 = machine.ADC(36)
        self.adc36.atten(machine.ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        # self.adc34 = machine.ADC(34)
        # self.adc34.atten(machine.ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        # self.adc35 = machine.ADC(35)
        # self.adc35.atten(machine.ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)

        # analog outputs (actually PWM)
        self.pwm0 = machine.PWM(machine.Pin(39))
        self.pwm1 = machine.PWM(machine.Pin(18))
        