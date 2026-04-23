#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from datetime import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ============================================
# Placeholder URLs – replace later with your real cloud links
# ============================================
PROFILE_PIC_URL = "https://via.placeholder.com/150x150/4facfe/ffffff?text=HS"
MEMORY_PHOTOS = [
    {"name": "Group on steps", "url": "https://via.placeholder.com/400x400/fa709a/ffffff?text=Memory+1"},
    {"name": "Selfie", "url": "https://via.placeholder.com/400x400/4facfe/ffffff?text=Memory+2"},
    {"name": "Dinner 9:09", "url": "https://via.placeholder.com/400x400/ffd700/ffffff?text=Memory+3"},
    {"name": "Pizza Night", "url": "https://via.placeholder.com/400x400/6bcb77/ffffff?text=Memory+4"},
    {"name": "Indoor Vibes", "url": "https://via.placeholder.com/400x400/fa709a/ffffff?text=Memory+5"}
]
MUSIC_TRACKS = [
    {"name": "Happy Birthday Funk", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"}
]
SURPRISE_WISHES = [
    {"name": "Friend 1", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"}
]

# ============================================
# Data
# ============================================
FRIENDSHIP_START = datetime(2026, 2, 22, 14, 30)

GATE = [
    {"id":1,"en":"What makes you smile every morning? 🌅","si":"උදේ පාන්දර ඔබව සිනහවට පත් කරන්නේ කුමක්ද? 🌅","ta":"காலையில் உங்களை சிரிக்க வைப்பது எது? 🌅"},
    {"id":2,"en":"If your heart had a color today, what would it be? 💙","si":"අද ඔබේ හදවතට වර්ණයක් තිබුනේ නම්, එය කුමක්ද? 💙","ta":"இன்று உங்கள் இதயத்திற்கு ஒரு நிறம் இருந்தால், அது என்ன? 💙"},
    {"id":3,"en":"What flower reminds you of yourself? 🌸","si":"ඔබව මතක් කරන මල කුමක්ද? 🌸","ta":"உங்களை நினைவூட்டும் மலர் எது? 🌸"}
]

QUOTES = {
    "en": ["🌸 Where you are, flowers bloom","💙 Your soul is blue skies","🎵 You are music"],
    "si": ["🌸 ඔබ ඉන්න තැන මල් පිපෙනවා","💙 ඔබේ ආත්මය නිල් අහස","🎵 ඔබ සංගීතය"],
    "ta": ["🌸 நீ இருக்கும் இடத்தில் பூக்கள் மலர்கின்றன","💙 உன் ஆன்மா நீல வானம்","🎵 நீ இசை"]
}

def friendship_stats():
    delta = datetime.now() - FRIENDSHIP_START
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    percent = min(100, int((days / 60) * 100)) if days < 60 else 100
    return {"days":days,"hours":hours,"minutes":minutes,"seconds":seconds,"percent":percent}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/init')
def init():
    return jsonify({
        "gate": GATE,
        "profile_url": PROFILE_PIC_URL,
        "memories": MEMORY_PHOTOS,
        "music": MUSIC_TRACKS,
        "wishes": SURPRISE_WISHES,
        "friendship": friendship_stats()
    })

@app.route('/api/quote/<lang>')
def quote(lang):
    return jsonify({"quote": random.choice(QUOTES.get(lang, QUOTES["en"]))})

@app.route('/api/friendship')
def friendship():
    return jsonify(friendship_stats())

# No need for app.run() – Vercel will call the WSGI app
