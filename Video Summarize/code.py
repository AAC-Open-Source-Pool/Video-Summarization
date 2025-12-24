import streamlit as st
import cv2
import numpy as np
import subprocess
from datetime import datetime

# Function to convert MP4 to NPY
def mp4_to_npy(mp4_file, npy_file):
    cap = cv2.VideoCapture(mp4_file)
    if not cap.isOpened():
        print("Error: Couldn't open video file")
        return

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break 
        # Convert frame from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    frames_array = np.array(frames)
    np.save(npy_file, frames_array)
    cap.release()
    
    print(f"Video has been converted and saved as {npy_file}")

# Function to summarize frames using frame difference
def summarize_frames(npy_file, threshold=20.0):
    # Load frames from the .npy file
    frames = np.load(npy_file, allow_pickle=True)
    frames = frames.astype(np.uint8)

    # Get the dimensions of the frame
    height, width, _ = frames[0].shape

    # Define output filenames (without extensions)
    output_file_base = npy_file.replace('.npy', '')

    # Create the .avi file using OpenCV
    output_file_avi = f"{output_file_base}.avi"
    writer_avi = cv2.VideoWriter(output_file_avi, cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))

    # Initialize variables
    prev_frame = frames[0]
    total_frames = 0
    unique_frames = 0
    common_frames = 0

    # Iterate through each frame
    for frame in frames:
        if ((np.sum(np.absolute(frame - prev_frame)) / np.size(frame)) > threshold):
            # Convert frame back to BGR before writing
            writer_avi.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            prev_frame = frame
            unique_frames += 1
        else:
            prev_frame = frame
            common_frames += 1

        total_frames += 1

    # Calculate the summarization ratio
    summarization_ratio = unique_frames / total_frames if total_frames > 0 else 0

    print(f"File: {npy_file}")
    print("Total frames: ", total_frames)
    print("Unique frames: ", unique_frames)
    print("Common frames: ", common_frames)
    print("Summarization ratio: ", summarization_ratio)

    # Release the writer for the .avi file
    writer_avi.release()

    # Convert .avi to .mp4 using ffmpeg (assuming ffmpeg is installed)
    output_file_mp4 = f"{output_file_base}.mp4"
    command = ["ffmpeg", "-i", output_file_avi, "-c:v", "libx264", "-c:a", "aac", output_file_mp4]
    subprocess.run(command)

    print(f"Summarized video saved as {output_file_mp4}")

    # Destroy all windows
    cv2.destroyAllWindows()

    return total_frames, unique_frames, common_frames, summarization_ratio, output_file_mp4

# Streamlit web app
st.title("Video Summarizer")
st.write("Upload an MP4 video file to summarize its frames and view the summarized video along with metrics.")

uploaded_file = st.file_uploader("Choose an MP4 file", type=["mp4"])

if uploaded_file is not None:
    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    video_name = uploaded_file.name.split('.')[0]
    mp4_file_path = f"{video_name}_{date_str}.mp4"
    
    with open(mp4_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded file: {uploaded_file.name}")
    
    npy_file_path = f"original_frames_{video_name}_{date_str}.npy"
    
    # Convert MP4 to NPY
    mp4_to_npy(mp4_file_path, npy_file_path)

    # Summarize frames and get metrics
    total_frames, unique_frames, common_frames, summarization_ratio, summarized_video_path = summarize_frames(npy_file_path)

    # Display metrics
    st.write(f"Total frames: {total_frames}")
    st.write(f"Unique frames: {unique_frames}")
    st.write(f"Common frames: {common_frames}")
    st.write(f"Summarization ratio: {summarization_ratio:.2f}")

    # Display summarized video
    st.write("### Summarized Video")
    st.video(summarized_video_path)
