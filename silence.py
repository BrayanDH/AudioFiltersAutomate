import os
import time

files = os.getcwd()
cut = os.listdir(files)
for cutter in cut:
    name, extension = os.path.splitext(cutter)
    if extension not in [".mp3", ".wav"]:
        continue
    name_complete = f"{name}{extension}"
    print("procesando audio " + name_complete)
    os.system(f'ffmpeg -y -i {name_complete} -af silenceremove=stop_periods=-1:stop_duration=1.5:stop_threshold=-50dB {name}-eddit.wav')
