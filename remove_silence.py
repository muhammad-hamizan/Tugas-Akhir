import os
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence

# --- Configuration ---
# 1. Define your input and output directories
INPUT_DIR = r"/media/chamomile/SSD/Paper/Dataset/audio_data"
OUTPUT_DIR = "audio_data_processed" # A new folder will be created

# 2. Silence Detection Parameters (YOU WILL NEED TO TUNE THESE)

# silence_thresh: The level (in dBFS) to consider as silence.
# A lower number (e.g., -50) means it will only detect "deader" silence.
# A higher number (e.g., -30) will treat quieter sounds as silence.
# Start with -40 and adjust.
SILENCE_THRESH_DB = -40

# min_silence_len: The minimum duration (in milliseconds) of a silence
# to be considered for "cutting". 1000ms = 1 second.
# For recitation, a shorter value like 500-700ms might be good.
MIN_SILENCE_LEN_MS = 700

# keep_silence: How much silence (in ms) to leave at the beginning
# and end of the "kept" audio chunks. This makes the cuts
# sound less abrupt. 150-250ms is usually good.
KEEP_SILENCE_MS = 200
# --- End Configuration ---


def process_file(input_path, output_path):
    """
    Loads an audio file, removes long silences, and saves the result.
    """
    try:
        # Load the audio file
        sound = AudioSegment.from_mp3(input_path)

        print("  -> Analyzing for silence...")
        # Split the audio into non-silent chunks
        chunks = split_on_silence(
            sound,
            min_silence_len=MIN_SILENCE_LEN_MS,
            silence_thresh=SILENCE_THRESH_DB,
            keep_silence=KEEP_SILENCE_MS
        )

        if not chunks:
            print(f"  -> SKIPPING: File might be all silence or parameters are too strict.")
            return

        # Combine the non-silent chunks back together
        processed_sound = AudioSegment.empty()
        for chunk in chunks:
            processed_sound += chunk

        # Create the parent directory in the output folder (e.g., .../Abdullaah_3awwaad_Al-Juhaynee/)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Export the processed file
        print(f"  -> Exporting processed file to {output_path}")
        processed_sound.export(output_path, format="mp3")

    except Exception as e:
        print(f"  -> FAILED to process {input_path}: {e}")

def main():
    """
    Finds all .mp3 files in the input directory and processes them.
    """
    print("Starting audio processing...")
    print(f"Input directory:  {INPUT_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Silence Threshold: {SILENCE_THRESH_DB} dB")
    print(f"Min Silence Length: {MIN_SILENCE_LEN_MS} ms")
    print("-" * 40)

    input_root = Path(INPUT_DIR)
    output_root = Path(OUTPUT_DIR)

    # Use rglob to find all .mp3 files recursively
    mp3_files = list(input_root.rglob("*.mp3"))
    
    if not mp3_files:
        print(f"No .mp3 files found in '{INPUT_DIR}'.")
        print("Please make sure the script is in the correct location.")
        return

    print(f"Found {len(mp3_files)} .mp3 files to process.")

    for i, input_path in enumerate(mp3_files):
        print(f"\n[{i+1}/{len(mp3_files)}] Processing: {input_path}")
        
        # Determine the corresponding output path
        # e.g., audio_data/Reciter/file.mp3 -> audio_data_processed/Reciter/file.mp3
        relative_path = input_path.relative_to(input_root)
        output_path = output_root / relative_path
        
        process_file(input_path, output_path)

    print("-" * 40)
    print("Processing complete.")
    print(f"All processed files are in the '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    main()