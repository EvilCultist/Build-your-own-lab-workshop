import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# === CONFIGURATION ===
SERIAL_PORT = 'COM5'     # Change to your port (e.g., '/dev/ttyUSB0' or 'COM4')
BAUD_RATE = 115200        # Match what your MicroPython device is using
MAX_POINTS = 100          # Number of points to display on the plot

# === SETUP SERIAL ===
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# === DATA STORAGE ===
voltages = []
timestamps = []
start_time = time.time()

# === MATPLOTLIB UPDATE FUNCTION ===
def update_plot(frame):
    global voltages, timestamps

    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            voltage = float(line)
            current_time = time.time() - start_time
            voltages.append(voltage)
            timestamps.append(current_time)

            # Trim to max points
            voltages = voltages[-MAX_POINTS:]
            timestamps = timestamps[-MAX_POINTS:]

            plt.cla()
            plt.plot(timestamps, voltages, label='Voltage (V)')
            plt.xlabel('Time (s)')
            plt.ylabel('Voltage (V)')
            plt.title('Live ADC Voltage from Serial')
            plt.ylim(0, 3.5)
            plt.grid(True)
            plt.legend()
    except ValueError:
        # If the line isn't a float, ignore it
        pass

# === START LIVE PLOT ===
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_plot, interval=100)  # 100 ms update
plt.tight_layout()
plt.show()
