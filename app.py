import streamlit as st
from pytube import YouTube 
from threading import Thread
import os

# Function to download video
def download_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        st.success(f"Your video is downloaded and saved in: {save_path}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Main function for Streamlit app
def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL below:")

    # Input field for the video URL
    video_url = st.text_input("Video URL")

    # Detecting the platform (mobile or desktop)
    is_mobile = st.sidebar.radio("Select your platform:", ["Mobile", "Desktop"]) == "Mobile"

    # Input field for the save location
    if is_mobile:
        default_save_location = "/storage/emulated/0/Download"  # Default download folder on Android
        st.write(f"You are using a mobile device. The default save location is set to: {default_save_location}")
    else:
        default_save_location = os.path.join(os.path.expanduser("~"), "Downloads")  # Default download folder on desktop
        st.write(f"You are using a desktop device. The default save location is set to: {default_save_location}")

    save_location = st.text_input("Enter the directory where you want to save the downloaded video:", default_save_location)
    
    if st.button("Download"):
        if video_url:
            st.write("Downloading video...")
            # Start downloading the video in a separate thread
            t = Thread(target=download_video, args=(video_url, save_location))
            t.start()
            t.join()  # Wait for the download to complete
            st.write("Download completed")
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()
