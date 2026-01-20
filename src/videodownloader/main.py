from pathlib import Path
from threading import Thread

from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp

from .android_utils import is_android, media_scan
from .downloader import download_audio

KV_PATH = Path(__file__).with_name("ui.kv")


class DownloaderApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file(str(KV_PATH))

    def start_download(self, url):
        Thread(target=self._download, args=(url,), daemon=True).start()

    def _download(self, url):
        path = download_audio(url)
        if path and is_android():
            media_scan(path)
        Clock.schedule_once(lambda *_: setattr(self.root.ids.status, "text", "Done"))


def run():
    DownloaderApp().run()
