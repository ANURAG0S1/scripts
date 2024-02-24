
# Music Song Extractor and Downloader

This script extracts music song metadata from URLs and generates a bash script to download the songs as MP3 files using `yt-dlp`.

## Features

- Extracts music song metadata from URLs
- Supports both single songs and playlists
- Generates a bash script for downloading MP3 files from extracted song metadata

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `yt-dlp`

You can install the required Python libraries via pip:

```bash
pip install requests beautifulsoup4 yt-dlp
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ANURAG0S1/scripts.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd scripts
   ```

3. Run the script:

   ```bash
   python3  spo-downloader.py
   ```

4. Enter the URL when prompted.
5. Choose whether it's a single song or a playlist.

   - For a single song, type `S` or `s`.
   - For a playlist, type `P` or `p`.
   - Press Enter to choose the default, which is a playlist.

6. Follow the instructions to complete the process.

## Disclaimer

Please ensure you have the necessary rights and permissions before downloading content from URLs.

---

This README provides an overview of the script's functionality, prerequisites, and usage instructions. You can further customize it based on your project's specific details and requirements.

Feel free to modify and enhance the script as needed! If you encounter any issues or have suggestions for improvement, please don't hesitate to open an issue or pull request on the repository.

Enjoy extracting and downloading your favorite music songs! 🎵🎶