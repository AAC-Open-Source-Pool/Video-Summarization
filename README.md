# Video Summarization & Youtube Transcript Summarizer and Translator
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
<h2>📌 Overview</h2>

<p>
The Video Summarizer project is designed to process and summarize MP4 video files by extracting unique frames based on frame differences 🎞️. 
This helps in creating a shorter version of the video by retaining only the essential frames, making it easier to review and analyze 🔍. 
The project leverages OpenCV and Numpy for video processing, and Streamlit to create an interactive web interface 🖥️.
</p>

<h2>✨ Features</h2>

<p><b>1) 🎥 MP4 to NPY Conversion:</b> Converts uploaded MP4 video files into NPY format, storing the video frames as a numpy array.</p>

<p><b>2) ✂️ Frame Summarization:</b> Utilizes frame difference to identify and retain unique frames, removing redundant frames to create a summarized video.</p>

<p><b>3) 📊 Real-time Metrics:</b> Displays metrics such as total frames, unique frames, common frames, and summarization ratio.</p>

<p><b>4) 🖱️ Interactive Web Interface:</b> A user-friendly interface built with Streamlit for easy video uploading, processing, and visualization of results.</p>

<p><b>5) 🔄 Automated Video Conversion:</b> Uses ffmpeg to convert summarized AVI files into MP4 format for easier playback and sharing.</p>

<p><b>6) 📁 NPY to Summarized AVI and MP4:</b> Converts NPY file to a summarized AVI file and then back to MP4 format for simplified viewing and sharing.</p>

<h2>🧰 Dependencies</h2>

<p><b>🐍 Python:</b> Ensure Python is installed on your system.</p>

<p><b>🎞️ OpenCV:</b> For video processing and frame extraction.</p>

<p><b>📐 Numpy:</b> For handling and processing video frames.</p>

<p><b>🖥️ Streamlit:</b> For creating the interactive web interface.</p>

<p><b>🔧 ffmpeg:</b> For video format conversion.</p>

<h2>⚙️ Setup</h2>

<p><b>1️⃣ Install the required dependencies:</b></p>
<pre>pip install streamlit opencv-python-headless numpy</pre>

<p><b>2️⃣</b> Ensure ffmpeg is installed and accessible from your system's PATH.</p>

<p><b>3️⃣ Run the Streamlit application:</b></p>
<pre>streamlit run video_summarizer.py</pre>

<h2>🧭 Usage Instructions</h2>

<p><b>⬆️ Upload Video:</b> Use the Streamlit web interface to upload an MP4 video file.</p>

<p><b>⚙️ Convert and Summarize:</b> The application converts the video into NPY format and summarizes the frames based on the specified threshold.</p>

<p><b>👀 View Results:</b> View the metrics and play the summarized video directly within the Streamlit interface.</p>

<h2>📈 Results</h2>

<p><b>🎞️ Total Frames:</b> The total number of frames present in the original video.</p>

<p><b>⭐ Unique Frames:</b> The number of unique frames retained after summarization.</p>

<p><b>🗑️ Common Frames:</b> The number of redundant frames removed during summarization.</p>

<p><b>📉 Summarization Ratio:</b> The ratio of unique frames to total frames, indicating the efficiency of the summarization process.</p>

<p><b>▶️ Summarized Video:</b> A shorter version of the original video that highlights essential content.</p>

<h2>🌍 Applications</h2>

<p>Some of the real-time applications of this project include:</p>

<p><b>🏅 Sports Highlights Generation:</b> Automatically generate highlights of sports events by summarizing key moments, such as goals, touchdowns, or spectacular plays.</p>

<p><b>🦁 Wildlife Monitoring:</b> Use the summarizer to condense hours of wildlife footage into clips showing significant animal behavior or rare sightings.</p>

<p><b>🚨 Disaster Response:</b> Summarize drone footage of disaster-stricken areas to quickly identify and assess damage, aiding in relief and recovery efforts.</p>

<p><b>🔐 Security Incident Reporting:</b> Create concise reports of security incidents by summarizing surveillance footage, making it easier for authorities to review and respond to events.</p>

<p><b>🏗️ Construction Site Monitoring:</b> Summarize time-lapse videos of construction sites to highlight progress, identify potential safety issues, and ensure compliance with project timelines. This can help project managers and stakeholders quickly review the status and critical milestones of construction projects.</p>

