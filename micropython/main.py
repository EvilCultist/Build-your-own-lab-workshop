import machine
import time

# Setup ADC on pin 36 (GPIO36)
adc = machine.ADC(machine.Pin(34))

# Configure ADC attenuation for full-scale voltage (0-3.3V)
adc.atten(machine.ADC.ATTN_11DB)  # 11 dB attenuation (max ~3.6V)

# ADC width (resolution)
adc.width(machine.ADC.WIDTH_12BIT)  # 12-bit resolution (0-4095)

def read_voltage():
    raw = adc.read()  # Read ADC raw value (0-4095)
    voltage = raw / 4095 * 3.3  # Convert to voltage (assuming 3.3V reference)
    return voltage

while True:
    voltage = read_voltage()
    print(f"Voltage: {voltage:.3f} V")
    time.sleep(0.1)  # 10 samples per second

