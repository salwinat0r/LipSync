# ListSync 👄
A Deep Learning app that lip syncs any audio to a video or image.

## Aim
- Video - [input_video.mp4](https://openinapp.co/5cwva)
- Audio - [input_audio.wav](https://openinapp.co/o9vuj)

## Demo
Watch the Demonstration:  
https://www.loom.com/share/dddbc63922714899a7c15b2eeba692d7?sid=2aba14f9-13cb-4bd9-8ffd-5c7cc0c2043e

## Installation
To install the neccessary dependancies to use this project:

- Create and activate a virtual environment using virtualenv,
```bash
python3 -m venv lipsync
lipsync/Scripts/activate
```

- Now run this,
```bash
pip install -r requirements.txt
```

## API
The POST method  `/upload_files/` in the `main.py` takes the audio and video input files and outputs the result in `Wav2Lip/results/result_voice.mp4`.