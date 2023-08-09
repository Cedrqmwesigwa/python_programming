import tkinter as tk
import moviepy.editor as mpy

# Create the main window
root = tk.Tk()
root.title("Video to Audio Converter")

# Create the entry field for the video file path
video_path_entry = tk.Entry(root)
video_path_entry.pack()

# Create the browse button
browse_button = tk.Button(root, text="Browse", command=browse)
browse_button.pack()

# Create the output file path entry
output_path_entry = tk.Entry(root)
output_path_entry.pack()

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

def browse():
    # Open a file dialog to select the video file
    video_path = tk.filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    video_path_entry.insert(0, video_path)

def convert():
    # Get the video file path from the entry field
    video_path = video_path_entry.get()

    # Get the output file path from the entry field
    output_path = output_path_entry.get()

    # Create a video object from the video file path
    video = mpy.VideoFileClip(video_path)

    # Extract the audio from the video
    audio = video.audio

    # Save the audio to the output file path
    audio.write_audiofile(output_path)

    print("Audio converted successfully!")

# Start the main loop
root.mainloop()
