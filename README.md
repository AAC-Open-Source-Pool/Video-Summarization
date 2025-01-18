# Video-Summarization
<h2>Team Details</h2>
<b>Team Number: </b><p>24AACL05</p>
<b>Senior Mentor:</b><p> Rohitha Tunikpati</p>
<b>Junior Mentor:</b><p> Yellanki Ekantha Sai Sundar</p>
<b>Team Member 1:</b><p> Charshitha Saineni</p>
<b>Team Member 2:</b><p> Jahnavi Gummadi</p>
<b>Team Member 3:</b><p> Kurukunda Srikari</p>
<b>Team Member 4:</b><p> Popuri Pratima</p>

<div align="center">
    <h1>VIDEO SUMMARIZER PROJECT</h1>
</div>
<h2>Overview</h2>

The Video Summarizer project is designed to process and summarize MP4 video files by extracting unique frames based on frame differences. This helps in creating a shorter version of the video by retaining only the essential frames, making it easier to review and analyze. The project leverages OpenCV and Numpy for video processing, and Streamlit to create an interactive web interface.

<h2>Features</h2>
<p><b>1) MP4 to NPY Conversion:</b> Converts uploaded MP4 video files into NPY format, storing the video frames as a numpy array.</p>
<p><b>2) Frame Summarization:</b> Utilizes frame difference to identify and retain unique frames, removing redundant frames to create a summarized video.</p>
<p><b>3) Real-time Metrics:</b> Displays metrics such as total frames, unique frames, common frames, and summarization ratio.</p>
<p><b>4) Interactive Web Interface:</b> A user-friendly interface built with Streamlit for easy video uploading, processing, and visualization of results.</p>
<p><b>4) Automated Video Conversion:</b> Uses ffmpeg to convert summarized AVI files into MP4 format for easier playback and sharing.</p>
<p><b>5) NPY to Summarized AVI and MP4:</b> Converts NPY file to a summarized AVI file and then back to MP4 format for simplified viewing and sharing.</p>
<h2>Applications</h2>
<p>Some of the real-time applications of this project include: </p>
<p><b>Sports Highlights Generation:</b> Automatically generate highlights of sports events by summarizing key moments, such as goals, touchdowns, or spectacular plays.</p>
<p><b>Wildlife Monitoring:</b> Use the summarizer to condense hours of wildlife footage into clips showing significant animal behavior or rare sightings.</p>
<p><b>Disaster Response:</b> Summarize drone footage of disaster-stricken areas to quickly identify and assess damage, aiding in relief and recovery efforts.</p>
<p><b>Security Incident Reporting:</b> Create concise reports of security incidents by summarizing surveillance footage, making it easier for authorities to review and respond to events.</p>
<p><b>Construction Site Monitoring: </b> Summarize time-lapse videos of construction sites to highlight progress, identify potential safety issues, and ensure compliance with project timelines. This can help project managers and stakeholders quickly review the status and critical milestones of construction projects.</p>


<h2>Results</h2>
<p><b>Total Frames:</b> The total number of frames present in the original video.</p>
<p><b>Unique Frames:</b> The number of unique frames retained after summarization.</p>
<p><b>Common Frames:</b> The number of redundant frames removed during summarization.</p>
<p><b>Summarization Ratio:</b> The ratio of unique frames to total frames, indicating the efficiency of the summarization process.</p>
<p><b>Summarized Video:</b> A shorter version of the original video that highlights essential content.</p>


<h2>Usage Instructions</h2>
<p><b>Upload Video:</b> Use the Streamlit web interface to upload an MP4 video file.</p>
<p><b>Convert and Summarize:</b> The application converts the video into NPY format and summarizes the frames based on the specified threshold.</p>
<p><b>View Results:</b> View the metrics and play the summarized video directly within the Streamlit interface.</p>

<h2>Dependencies</h2>
<p><b>Python:</b> Ensure Python is installed on your system.</p>
<p><b>OpenCV:</b> For video processing and frame extraction.</p>
<p><b>Numpy:</b> For handling and processing video frames.</p>
<p><b>Streamlit:</b> For creating the interactive web interface.</p>
<p><b>ffmpeg:</b> For video format conversion.</p>

<h2>Setup</h2>
<p><b>1) Install the required dependencies:</b> 
    <pre>pip install streamlit opencv-python-headless numpy</pre></p>
<p>2) Ensure ffmpeg is installed and accessible from your system's PATH.</p>
<p><b>3) Run the streamlit application:</b> 
<pre>streamlit run video_summarizer.py</pre></p>

<h2>Futue Enhancements</h2>
<p><b>1) Advanced Frame Analysis:</b> Developers can implement more sophisticated frame analysis techniques to improve summarization accuracy. Some of the techniques include- Optical Flow Analysis, Histogram-Based Methods, Structural Similarity Index (SSIM), Keyframe Extraction Using Clustering, Scene Change Detection,etc.</p>
<p><b>2) Customizable Threshold:</b> The application can be enhanced to allow users to adjust the frame difference threshold for summarization.</p>
<p><b>3) Batch Processing:</b> The system can be upgraded to enable batch processing of multiple video files for large-scale video summarization.</p>


