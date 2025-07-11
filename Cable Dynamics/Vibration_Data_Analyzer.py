from sklearn.cluster import DBSCAN
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Main function to execute the program
def process_file(file_name):
    # Initialize empty lists for needed columns
    # column 1 is time domain in s
    time = []
    # column 2 is force in lbf
    force = []
    # column 3 is also time, so skip to column 4 which is acceleration in in/s^2
    accel = []
    # column 5 is the frequency domain in Hz
    freq = []
    # column 6 is coherence
    coherence = []
    # column 7 is also frequency, so skip to column 8 which is compliance in in/lbf
    compliance = []


    #Removed this section to improve the user expereience
    # # Prompt the user for the file name and confirm that it is correct
    # print("Hello, please upload your data in the form of a .tab file. Once the file is uploaded, please enter the file name. \nPlease do NOT include the file extension. \nExample:Test")
    # file_name = ("\nEnter the file name:")
    # file_name = input(file_name) + ".tab"
    # print(f"\nThe file is: {file_name}")
    # confirmation = input("Is this correct? (y/n):")
    # while confirmation != "y":
    #     file_name = input("\nEnter the file name:")
    #     file_name = file_name + ".tab"
    #     print(f"\nThe file is: {file_name}")
    #     confirmation = input("Is this correct? (y/n):")
    # Remove the file extension for the filename
    no_ext_file_name = file_name[:-4]
    
    # Open the tab delimited file given by the user and read it's data
    with open(f"Datasets/{file_name}", 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 8:  # Ensure we have enough columns
                time.append(float(row[0]) if row[0].strip() else 0.0)
                force.append(float(row[1]) if row[1].strip() else 0.0)
                accel.append(float(row[3]) if row[3].strip() else 0.0)
                freq.append(float(row[4]) if row[4].strip() else 0.0)
                coherence.append(float(row[5]) if row[5].strip() else 0.0)
                compliance.append(float(row[7]) if row[7].strip() else 0.0)
            else:
                print("Skipping row due to insufficient columns:", row)    
    
    # #Print the first 5 entries of each list to verify the data if necessary
    #     print("Time data:", time[:5])
    #     print("Force data:", force[:5])
    #     print("Acceleration data:", accel[:5])
    #     print("Frequency data:", freq[:5])
    #     print("Coherence data:", coherence[:5])
    #     print("Compliance data:", compliance[:5])
    
    #Plotting force and acceleration on the time domain
    # Plotting force with primary y-axis
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:blue'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Force (lbf)', color=color)
    ax1.plot(time,
             force,
             label='Force (lbf)',
             color=color,
             linestyle='-',
             marker='o')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Create a secondary y-axis for acceleration
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Acceleration (in/s^2)', color=color)
    ax2.plot(time,
             accel,
             label='Acceleration (in/s^2)',
             color=color,
             linestyle='--',
             marker='x')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Adding titles and showing the grid
    plt.title('Force and Acceleration on Time Domain')
    fig.tight_layout()  # Otherwise, the right y-label is slightly clipped
    plt.grid(True)
    
    # Show the plot
    plt.savefig(f'Graphs/{no_ext_file_name}_time_domain_plot.png')
    
    # Second Plot: Compliance and Coherence as functions of Frequency
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:green'
    ax3.set_xlabel('Frequency (Hz)')
    ax3.set_ylabel('Compliance (in/lbf)', color=color)
    ax3.plot(freq, compliance, label='Frequency (Hz)', color=color, linestyle='-', marker='o')
    ax3.tick_params(axis='y', labelcolor=color)
    
    # Create a secondary y-axis for coherence
    ax4 = ax3.twinx()
    color = 'tab:purple'
    ax4.set_ylabel('Coherence', color=color)
    ax4.plot(freq, coherence, label='Coherence', color=color, linestyle='--', marker='x')
    ax4.tick_params(axis='y', labelcolor=color)
    
    # Adding titles and showing the grid
    plt.title('Compliance and Coherence on Frequency Domain')
    fig2.tight_layout()  # Ensure the right y-label is not slightly clipped
    plt.grid(True)
    
    # Show the second plot
    plt.savefig(f'Graphs/{no_ext_file_name}_frequency_domain_plot.png')
    
    
    
    
    
    # Determine local Maxima and Minima
    # Find the peaks in the compliance data
    freq = np.array(freq)
    compliance = np.array(compliance)
    maxima_indices, _ = find_peaks(compliance)
    inverted_compliance = -compliance
    minima_indices, _ = find_peaks(inverted_compliance)
    peaks_freq = freq[maxima_indices]
    valleys_freq = freq[minima_indices]
    
    # Print the frequency and compliance values at the peaks for debugging if necessary
    # print("Local Maxima:")
    # for i in maxima_indices:
    #    print(f"  Frequency: {freq[i]:.3f} Hz, Compliance: {compliance[i]:.3f} in/lbf")
    
    # print("Local Minima:")
    # for i in minima_indices:
    #    print(f"  Frequency: {freq[i]:.3f} Hz, Compliance: {compliance[i]:.3f} in/lbf")
    
    # Also print the indices if needed for debugging
    # print(f"Maxima indices: {maxima_indices}")
    # print(f"Minima indices: {minima_indices}")
    
    
    #Filter data for natural frequency harmonics and eliminate false peaks
    eps = 2 #Defines the maximum distance between two samples for them to be considered in the same neighborhood
    min_samples = 1 #Minimum number of samples in a neighborhood for a point to be considered as a core point
    
    #Reshape the data for DBSCAN
    peaks_freq_DBSCAN = peaks_freq.reshape(-1, 1)
    
    #Fit the DBSCAN model and extract unique clusters and their corresponding natural frequencies
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(peaks_freq_DBSCAN)
    labels = db.labels_
    unique_labels = set(labels)
    natural_frequencies = [np.mean(peaks_freq[labels == label]) for label in unique_labels]
    
    # #Print the Natural Frequencies for debugging if necessary
    # print("Natural Frequencies:")
    # for nf in natural_frequencies:
    #     print(f"  {nf:.3f} Hz")
    
    #Identify the base frequency of the hamonics to identify the natural frequency
    based_frequencies = [f / (i+1) for i, f in enumerate(natural_frequencies)]
    # Print based frequencies for debugging if necessary
    # print(f"\nBased Frequencies: {based_frequencies}")
    def average(lst):
        return sum(lst) / len(lst)
    # Calculate the average based on the first 5 base frequencies
    avg = average(based_frequencies[:5])
    print(f"\nHere is the processed data from the '{file_name}' dataset: \n{RED}Natural Frequency: {avg:.3f} Hz")
    print(f"{GREEN}First Harmonic: {natural_frequencies[0]:.3f} Hz")
    print(f"{GREEN}Second Harmonic: {natural_frequencies[1]:.3f} Hz")
    print(f"{GREEN}Third Harmonic: {natural_frequencies[2]:.3f} Hz")
    print(f"{GREEN}Fourth Harmonic: {natural_frequencies[3]:.3f} Hz")
    print(f"{GREEN}Fifth Harmonic: {natural_frequencies[4]:.3f} Hz")

    # Filter the valleys
    eps = avg/2 #Defines the maximum distance between two samples for them to be considered in the same neighborhood; I use half the natural frequency as the eps value
    min_samples = 1 #Minimum number of samples in a neighborhood for a point to be considered as a core point
    
    #Reshape the data for DBSCAN
    valleys_freq_DBSCAN = valleys_freq.reshape(-1, 1)
    
    #Fit the DBSCAN model and extract unique clusters and their corresponding frequencies
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(valleys_freq_DBSCAN)
    labels = db.labels_
    unique_labels = set(labels)
    valley_frequencies = [np.mean(valleys_freq[labels == label]) for label in unique_labels]
    
    # #Print the Valley Frequencies for debugging if necessary
    # for vf in valley_frequencies:
    #     print(f"Valley Frequency:{vf: .3f} Hz")
    
    # Calculate the damping ratio
    x1, x3 = natural_frequencies[0], natural_frequencies[1]
    # The following variables are for the valleys, but they are not used in the calculation of the damping ratio; other methods use the following vairables to calculate the lograrithmic decrement.
    #x2, x4 = valley_frequencies[0], valley_frequencies[1]
    
    # #Print the variables x1 and x3 for debugging if necessary
    # print(f"x1: {x1:.3f} Hz")
    # print(f"x3: {x3:.3f} Hz")
    
    
    #Calculate the logarithmic decrement
    delta = np.log(x1/x3)
    print(f"{RED}Logarithmic Decrement: {delta:.3f}")
    
    #Calculate the zeta (the damping ratio)
    zeta = -delta / np.sqrt((delta**2 +(4 * np.pi**2)))
    
    print(f"Damping Ratio: {zeta:.3f}")

    #Create a text file to store the data
    content = f"""{no_ext_file_name}
    Natural Frequency: {avg:.3f} Hz
    Damping Ratio: {zeta:.3f}
    First Harmonic: {natural_frequencies[0]:.3f} Hz
    Second Harmonic: {natural_frequencies[1]:.3f} Hz
    Third Harmonic: {natural_frequencies[2]:.3f} Hz
    Fourth Harmonic: {natural_frequencies[3]:.3f} Hz
    Fifth Harmonic: {natural_frequencies[4]:.3f} Hz
    Logarithmic Decrement: {delta:.3f}
    Any additional data (including wire characterization) can be added below. 
    """
    text_file_name = f"{no_ext_file_name}_processed_data.txt"
    text_file_name = text_file_name + ".txt"
    with open(f"Processed Data/{text_file_name}", 'w') as file:
        file.write(content)
    
    print(f"{RESET}Analysis complete.")


# Define ANSI color codes for text formatting
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" 



datasets_folder = "Datasets"
tab_files = [f for f in os.listdir(datasets_folder) if f.endswith(".tab")]
print(f"\n{RESET}Found tab files in the '{datasets_folder}' folder:{tab_files}")
if not tab_files:
    print(f"{RED}No CSV files found in the '{datasets_folder}' folder.{RESET}")

for file_name in tab_files:
    print(f"\n{RESET}Processing file: {file_name}")
    process_file(file_name)
    
print("\nThank you for using this program. Have a great day!")


# main()
# repeat = input("\nWould you like to analyze another file? (y/n):")
# while repeat != "n":
#     main()
#     repeat = input("\nWould you like to analyze another file? (y/n):")

# print("\nThank you for using this program. Have a great day!")
    
