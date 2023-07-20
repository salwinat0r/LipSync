import subprocess
def run_wav2lip(video_path:str, audio_path: str):
    """Runs the Wav2Lip model on a given video and audio file."""
    argv = [
        "python3 inference.py",
        "--checkpoint_path", "checkpoints/wav2lip_gan.pth",
        "--face", video_path,
        "--audio", audio_path,
        "--nosmooth",
        "--pads", "20", "0", "0", "0"
    ]
    return argv
video_path = "files/input_video.mp4"
audio_path = "files/input_audio.wav"
x = run_wav2lip(video_path, audio_path)

subprocess.run("cd Wav2Lip && python inference.py", shell=True)
# subprocess.run("cd Wav2Lip", shell=True)
# subprocess.run(x, shell=True)