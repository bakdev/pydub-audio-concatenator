from pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import os

folder_name = 'audio'
file_extension_in = ".wav"
extra_silence = 1000  # in msc. Add extra time to pause between sentences
file_extension_out = "mp3"
file_name_out = "repeat"

# looking for audio files in the folder
audio_files = [(folder_name+os.sep+f) for f in os.listdir(folder_name) if Path(f).suffix == file_extension_in]
audio_files.sort(reverse=True)


print('Start creating combined file \n')
combined_wav = AudioSegment.empty()
for wav_path in audio_files:
    wav_chunk = AudioSegment.from_wav(wav_path)
    original_tags = mediainfo(wav_path)
    wav_chunk_pause = len(wav_chunk) + extra_silence  # length of the chunk + extra silence
    combined_wav += wav_chunk + AudioSegment.silent(wav_chunk_pause)
if not audio_files:
    print('no files found')
    exit()

print('Start export')
combined_wav.export(
    folder_name+os.sep+file_name_out+'.'+file_extension_out,
    format=file_extension_out,
    bitrate=original_tags["bit_rate"],
    tags=original_tags["TAG"]
)



