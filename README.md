<p id="top">

# Youtube Downloader

<!-- <img src="https://img.shields.io/badge/Project%20Status-In%20Development-yellow" alt="Project Status"> -->
<img src="https://img.shields.io/badge/Project%20Status-Finished-brightgreen" alt="Project Status">
</p>

---

> [!NOTE]
> Caso tenha preferência de ler este documento em "PT-BR <img style="width:13px" src="https://em-content.zobj.net/source/google/387/flag-brazil_1f1e7-1f1f7.png"/>", sinta-se livre para ler **[aqui (LEIAME.md)](LEIAME.md)**

<br>

By following the instructions below, you will be able to download music and videos from YouTube.

<br>

<summary>Details:</summary>
  <ol>
    <li><a href="#⚙️-how-to-run">⚙️ How to Run</a></li>
    <li><a href="#✨-features">✨ Features</a></li>
    <ul>
        <li><a href="#preview-🎞️"> Preview 🎞️</a></li>
        <li><a href="#built-with-🔨"> Built With 🔨</a></li>
    </ul>
  </ol>

---

<br>

# ⚙️ How to Run

### Installing dependencies

- First, install the Python dependencies. Before starting, make sure you have Python version **3.1x+** installed.
- The version tested by me was **v3.12.2**.

```bash
pip install -r requirements.txt
```

- Then, install the PO-Token generator library using npm.

```bash
npm install:all
```

<br>

## Generating PO Token

This step is not essential, and it only needs to be done once. There are three options:

- Generate the PO Token using the potoken.js file (this may take a while or fail due to firewall blocks or network issues)

- Do it manually by following the steps found here: https://pytubefix.readthedocs.io/en/latest/user/po_token.html

_(Remember that you must be logged out when doing this manually, otherwise you risk getting your account banned)_

### Running without a PO Token

- In this third option, you must modify the following line _(ln 20, main.py)_:

From:

`yt = YouTube(link, use_po_token=True, on_progress_callback=on_progress)`

To:

`yt = YouTube(link, 'WEB', on_progress_callback=on_progress)`

### What are the disadvantages of running without a PO Token?

- Access will generate ads in the process, which may slow down downloads or even cause them to fail, especially when downloading playlists.

<br>

# ✨ Features

## Download Types:

- m4a (audio) with the best available audio track;
- mp4 with audio with the best available video track;
- mp4 without audio with the best available video track;
- Custom mode:
  - Allows you to choose which available audio or video tracks to download, since the best video track may not always have the best audio (and vice versa), or to download a lower quality version.
  - After choosing, you can merge the tracks using ffmpeg.
- Playlist recognition — download entire playlists with the same options as above.

<br>

## Preview 🎞️


https://github.com/user-attachments/assets/d76603c5-f833-424d-8f5e-be943ac15baa


<br>

## Built With 🔨

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
  - [pytube](https://github.com/pytube/pytube)
  - [pytubefix](https://github.com/JuanBindez/pytubefix)
  - [YouTube PoToken Generator](https://github.com/YunzheZJU/youtube-po-token-generator)
- ![FFmpeg](https://shields.io/badge/FFmpeg-%23171717.svg?logo=ffmpeg&style=for-the-badge&labelColor=171717&logoColor=5cb85c)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

<p align="right">(<a href="#top">back to top</a>)</p>

> [!IMPORTANT]
> If you have found any bugs or issues, please do not hesitate to report it to me, you can do so either through [github](https://github.com/pedromondek/Whatsapp-2/issues), I will be very grateful, as I am for your visit!

<p align="right">(<a href="#top">back to top</a>)</p>
