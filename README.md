# pydub-audio-concatenator
For foreign language repetition. You can combine small audio files with sentences into one big with pauses between sentences

Set the folder path where you have .wav audio files with sentences.
```python
folder_name = 'audio'
file_extension_in = ".wav"
```

The scrupt takes length of each sentence and add the same pause. You can also increase the pause by setting extra_silence.

```python
extra_silence = 1000
```

Also set output file name and extension.
```python
file_extension_out = "mp3"
file_name_out = "repeat"
```