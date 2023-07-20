from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from inference import run_wav2lip
import subprocess
import aiofiles

app = FastAPI(title="Wav2Lip")


async def save_uploaded_files(video, audio):
    # Save the uploaded files to a temporary location
    video_path = f"C:/Users/salwy/OneDrive/code/LipSync/files/{video.filename}"
    audio_path = f"C:/Users/salwy/OneDrive/code/LipSync/files/{audio.filename}"

    async def write_file(file_path, file_content):
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(file_content)

    # Read and write the video and audio files asynchronously
    video_content = await video.read()
    audio_content = await audio.read()
    await write_file(video_path, video_content)
    await write_file(audio_path, audio_content)

    return video_path, audio_path


@app.post("/upload_files/")
async def upload_files(video: UploadFile = File(...), audio: UploadFile = File(...)):
    # Save the uploaded files
    video_path, audio_path = await save_uploaded_files(video, audio)

    # Run Wav2Lip inference with the uploaded files and save the output video
    command = f"cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face {video_path} --audio {audio_path} --nosmooth --pads 20 0 0 0 "
    
    subprocess.run(command, shell=True)



    return {"resuls are generated"}

@app.get("/get_output_video")
async def get_output_video(output_video_path: str):
    # Return the generated output video to the user
    return FileResponse(output_video_path)
