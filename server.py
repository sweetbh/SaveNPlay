from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

# ডাউনলোড ফোল্ডার তৈরি
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Video Downloader API!"})

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"error": "Please provide a video URL!"}), 400

    try:
        # yt-dlp অপশন সেটআপ
        ydl_opts = {
            'outtmpl': f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
            'format': 'best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_title = info_dict.get('title', 'video')
            video_extension = info_dict.get('ext', 'mp4')
            video_filename = f"{DOWNLOAD_FOLDER}/{video_title}.{video_extension}"

        return send_file(video_filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
