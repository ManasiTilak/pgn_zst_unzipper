# PGN Zstd Unzipper

This Python script allows you to decompress Zstandard (Zstd) compressed PGN files.

## Overview

This project provides a Python script to decompress large Zstd-compressed PGN files. It utilizes the Zstandard compression library and can be run from the command line. Works on databases from lichess.org, chess.com and many others. Max file size: 1gb.
NOTE: Uncompressed files are around 5-6 thimes the compressed file. Make sure you have enough space accordingly.

## Requirements

- Python 3.x
- Zstandard library (install with `pip install zstandard`)

## Usage

1. Clone the repository or download the script.

2. Ensure Python and the Zstandard library are installed on your system. Use `pip install -r requirements.txt` to install if needed.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. In the script replace : Input_file and Output_file paths with your desired paths

4. Run the script with the following command:

   ```bash
   python unzipper.py

