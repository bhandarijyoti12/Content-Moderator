# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pickle
import app

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
filename= "audio-input.wav"

def get_text_from_small_audio(filename):
    with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
        input_audio_data = r.record(source)
        # recognize (convert from speech to text)
        text_format = r.recognize_google(input_audio_data)
        return text_format




def get_text_from_large_audio(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """

    sound_part = AudioSegment.from_wav(path)  
    # split the audio sound into differnet chuncks , here if the silence is 500 miliseconds or more , get chunks
    chunks = split_on_silence(sound_part,
        min_silence_len = 500,
        # adjust this as per your requirement
        silence_thresh = sound_part.dBFS-14,
        # keeping the silence for 1 second
        keep_silence=500,
    )
     # creating a directory to store the audio chunks
    foldername = "audio-chunks"
   
    if not os.path.isdir(foldername):
        os.mkdir(foldername)
    all_text = ""
    # process each chunk 
    for i, c in enumerate(chunks, start=1):
        # exporting the  audio chunks to save it in the directory
        chunk_filename = os.path.join(foldername, f"chunk{i}.wav")
        c.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                all_text += text
    # return the text for all chunks detected
    return all_text



print("\nFull text:", get_text_from_small_audio(filename))


print("\nFull text from large audio function:", get_text_from_large_audio(filename))





