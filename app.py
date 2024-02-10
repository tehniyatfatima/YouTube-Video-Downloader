import streamlit as st
from pytube import YouTube
from threading import Thread

# Function to download video
def download_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        st.success("Your video is downloaded!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Main function for Streamlit app
def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL below:")

    # Input field for the video URL
    video_url = st.text_input("Video URL")

    if st.button("Download"):
        if video_url:
            st.write("Downloading video...")
            # Start downloading the video in a separate thread
            t = Thread(target=download_video, args=(video_url, "./downloads/"))
            t.start()
            t.join()  # Wait for the download to complete
            st.write("Download completed")
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()
print("successfully done")