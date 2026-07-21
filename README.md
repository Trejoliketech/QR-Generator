# QR Code Generator

A simple, ad-free QR code generator — no trackers, no paywalls, no premium tier. Type in a URL and get a QR code.

**Live demo:** [your-free-qr-generator.onrender.com](https://your-free-qr-generator.onrender.com) *(free tier may take 30-60s to wake up on first load)*

## Why

I thought something as simple as generating QR codes shouldn't be jumping through hoops or clicking close on ads. This also doubles as a first full stack project of mine that I'll continue to add features onto and support.

## Features

- Generates a scannable QR code from any text or URL
- No ads and no accounts needed
- Server-side input validation ie length limits, whitespace handling
- Rate limiting to prevent abuse (10 requests/minute per IP)
- Images generated in-memory on request — nothing is ever written to disk, so there's no accumulating storage or cleanup needed
- Clean, minimal, novice UI

## Tech Stack

- **Backend:** Python, Flask
- **Templating:** Jinja2
- **QR generation:** `qrcode` + Pillow
- **Rate limiting:** Flask-Limiter
- **Styling:** hand-written CSS (Flexbox)
- **Production server:** Gunicorn
- **Hosting:** Render

## Security Considerations

- All user input is validated and length-capped server side before use
- Rate limiting is applied per-IP
- debug mode is disabled in production to avoid leaking stack traces
- QR images are generated fresh per request in memory (`io.BytesIO`) rather than saved to disk

## Running Locally

```bash
git clone https://github.com/Trejoliketech/QR-Generator.git
cd QR-Generator
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000`.

## What This Project Was

This was my first full Python project. I leveraged AI tools during development while ensuring the app remained secure to the best of my ability and accomplished what it was meant to do. It helped me understand full stack development just a little better and I hope it serves to help even one individual out there.
