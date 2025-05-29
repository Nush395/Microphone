import whisper
import argparse
import logging
import os # For checking file existence

def transcribe_audio(audio_path, model_name="turbo") -> str | list[str] | None:
    """
    Transcribes an audio file using OpenAI Whisper and saves the transcription
    to a specified output file.

    Args:
        audio_path (str): The path to the input audio file.
        model_name (str): The name of the Whisper model to use. Defaults to "turbo".
    """
    print(f"Loading Whisper model: {model_name}...")
    try:
        model = whisper.load_model(name=model_name)
    except Exception as e:
        print("Please ensure you have a valid model name (e.g., tiny, base, small, medium, large, turbo).")
        raise RuntimeError(f"Error loading Whisper model '{model_name}': {e}")

    if not os.path.exists(audio_path):
        raise RuntimeError(f"Error: Audio file not found at '{audio_path}'")

    print(f"Transcribing audio file: {audio_path}...")
    try:
        result = whisper.transcribe(model=model, audio=audio_path)
        transcribed_text = result["text"]
    except Exception as e:
        raise RuntimeError(f"Error during transcription: {e}")
    return transcribed_text

def save_to_file(transcribed_text: str, output_path: str):
    print(f"Transcription complete. Saving to: {output_path}")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcribed_text)
        print("Successfully saved transcription.")
    except IOError as e:
        print(f"Error writing to output file '{output_path}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file using OpenAI Whisper.")
    parser.add_argument(
        "--audio_file",
        "-a",
        type=str,
        required=True,
        help="Path to the input audio file (e.g., audio.mp3)."
    )
    parser.add_argument(
        "--output_file",
        "-o",
        type=str,
        default="output.txt",
        help="Path to save the transcribed text (e.g., output.txt)."
    )
    parser.add_argument(
        "--model_name",
        "-m",
        type=str,
        default="base", # Default model
        help="Name of the Whisper model to use (e.g., tiny, base, small, medium, large, large-v2, large-v3). Default is 'base'."
    )

    args = parser.parse_args()

    effective_model_name = args.model_name

    text = transcribe_audio(args.audio_file, effective_model_name,)
    save_to_file(text, args.output_file,)