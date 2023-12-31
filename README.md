# ListSync 👄
A Deep Learning app that lip syncs any audio to a video or image.

## Aim
- Video - [input_video.mp4](https://openinapp.co/5cwva)
- Audio - [input_audio.wav](https://openinapp.co/o9vuj)

**Output**

<a href="https://github-production-user-asset-6210df.s3.amazonaws.com/72353689/255168903-f9047d31-c30e-4611-bd48-54a520719121.mp4"><img src="results.gif" width="240" height="150"/>
</a>

## Demo
Watch the Demonstration:  
https://www.loom.com/share/dddbc63922714899a7c15b2eeba692d7?sid=1814f160-f917-465d-8b4f-c84901655782

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
