# Import the Speech-to-Text client library
from google.cloud import speech
from google.protobuf import wrappers_pb2
import os

# Option 1: Set your Google Cloud API key (service account file)
# Replace this path with your actual service account JSON file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sehajpunitsingh/Desktop/Code/APIKeys/studychain-backend-e47e269395bb.json"

# Instantiates a client
client = speech.SpeechClient()

# The name of the local audio file to transcribe
#local_audio_file = "/Users/sehajpunitsingh/Desktop/Code/Voice-Bot/Financial Lesson from Sikh Religion ｜ Jaspreet Singh [GPK6-gkJIqc].mp3"  # Replace with your actual local file path
local_audio_file = "/Users/sehajpunitsingh/Desktop/Code/Voice-Bot/President Kennedy's 1962 ＂Moon Speech＂ [3YWIIV19U70].mp3"

def transcribe_speech():
  # Read the local audio file
  with open(local_audio_file, "rb") as audio_file:
    content = audio_file.read()
  
  audio = speech.RecognitionAudio(content=content)

  config=speech.RecognitionConfig(
  encoding=speech.RecognitionConfig.AudioEncoding.MP3,
  sample_rate_hertz=48000,
  language_code="en-US",
  model="latest_long",
  audio_channel_count=2,
  enable_word_confidence=True,
  enable_word_time_offsets=True,
  )

  # Detects speech in the audio file
  response = client.recognize(config=config, audio=audio)

  for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))

transcribe_speech()