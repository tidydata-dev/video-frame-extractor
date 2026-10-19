// npm i apify-client  ·  APIFY_TOKEN=... node examples/node.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('tidydata/video-frame-extractor').call({
    videoUrls: [{ url: 'https://example.com/clip.mp4' }],
    mode: 'count', frameCount: 6, format: 'webp', maxWidth: 640,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.map((f) => `${f.timeSeconds}s ${f.imageUrl}`).join('\n'));
