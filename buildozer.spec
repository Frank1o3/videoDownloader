[app]
source.dir = .
source.include_exts = py,kv,png

requirements = python3,kivy,kivymd,yt-dlp,mutagen,pillow,ffmpeg,pyjnius

entrypoint = videodownloader.main:run
