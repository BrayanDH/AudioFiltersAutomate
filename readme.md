# Audio filters automate

The script's main function is to add edition filters to audio files, making them sound better or more polished. These filters are similar to the ones available in the audio editing software, Audacity.

Wou only need put the audios files in the same folder as the script and and run it.

## Filters Applied: The script applies the following filters to the audio files:

+ Noise Reduction: Reduces or removes background noise from the audio.
+ Hardlimiter: Limits the amplitude of the audio to avoid clipping or distortion.
+ Equalizer: Adjusts the frequency response of the audio to enhance or reduce specific frequencies.
+ Compression with Auto Normalizer LVS: Applies dynamic range compression to even out audio levels, and the auto normalizer brings the overall loudness to a desired level.

Silence Removal (Optional): Additionally, users have the option to use the silence script, which removes all silent spaces or pauses from the audio files. This can be helpful for creating a more seamless and continuous audio experience.

FFMPEG Dependency: The script relies on FFMPEG to perform the audio processing tasks. Users need to install FFMPEG to run the script successfully. The description suggests using "chocolatey" as a package manager to install FFMPEG.
**https://community.chocolatey.org/packages/ffmpeg**
