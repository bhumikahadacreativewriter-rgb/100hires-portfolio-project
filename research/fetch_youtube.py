import os
import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return match.group(1) if match else None

def fetch_transcript():
    print("\n--- 🤖 B2B SaaS Data Fetcher Pipeline ---")
    video_url = input("Enter the YouTube Video URL: ").strip()
    expert_name = input("Enter the Expert's Name (e.g., tk_kader): ").strip().lower().replace(" ", "_")
    
    video_id = get_video_id(video_url)
    if not video_id:
        print("❌ Error: Invalid YouTube URL layout.")
        return

    try:
        print("Connecting to API and fetching transcript... please wait...")
        
        # Pull down the transcript using the modern API instance system
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        
        # Ensure the destination directory exists (relative to this script's location)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "youtube-transcripts", expert_name)
        os.makedirs(output_dir, exist_ok=True)
        
        # Save file cleanly
        filename = f"{output_dir}/video_{video_id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for entry in transcript:
                # FIX: We now use dot notation (entry.text) instead of brackets
                f.write(f"{entry.text}\n")
                
        print(f"✅ Success! Data pipeline complete. Saved to: {filename}\n")
    except Exception as e:
        print(f"❌ Error fetching transcript: {e}\n")

if __name__ == "__main__":
    fetch_transcript()
