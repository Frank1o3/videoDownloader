import io
import os
from pathlib import Path

from mutagen.mp4 import MP4, MP4Cover
from PIL import Image
import yt_dlp

DOWNLOAD_DIR = Path.home() / "Downloads"

def embed_cover(m4a: str, thumb: str) -> None:
    audio = MP4(m4a)
    img = Image.open(thumb).convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    audio["covr"] = [MP4Cover(buf.getvalue())]
    audio.save()

def download_audio(url: str) -> str:
    opts: dict[str, str|bool]= {
        "format": "bestaudio[ext=m4a]/bestaudio",
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "writethumbnail": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True, process=False)
        path = ydl.prepare_filename(info)

    base = os.path.splitext(path)[0]
    thumb = next(
        (base + ext for ext in (".jpg", ".png", ".webp") if os.path.exists(base + ext)),
        None,
    )

    if thumb:
        embed_cover(path, thumb)
        os.remove(thumb)

    return path
