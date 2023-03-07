from pydub import AudioSegment

# Load the input audio file
input_file = "./통화 녹음 0269404030_230302_082957.m4a"
input_name = input_file.split("/")[-1].split(".")[0]


audio_file = AudioSegment.from_file(input_file, format="m4a")

# Define the duration to keep in milliseconds
duration_to_keep = 2.5 * 60 * 1000  # Keep 2.5 minutes

# Extract the desired portion of the audio file
trimmed_audio = audio_file[duration_to_keep:]

# Export the trimmed audio file
output_file = "./" + input_name + "_trimmed.mp3"
trimmed_audio.export(output_file, format="mp3")

