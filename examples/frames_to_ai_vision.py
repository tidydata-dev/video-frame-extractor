"""Sample 8 frames of a video and build a prompt for any vision model (OpenAI, Anthropic, Gemini…). pip install apify-client"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tidydata/video-frame-extractor").call(run_input={
    "videoUrls": [{"url": "https://example.com/your-video.mp4"}],
    "mode": "count", "frameCount": 8, "format": "webp", "maxWidth": 768,
})
frames = list(client.dataset(run["defaultDatasetId"]).iterate_items())
content = [{"type": "text", "text": "These are frames of one video in order. Describe what happens."}]
for f in frames:
    content.append({"type": "text", "text": f"t = {f['timeSeconds']} s"})
    content.append({"type": "image_url", "image_url": {"url": f["imageUrl"]}})  # adapt to your provider's image format
print(len(frames), "frames ready to send as one multimodal message")
