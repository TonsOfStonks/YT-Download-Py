from __future__ import unicode_literals
import yt_dlp as youtube_dl

ydl_opts = {
    'verbose': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=qU-okJIgafg'])

