import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
from gtts import gTTS
from nltk.tokenize import sent_tokenize
import os
import nltk
import pyttsx3

nltk.download("punkt")

st.title("YouTube Transcript Summarizer & Translator")
st.write("Extract transcripts, summarize, translate, and listen to YouTube video summaries!")

def get_transcript(video_url):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item['text'] for item in transcript])
        return full_text
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

def summarize_text_with_limit(text, percentage, char_limit=5000):
    try:
        sentences = sent_tokenize(text)
        num_sentences = max(1, int(len(sentences) * (percentage / 100)))
        summary = " ".join(sentences[:num_sentences])
        
        if len(summary) > char_limit:
            truncated_summary = ""
            for sentence in sentences[:num_sentences]:
                if len(truncated_summary) + len(sentence) + 1 <= char_limit:
                    truncated_summary += sentence + " "
                else:
                    break
            summary = truncated_summary.strip()
        
        return summary
    except Exception as e:
        st.error(f"Error during summarization: {e}")
        return None

def translate_text(text, target_language_code):
    try:
        chunk_size = 5000
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        translated_chunks = [GoogleTranslator(source="auto", target=target_language_code).translate(chunk) for chunk in chunks]
        translated_text = " ".join(translated_chunks)
        return translated_text
    except Exception as e:
        st.error(f"Error during translation: {e}")
        return None

def text_to_speech(text, language_code="en"):
    try:
        tts = gTTS(text, lang=language_code)
        
        audio_file = "summary_audio.mp3"
        tts.save(audio_file)
        
        return audio_file
    
    except Exception as e:
        if language_code == "en":
            try:
                tts = gTTS(text, lang="en-us")  
                tts.save(audio_file)
                return audio_file
            except Exception as e:
                st.error(f"Error converting text to speech (fallback): {e}")
                return None
        else:
            st.error(f"Error converting text to speech: {e}")
            return None

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Odia": "or",
    "Assamese": "as",
    "Urdu": "ur"

}

video_url = st.text_input("Enter YouTube Video URL:", "")
summary_percentage = st.slider("Select Summary Percentage:", 10, 100, 50)
selected_language = st.selectbox("Select Target Language for Translation:", list(languages.keys()))

if st.button("Summarise"):
    if video_url:
        st.info("Fetching transcript...")
        transcript = get_transcript(video_url)
        
        if transcript:
            st.success("Transcript fetched successfully!")
            st.text_area("Transcript:", transcript, height=200)
            
            st.info("Summarizing the transcript...")
            summary = summarize_text_with_limit(transcript, percentage=summary_percentage)
            
            if summary:
                st.success("Summary generated successfully!")
                st.text_area("Summary:", summary, height=150)
                
                st.info("Translating summary...")
                target_language_code = languages[selected_language]
                translated_summary = translate_text(summary, target_language_code)
                
                if translated_summary:
                    st.success("Translation completed!")
                    st.text_area("Translated Summary:", translated_summary, height=150)
                    
                    st.info("Converting summary to audio...")
                    audio_file = text_to_speech(translated_summary, language_code=target_language_code)
                    
                    if audio_file:
                        st.success("Audio generated successfully!")
                        audio_bytes = open(audio_file, "rb").read()
                        st.audio(audio_bytes, format="audio/mp3")
                        os.remove(audio_file)
    else:
        st.warning("Please enter a valid YouTube video URL.")
