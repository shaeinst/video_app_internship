import ffmpeg


def video_lenght(video_name):
    info = ffmpeg.probe(video_name)
    duration = info["format"]["duration"]
    return int(float(duration))
