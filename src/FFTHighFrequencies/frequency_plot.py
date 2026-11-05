
import serial
import matplotlib.pyplot as plt

# Change COM4 if necessary
ser = serial.Serial("COM4", 115200, timeout=1)

# Set up graph
plt.ion()

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(800, 2400)

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("FFT Magnitude (a.u.)")
ax.set_title("High-Frequency Water Vibration")

ax.grid(True)

frequencies = []
magnitudes = []

reading = False

try:
    while plt.fignum_exists(fig.number):

        data = ser.readline().decode(
            errors="ignore"
        ).strip()

        if data == "SPECTRUM_START":
            frequencies = []
            magnitudes = []
            reading = True

        elif data == "SPECTRUM_END":

            if frequencies:
                line.set_data(
                    frequencies,
                    magnitudes
                )

                ax.relim()
                ax.autoscale_view(
                    scalex=False,
                    scaley=True
                )

                plt.pause(0.01)

            reading = False

        elif reading:
            try:
                frequency, magnitude = data.split(",")

                frequencies.append(float(frequency))
                magnitudes.append(float(magnitude))

            except ValueError:
                pass

        plt.pause(0.001)

finally:
    ser.close()
