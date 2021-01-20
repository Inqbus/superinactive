# superinactive
supervior plugin to monitor for file activity and restart program on inactivity

This sound silly, but I have an infinite long running `ffmpeg` job, which converts a video stream on the fly.
The file output stills at a certain time but supervisor does not detect the `ffmpeg` as crashed.




Configuration:

    [program:ffmpeg]
    command=ffmpeg ......  -o /home/volker/out.stream

    [program:superinactive]
    command=superinactive /home/volker/out.stream 10 ffmpeg



