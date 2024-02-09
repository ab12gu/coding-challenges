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


def compare_sensors():
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




def plot_data(data):

    # import plotting package
    # WSL plot instructions: https://stackoverflow.com/questions/43397162/show-matplotlib-plots-and-other-gui-in-ubuntu-wsl1-wsl2
    import matplotlib.pyplot as plt

    # Separate data into x and y values (assuming first column is x, second is y)
    time = data[0]
    encoder = data[1]
    potentiometer = data[2]

    # Create the plot
    plt.plot(time, encoder, label = "Encoder (degrees)")
    plt.plot(time, potentiometer, label = "Potentiometer (V)")

    # Customize the plot (optional)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Output Shaft Position (degrees) and Voltage')
    plt.title('Encoder & Potentiometer over time')

    # Show the plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    """ run file directly """

    # extract data
    data = compare_sensors()

    # plot data
    plot_data(data)
