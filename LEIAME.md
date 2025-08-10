<p id="top">

# Youtube Downloader

<!-- <img src="https://img.shields.io/badge/Project%20Status-In%20Development-yellow" alt="Project Status"> -->
<img src="https://img.shields.io/badge/Project%20Status-Finished-brightgreen" alt="Project Status">
</p>

---

> [!NOTE]
> If you prefer to read this document in "EN-US <img style="width:13px" src="https://em-content.zobj.net/source/google/387/flag-united-states_1f1fa-1f1f8.png"/>", feel free to read it in **[here (README.md)](README.md)**

<br>

Seguindo as instruções você poderá realizar o download de músicas e videos do Youtube.

<br>

<summary>Detalhes:</summary>
  <ol>
    <li><a href="#⚙️-Como-Rodar">⚙️ Como Rodar</a></li>
    <li><a href="#✨-Features">✨ Features</a></li>
    <ul>
        <li><a href="#Preview-🎞️"> Preview 🎞️</a></li>
        <li><a href="#Construido-Com-🔨"> Construido Com 🔨</a></li>
    </ul>
  </ol>

---

<br>

# ⚙️ Como Rodar

### Instalando dependências

- Começamos então instalando nossas dependências do python, portanto antes de começar certifique-se que está com uma versão **3.1x+** do Python instalada.
- A versão testada por mim foi a **v3.12.2**.

```bash
pip install -r requirements.txt
```

- Feito isto, faltará agora a biblioteca de geração de PO-Token, agora usando npm.

```bash
npm install:all
```

<br>

## Gerando PO Token

Essa etapa não é essencial, porém ela é feita uma única vez. Há três opções:

- Gerar o PO Token pelo arquivo `potoken.js` (o que pode ser um pouco demorado ou falhar por algum bloqueio de firewall ou problema de rede)
- Fazê-lo manualmente seguindo as etapas que podem ser encontradas por aqui: https://pytubefix.readthedocs.io/en/latest/user/po_token.html

_(lembre-se que você deve estar deslogado para fazer essa etapa manualmente, pois corre o risco de ter sua conta banida)_

### Rodar sem PO Token

- Nesta terceira opções, caso o faça, deverá ser modificado a seguinte linha _(ln 20, main.py)_:

De:

`yt = YouTube(link, use_po_token=True, on_progress_callback=on_progress)`

Para:

`yt = YouTube(link, 'WEB', on_progress_callback=on_progress)`

### Quais as desvantagens de usar sem o PO Token?

- O acesso gerará ads no processo, o que pode fazer com que o download seja mais demorado ou até mesmo falhe, especialmente no download de playlists.

<br>

# ✨ Features

## Tipos de Downloads:

- m4a (áudio) com a melhor faixa de áudio disponível;
- mp4 com a melhor faixa de video disponível;
- mp4 sem áudio com a melhor faixa de video disponível;
- Customizado:
  - Permite personalizar quais das faixas disponíveis de áudio ou video deseja baixar, por que nem sempre a melhor versão de video possui a melhor versão de áudio (e vice-versa), ou até mesmo para baixar uma versão com qualidade reduzida.
  - Após as escolhas, é possível escolher juntar as faixas que será feito através do ffmpeg.
- Reconhecimento de playlist, é possível através instalar playlists com esses mesmos tipos relatados.

<br>

## Preview 🎞️

<video src="https://github.com/user-attachments/assets/d76603c5-f833-424d-8f5e-be943ac15baa" controls></video>

<br>

## Construido Com 🔨

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
  - [pytube](https://github.com/pytube/pytube)
  - [pytubefix](https://github.com/JuanBindez/pytubefix)
  - [YouTube PoToken Generator](https://github.com/YunzheZJU/youtube-po-token-generator)
- ![FFmpeg](https://shields.io/badge/FFmpeg-%23171717.svg?logo=ffmpeg&style=for-the-badge&labelColor=171717&logoColor=5cb85c)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

<p align="right">(<a href="#top">back to top</a>)</p>

> [!IMPORTANT]
> Se você encontrou algum bug ou problema, porfavor não hesite em me relatar, você pode fazer isso por meio do [github](https://github.com/pedromondek/Whatsapp-2/issues), ficarei muito grato, assim como estou pela sua visita!

<p align="right">(<a href="#top">volte ao topo</a>)</p>
