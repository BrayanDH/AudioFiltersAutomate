import os
import time
from os import path
import shutil

# get directory and files list
get_files = os.getcwd()
files_explorer = os.listdir(get_files)
filter_register = ""

# get audio archives and commands
for files in files_explorer:
    name, extension = os.path.splitext(files)
    if extension in [".wav", ".mp3"]:
        name_complete = f"{name}{extension}"
        print("processing audio " + name_complete)
        commands_list = ['"highpass=f=300,asendcmd=0.0 afftdn sn start,asendcmd=1.5 afftdn sn stop,afftdn=nf=-20,lowpass=f=3000"',
                         '"equalizer=f=5000:g=2,equalizer=f=100:g=3"',
                         '"compand=attacks=0:points=-80/-900|-45/-15|-27/-9|0/-7|20/-7:gain=5"']

        # Aplly filters
        counter = 1
        for command in commands_list:
            if counter == 1:
                noise_reduction = f'ffmpeg -i {name}{extension} -af {command} {name}{counter}.wav'
                os.system(noise_reduction)

            if counter != 1:
                equalize = f'ffmpeg -i {name}{counter - 1}.wav -af {command} {name}{counter}.wav'
                os.system(equalize)
                last_number = counter - 1
                os.remove(f'{name}{last_number}.wav')
                filter_register = f"{name}{counter}.wav"

            counter += 1

        # Save the original archive
        try:
            dir_original_file = "processed"
            if path.exists('processed') == False:
                os.mkdir('processed')
                shutil.move(name_complete, dir_original_file)
            elif path.exists('processed') == True:
                shutil.move(name_complete, dir_original_file)
        except shutil.Error:
            print("the files is already in folder")

        # Save the processed archive
        rename = name + "-eddit" + ".wav"
        os.rename(filter_register, rename)


print(f"Filters apply with not problems")
