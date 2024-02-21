# 
# filename: sensory.py
# by: Abhay Gupta
#
### desc:
# - Write a command-line program that takes first argument
# a path to a text file with a series of readings from each sensor
# - Compare two sensor data series
# - Print to the console a single message:
#     - indicate whether error was detected
#     - If detected, print time of error
# - if any imports are used, they must be from standard lib
# and justified

#
### Hardware: 
# - Motor
# - Encoder: attached between motor and gearbox
#     - 2048 counts per revolution of motor
#     - signed # for encoder counts
#     - 0 at boot time
# - Gearbox 30:1 ratio
# - Potentiometer: attached to output of shaft of gearbox
#     - range 0 -> 5V
#     - cycles linearly as a sawtooth wave per revolution
#     - voltage read by 8 bit A/D converter
#     - unsigned 0 = 0V, 255 = 5V
#     - absolution sensor - at boot time, non-zero position
# - Potentiometer/Encoder
#     - Fixed offset must be computed at start up 
#     - Assume both sensors are correct during first 0.5 seconds
#     - Usable time to initilize/calibrate algorithms

### imports

# Arguments are stored in the sys module’s argv attribute as a list
# Alternative: https://stackoverflow.com/a/27368717/10051223
# Commentary: Instructions are weird to say to not use imports but then
# the first step requires an import...
import sys

def extract_data():
    """ main sensor comparision script """

    # import in data via command line

    # check if only one data file argument (script is considered an additional argument)
    if len(sys.argv) != 2:
        print("Usage: compare_sensors.py <data_file>")
        return 1

    # Read data from file
    #data = read_data(sys.argv[1]) 
    data = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace
            line = line.strip()
            # Split the line based on spaces
            values = line.split()
            # Convert each value to a number
            data.append([float(value) for value in values])
    #return data
    data = [[row[i] for row in data] for i in range(3)]

    # data checks
    #print(data)
    #print(len(data))
    #print(len(data[1]))
    #plot_data(data)

    return data

def plot_data(data, error_index):

    # import plotting package
    # WSL plot instructions: https://stackoverflow.com/questions/43397162/show-matplotlib-plots-and-other-gui-in-ubuntu-wsl1-wsl2
    import matplotlib.pyplot as plt

    # Separate data into x and y values (assuming first column is x, second is y)
    time = data[0]
    encoder = list(x / 2048 * 360 / 30 + 180 for x in data[1])
    potentiometer = list(map(lambda x: x / 255 * 5, data[2]))

    print("min/max encoder", min(data[1]), max(data[1]))
    print("min/max encoder", min(encoder), max(encoder))
    print("min/max potentiometer", min(data[2]), max(data[2]))
    print("min/max potentiometer", min(potentiometer), max(potentiometer))

    # Mulitple plots
    fig, axes = plt.subplots(3)

    # Create the plot
    axes[0].plot(time, encoder)
    axes[0].set_xlabel('Time (seconds)')
    axes[0].set_ylabel('Output Shaft Position (degrees) and Time')

    # Customize the plot (optional)
    axes[1].plot(time, potentiometer)
    axes[1].set_xlabel('Time (seconds)')
    axes[1].set_ylabel('Potentiometer Reading (Voltage) and Time')
    #axes[1].set_title('Encoder & Potentiometer over time')

    # Plot potentiometer reading vs output shaft position
    axes[2].plot(encoder, potentiometer)
    axes[2].set_xlabel('Output Shaft Position (degrees)')
    axes[2].set_ylabel('Potentiometer Reading (volts)')
    #axes[2].set_title('Potentiometer reading vs output shaft position')

    # Show the plot
    plt.show()

def find_sensor_errors(data):
    """ Compare data and find if error """

    # Total data length
    data_len = len(data[0])

    # Max voltage reading
    volts = 5

    # Max bit range for potentiometer
    bit_volts = 255
    
    # Max encoder rating per revolution
    encoder = 2048

    # Gear Ratio
    gear_ratio = 30

    # Number of degrees per revolution
    degrees = 360

    # Encoder - Potentiometer ratio
    ratio = volts / degrees

    # Calibration Function
    encoder = list(x / encoder * degrees / gear_ratio for x in data[1])
    potentiometer = list(map(lambda x: x / bit_volts * volts, data[2]))

    # Get data range for calibration
    for index in range(data_len):
        if data[0][index] > 0.5:
            break

    # Calibration data
    calibration_data = [abs(x * ratio - y) for x, y in zip(encoder[0:index-1], potentiometer[0:index-1])]
    #calibration_data = encoder[index-1:] * ratio - potentiometer[index-1:]

    max_noise = max(calibration_data)
    #print("max noise:", max_noise)

    # Margin of Safety for Noise
    safety_ratio = 1.1

    #check = []
    # Check if remaining data has an error
    for i in range(index, data_len):
        
        # extract data point
        data_difference = encoder[i] * ratio - potentiometer[i]
        #check.append(abs(data_difference))

        if abs(data_difference) > safety_ratio * max_noise:
            print("Error Occured at ", data[0][i], "seconds")
            return i

    #print("check", max(check))

    return None

if __name__ == "__main__":
    """ run file directly """

    # extract data
    data = extract_data()

    # plot data
    #plot_data(data, None)

    # compare data and find if error
    error_index = find_sensor_errors(data)

    # check error location
    #plot_data(data, error_index)
