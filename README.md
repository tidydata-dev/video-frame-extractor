# Video frame extractor — video to images (examples)

Turn any **video link** (MP4, MOV, WebM, MKV, AVI, OGV… up to 1 GB) into **images**: one frame **every N seconds** or an **exact number of evenly spaced frames**, as JPG, PNG or WebP with timestamps and a **public link per frame**. Hosted on Apify: **[Video Frame Extractor](https://apify.com/tidydata/video-frame-extractor)** — **$2 per 1,000 frames**, no ffmpeg install.

## Python

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tidydata/video-frame-extractor").call(run_input={
    "videoUrls": [{"url": "https://upload.wikimedia.org/wikipedia/commons/3/37/STS-134_launch_2.ogv"}],
    "mode": "interval",      # or "count"
    "everySeconds": 1,
    "format": "jpg",
    "maxWidth": 1280,
})
for f in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f["timeSeconds"], f["imageUrl"])
```

More: [`examples/frames_to_ai_vision.py`](examples/frames_to_ai_vision.py) (describe a video with any vision model) · [`examples/node.mjs`](examples/node.mjs)

## Output per frame

`videoUrl` · `index` · `timeSeconds` · `imageUrl` (public) · `width` · `height` · `format` · `videoDurationSeconds`

Examples are MIT-licensed. Use videos you have the right to process.