<h2>🚀 Future Enhancements</h2>

<p><b>1️⃣ Advanced Frame Analysis:</b> Developers can implement more sophisticated frame analysis techniques to improve summarization accuracy. Some of the techniques include Optical Flow Analysis, Histogram-Based Methods, Structural Similarity Index (SSIM), Keyframe Extraction Using Clustering, Scene Change Detection, etc.</p>

<p><b>2️⃣ Customizable Threshold:</b> The application can be enhanced to allow users to adjust the frame difference threshold for summarization.</p>

<p><b>3️⃣ Batch Processing:</b> The system can be upgraded to enable batch processing of multiple video files for large-scale video summarization.</p>


<div align="center">
    <h1>YOUTUBE TRANSCRIPT SUMMARIZER & TRANSLATOR</h1>
</div>

<h2> 🎥Overview</h2>

A **Streamlit-based web application** that extracts YouTube video transcripts, summarizes them based on a selected percentage, translates the summary into multiple languages (including Indian languages), and converts the translated summary into **audio using Text-to-Speech**.

<h2>✨ Features</h2>

- 🔗 Extract transcripts from YouTube videos  
- ✂️ Summarize transcripts using a user-defined percentage  
- 🌍 Translate summaries into multiple global and Indian languages  
- 🔊 Convert translated summaries into speech (MP3 format)  
- 🖥️ Simple, interactive, and user-friendly Streamlit interface

<h2>🛠️ TechStack and Libraries Used</h2>

- **Python**
- **Streamlit** – for building the web UI  
- **youtube-transcript-api** – to fetch YouTube video transcripts  
- **NLTK** – for sentence tokenization  
- **deep-translator** – for translating text  
- **gTTS (Google Text-to-Speech)** – for audio generation  

<h2>▶️ How to Run the Application</h2>

<ol> <li>Open a terminal or command prompt in your project folder.</li> <li>Create a virtual environment to keep your dependencies isolated:</li> </ol>

<pre><code>#Windows python -m venv .venv

macOS / Linux
python3 -m venv .venv</code></pre>

<ol start="3"> <li>Activate the virtual environment:</li> </ol>

<pre><code># Windows .venv\Scripts\activate.ps1

macOS / Linux
source .venv/bin/activate</code></pre>

<ol start="4"> <li>Install the required libraries:</li> </ol>

<pre><code>pip install -r requirements.txt</code></pre>

<ol start="5"> <li>Launch the Streamlit application:</li> </ol>

<pre><code>streamlit run app.py</code></pre>

<ol start="6"> <li>The application will automatically open in your default web browser. If it does not, access it at:</li> </ol>

<pre><code>http://localhost:8501</code></pre>

<h2>🌐 Supported Languages</h2>
<ul>
  <li>English</li>
  <li>Spanish</li>
  <li>French</li>
  <li>German</li>
  <li>Hindi</li>
  <li>Telugu</li>
  <li>Tamil</li>
  <li>Kannada</li>
  <li>Malayalam</li>
  <li>Marathi</li>
  <li>Bengali</li>
  <li>Gujarati</li>
  <li>Punjabi</li>
  <li>Odia</li>
  <li>Assamese</li>
  <li>Urdu</li>
</ul>

<h2>🧠 Application Workflow</h2>
<ol>
  <li>Enter a YouTube video URL</li>
  <li>Fetch the transcript using <code>youtube-transcript-api</code></li>
  <li>Summarize the transcript based on the selected percentage</li>
  <li>Translate the summary into the chosen language</li>
  <li>Convert the translated summary into audio</li>
  <li>Play the audio directly within the application</li>
</ol>

<h2>⚠️ Limitations</h2>
<ul>
  <li>Works only for videos with publicly available transcripts</li>
  <li>Uses extractive summarization, not AI-based abstractive summarization</li>
  <li>Very long transcripts may be truncated due to API limits</li>
  <li>Translation and Text-to-Speech depend on external services</li>
</ul>

<h2>🚀 Future Enhancements</h2>
<ul>
  <li>AI-based abstractive summarization using BERT / GPT</li>
  <li>Keyword-based summaries</li>
  <li>Download summaries as PDF or TXT</li>
  <li>Improved user interface and accessibility</li>
  <li>Support for additional languages</li>
</ul>





