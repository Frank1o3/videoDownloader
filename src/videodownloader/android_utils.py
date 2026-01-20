import sys

from jnius import autoclass


def is_android():
    return sys.platform == "android"


def media_scan(path) -> None:
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    MediaScanner = autoclass("android.media.MediaScannerConnection")
    MediaScanner.scanFile(PythonActivity.mActivity, [path], None, None)


def get_download_dir():
    Environment = autoclass("android.os.Environment")
    return Environment.getExternalStoragePublicDirectory(
        Environment.DIRECTORY_DOWNLOADS
    ).getAbsolutePath()
