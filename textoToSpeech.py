import os

# Set your Google Cloud API key (service account file)
# Replace this path with your actual service account JSON file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sehajpunitsingh/Desktop/Code/APIKeys/studychain-backend-e47e269395bb.json"

def synthesize_ssml():
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    """
    from google.cloud import texttospeech

    ssml = "<speak>Hello there</speak>"
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

# Call the function to execute it
if __name__ == "__main__":
    synthesize_ssml()
