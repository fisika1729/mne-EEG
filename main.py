import mne
import matplotlib.pyplot as plt
from pathlib import Path
import os
from mne import channels

# Define the path to the .set file
data_path = Path('/mnt/eb92f9cc-64e6-4a6b-8dce-30d243f7eab9/12246218')
set_file = data_path / 'Stars_mento_02.set'

# Load the .set file with a specified montage
raw = mne.io.read_epochs_eeglab(set_file)

# Check if the montage is set, if not, set a default montage
if raw.get_montage() is None:
    # Specify a standard montage (e.g., 'standard_1020')
    montage = channels.make_standard_montage('standard_1020')
    raw.set_montage(montage)

# Filter the data
raw.filter(l_freq=1.0, h_freq=40.0)

# Plot the raw data
raw.plot()

# Save the filtered data
filtered_file = data_path / 'filtered_data.fif'
raw.save(filtered_file, overwrite=True)

# Show the plot
plt.show()
