# Shared images, BFCM week US

| File | Klaviyo URL | Dimensions | Where it goes | Safe area for text |
|---|---|---|---|---|
| `bfcm-dark-hammered-texture-2400x800.jpg` (uploaded, retina) | https://cdn.klaviyomail.com/company/TdtTzz/images/aa0f4a01-10ed-42f4-8ee1-bcdb50b9a86b.jpeg (Klaviyo image id 406840809, name `bfcm-week-us-shared-texture`) | 2400x800, 117 KB | Background of a banner strip (display at 600x200), e.g. behind the gifts or countdown row | Whole strip. Very dark (about #0d0d0c to #2a2a28), so use white or cream text; no busy hotspots |
| `bfcm-dark-hammered-texture-1200x400.jpg` | not uploaded (local 1x copy) | 1200x400, 51 KB | Same, 1x fallback | Same |

Notes
- Made procedurally (Python, no AI), so there are no artefacts, logos or text. Subtle hammered-metal dimples, faint warm graphite tone, top-left light.
- Seamless in both directions: tiles cleanly as `background-repeat` and can be cropped anywhere.
- Fallback background colour for clients that drop background images: `#111110`.
