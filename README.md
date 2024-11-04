# FileShare 
[![Testing](https://github.com/Hunter87ff/FileShare/actions/workflows/python-app.yml/badge.svg)](https://github.com/Hunter87ff/FileShare/actions/workflows/python-app.yml)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Tested on Windows](https://img.shields.io/badge/Tested%20on-Windows|linux|Android-brightgreen.svg)](https://www.microsoft.com/windows/)

This Python project provides a simple file-sharing application over a local network using Flask. Users can upload files through a web interface and receive a URL for downloading the uploaded files. The application generates a QR code for easy access to the file-sharing URL.

## Installation 
```bash
git clone https://github.com/Hunter87ff/FileShare.git
```
```bash
cd FileShare/src
```
```bash
pip install -r requirements.txt
```
```bash
python main.py  #for windows
python3 main.py #for linux
```
## QR Code Generation (Windows Only)
- Generates a QR code for the file-sharing URL.
- Saves the QR code as "url_qr.png" (temporary file for display).
- Displays the QR code and removes the temporary file.

## Note 
tkinter might not work properly with linux. in that case you won't get any qr code popup, instead you'll get the local address in the terminal. just you have to open that url into the other device, from which the data will be shared.
