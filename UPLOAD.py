import cv2
import numpy as np
import subprocess
import os  # Import the os module

# Set the directory containing the .npy files
npy_folder = "D://Video Summarizer//archive//NPY files//"

# Set the threshold for frame difference
threshold = 20.0
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 500, 400)

# Iterate through each .npy file in the folder
for npy_file in os.listdir(npy_folder):
    if npy_file.endswith(".npy"):
        full_npy_file = os.path.join(npy_folder, npy_file)

        # Load frames from the .npy file
        frames = np.load(full_npy_file, allow_pickle=True)
        frames = frames.astype(np.uint8)

        # Get the dimensions of the frame
        height, width, _ = frames[0].shape

        # Define output filenames (without extensions)
        output_file_base = full_npy_file.replace('.npy', '')

        # Create the .avi file using OpenCV
        output_file_avi = f"{output_file_base}.avi"
        writer_avi = cv2.VideoWriter(output_file_avi, cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))

        # Initialize variables
        prev_frame = frames[0]
        a = 0
        b = 0
        c = 0

        # Iterate through each frame
        for frame in frames:
            if ((np.sum(np.absolute(frame - prev_frame)) / np.size(frame)) > threshold):
                writer_avi.write(frame)
                prev_frame = frame
                a += 1
            else:
                prev_frame = frame
                b += 1

            # Display the current frame
            cv2.imshow('frame', frame)

            # Check if 'q' is pressed to break the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            c += 1

        print(f"File: {npy_file}")
        print("Total frames: ", c)
        print("Unique frames: ", a)
        print("Common frames: ", b)

        # Release the writer for the .avi file
        writer_avi.release()

        # Convert .avi to .mp4 using ffmpeg (assuming ffmpeg is installed)
        command = ["ffmpeg", "-i", output_file_avi, "-c:v", "libx264", "-c:a", "aac", f"{output_file_base}.mp4"]
        subprocess.run(command)

# Destroy all windows
cv2.destroyAllWindows()
