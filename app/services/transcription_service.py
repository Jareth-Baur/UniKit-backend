import os
import tempfile

from faster_whisper import WhisperModel


# Load the model once.
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(
    audio_data: bytes,
    filename: str
) -> dict:
    """
    Convert an audio/video file into text.
    """

    extension = os.path.splitext(filename)[1]

    if not extension:
        extension = ".mp3"

    temp_path = None

    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp_file:

            temp_file.write(audio_data)
            temp_path = temp_file.name

        # Transcribe
        segments, info = model.transcribe(
            temp_path,
            beam_size=5
        )

        transcript_segments = []

        for segment in segments:

            transcript_segments.append({
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": segment.text.strip()
            })

        full_text = " ".join(
            segment["text"]
            for segment in transcript_segments
        )

        return {
            "text": full_text,
            "language": info.language,
            "language_probability": round(
                info.language_probability,
                4
            ),
            "segments": transcript_segments
        }

    except Exception as e:

        raise RuntimeError(
            f"Transcription failed: {str(e)}"
        )

    finally:

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)