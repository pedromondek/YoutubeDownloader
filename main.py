from pytube import *
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import imageio_ffmpeg as ffmpeg
import subprocess
import os
import shutil
import re

def downloadYoutube():
    inputTypeDownload = input('🔗 Url Video/Playlist:\n')
    if "playlist" in inputTypeDownload or "&list=" in inputTypeDownload:
        downloadPlaylist(inputTypeDownload)
    else:
        folderPath = os.path.join("downloads", "standalone")
        downloadSingle(inputTypeDownload, folderPath)
       
def downloadSingle(link, folderPath, downloadType=None):
    try:
        yt = YouTube(link, use_po_token=True, on_progress_callback=on_progress)

        if downloadType == None:
            print(f'{yt.title} - {yt.author}')
            
            video_streams = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by("resolution").desc()
            print("\n🎞️ Qualidades de VIDEO disponíveis:")
            for i, stream in enumerate(video_streams):
                print(f"{i}: {stream.resolution} - itag={stream.itag} - fps={stream.fps}")

            audio_streams = yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').order_by("abr").desc()
            print("\n🎧 Qualidades de ÁUDIO disponíveis:")
            for i, stream in enumerate(audio_streams):
                print(f"{i}: {stream.abr} - itag={stream.itag}")
            
            downloadType = input('\n📌 Selecione como baixar o video:\n"audio" (m4a) 🎧\n"mp4" 🎥\n"video" (sem som) 🎞️\n"customizado" (video e áudio) 📀\n"exit" 🛑\nDigite a opção:\n').strip().lower()
            while downloadType not in ("mp3", "audio", "mp4", "video", "customizado", "customizada", "custom", "exit"):
                downloadType = input('❌ Opção inválida!\n📌 Selecione como baixar o video:\n"audio" (m4a) 🎧\n"mp4" 🎥\n"video" (sem som) 🎞️\n"customizado" (video e áudio) 📀\n"exit" 🛑\nDigite a opção:\n').strip().lower()
            
        match downloadType:
            case "mp3" | "audio":
                stream = yt.streams.get_audio_only()
                print('🔄🎧 Iniciando download do áudio.')
                stream.download(output_path=folderPath)
                print('✅🎧 Download do áudio concluído.')

                print(f"Operação concluída com sucesso! ✅")
                return True
            case "mp4":
                stream = yt.streams.get_highest_resolution()
                print('🔄🎥 Iniciando download do vídeo.')
                stream.download(output_path=folderPath)
                print('✅🎥 Download do vídeo concluído.')

                print(f"Operação concluída com sucesso! ✅")
                return True
            case "video":
                video_streams = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by("resolution").desc()
                video_stream = video_streams[0]
                print('🔄🎞️ Iniciando download do vídeo sem áudio.')
                video_stream.download(output_path=folderPath , filename=yt.title)
                print('✅🎞️ Download do vídeo sem áudio concluído.')

                print(f"Operação concluída com sucesso! ✅")
                return True
            case "customizado" | "customizada" | "custom":
                video_choice = int(input("\n📌 Escolha o número do vídeo desejado: "))
                audio_choice = int(input("📌 Escolha o número do áudio desejado: "))

                video_stream = video_streams[video_choice]
                audio_stream = audio_streams[audio_choice]

                print(f"\n📍 Selecionado:\n - 🎞️ Video: {video_stream.resolution}\n - 🎧 Áudio: {audio_stream.abr}")

                print(f'\n🔄🎞️ Iniciando download do vídeo.')
                video_filename = yt.title.replace(" ", "_").replace("/", "_").replace(":", "_") + "_video.mp4"
                video_path = video_stream.download(output_path=folderPath, filename= yt.title.replace(" ", "_").replace("/", "_").replace(":", "_") + '_video')
                print('✅🎞️ Download do vídeo concluído.')

                print(f'\n🔄🎧 Iniciando download do áudio.')
                audio_filename = yt.title.replace(" ", "_").replace("/", "_").replace(":", "_") + "_audio.m4a"
                audio_path = audio_stream.download(output_path=folderPath, filename= yt.title.replace(" ", "_").replace("/", "_").replace(":", "_") + '_audio')
                print('✅🎧 Download do áudio concluído.')

                merge = input(f"\n♻️  Juntar os arquivos?\n⚠️  NOTA: Isso pode levar um tempo. (y / n)\n").strip().lower()
                while merge not in ("y", "s", "n"):
                    merge = input("❌ Opção inválida!\n♻️  Juntar os arquivos?\n⚠️  NOTA: Isso pode levar um tempo. (y / n)\n").strip().lower()
                if merge in ("y", "s"):
                    print(f"\n🔄♻️ Iniciando a junção de arquivos.")

                    output_filename = yt.title.replace(" ", "_").replace("/", "_").replace(":", "_") + "_EDITADO.mp4"

                    try:
                        ffmpeg_path = ffmpeg.get_ffmpeg_exe()

                        subprocess.run([
                            ffmpeg_path,
                            "-i", video_filename,
                            "-i", audio_filename,
                            "-c:v", "copy",
                            "-c:a", "aac",
                            "-strict", "experimental",
                            output_filename
                        ], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"❌ Erro ao juntar com ffmpeg: {e}")

                    print(f"\n✅🎥 Video e áudio juntados com sucesso.")

                    print(f"\n🔄🗑️  Apagando video e áudio temporários.")
                    os.remove(video_filename)
                    os.remove(audio_filename)
                    print("✅🗑️  Vídeo e aúdio temporários apagados com sucesso!")


                print(f"Operação concluída com sucesso! ✅")
                return True
            # case "best" | "melhor":
            #     print('teste')
            # return True
            # Talvez seja implementado futuramente
            case "exit":
                print(f"\n⏹️  Encerrado!")
                return True

    except Exception as e:
        print(f"❌ Ocorreu um erro ao tentar baixar um video/áudio: {e}")
        return False
        
def downloadPlaylist(link):
    try:
        yt = Playlist(link)
        totalVideos = len(yt.videos)

        print(f'\n⏸️  Em breve será iniciado o download da playlist: "{yt.title}" do dono "{yt.owner}".')
        if totalVideos > 10:
            print(f'\n🗒️  A playlist contêm "{totalVideos}" videos para baixar.')
        else:
            print(f'\n🗒️  A playlist contêm "{totalVideos}" videos para baixar. Sendo eles:')
            for index, video in enumerate(yt.videos, start=1):
                print(f"#{index} - {video.title} - {video.author} - ({video.watch_url})")
        
        inicializeProcess = input('\n⏯️  Tem certeza que deseja iniciar download da playlist? (y/n)\n').strip().lower()
        if inicializeProcess == "y":
            downloadType = input('\n📌 Selecione como baixar os videos:\n"audio" (m4a) 🎧\n"mp4" 🎥\n"video" (sem som) 🎞️\n"customizado" 📀 (video e áudio) ⚠️ NOTA: Será perguntado a customização para CADA video da playlist)\n"exit" 🛑\nDigite a opção:\n').strip().lower()
            while downloadType not in ("mp3", "audio", "mp4", "video", "customizado", "customizada", "custom", "exit"):
                downloadType = input('❌ Opção Inválida!\n📌 Selecione como baixar os videos:\n"audio" (m4a) 🎧\n"mp4" 🎥\n"video" (sem som) 🎞️\n"customizado" 📀 (video e áudio) ⚠️  NOTA: Será perguntado a customização para CADA video da playlist)\n"exit" 🛑\nDigite a opção:\n').strip().lower()

            print(f'\n▶️  Iniciando processo para download da playlist "{yt.title}" [{totalVideos} videos disponíveis] como "{downloadType}"')
            
            playlistPath = os.path.join("downloads/playlists", re.sub(r'[\\/*?:"<>|]', '_', yt.title)).strip()
            print(f"\n🔄📁 Criando pasta da playlist.")
            if os.path.exists(playlistPath):
                if os.listdir(playlistPath):
                    folderExist = input(f"⚠️ 🗂️  Encontrado uma pasta de mesmo nome ({yt.title}) no diretório de playlists com arquivos existentes.\n⚠️  NOTA: A pasta será refeita e os arquivos deletados, portanto certifique-se que os arquivos não sejam necessários.\nDeseja prosseguir? (y/n)\n").strip().lower()
                    if folderExist != "y":
                        print(f"\n⏏️  Processo encerrado!")
                        return
                    print(f'🔄🗑️  Deletando arquivos e pasta.')
                    shutil.rmtree(playlistPath)
                    print(f'✅🗑️  Arquivos e pasta deletado com sucesso!')
                    print(f'♻️ 📁 Recriando pasta da playlist.')
                    os.mkdir(playlistPath)
                    print(f'✅📂 Nova pasta criada com sucesso!')
                else:
                    print(f'♻️ 📂 Pasta vazia já existente, portanto será utilizada a mesma.')
            else:
                os.mkdir(playlistPath)
                print(f'✅📂 Pasta criada com sucesso!')

            print(f"\n🔄 Iniciando download dos videos:")
            successfulDownloads = 0
            failedDownloads = {
                "fails": 0, 
                "videosLabels": {}, 
                "videosLinks": {}
                }
            for index, video in enumerate(yt.videos, start=1):
                print(f"\n#{index} - {video.title} - {video.author} [{successfulDownloads} / {totalVideos}] 🔄")
                
                try:
                    resultDownload = downloadSingle(video.watch_url, playlistPath, downloadType)
                    if resultDownload:
                        successfulDownloads += 1
                        print(f"#{index} - {video.title} - {video.author} [{successfulDownloads} / {totalVideos}] ✅")
                    else:
                        failedDownloads["fails"] += 1
                        failedDownloads["videosLabels"][index] = f"#{index} - {video.title} - {video.author}"
                        failedDownloads["videosLinks"][index] = video.watch_url
                        print(f"#{index} - {video.title} - {video.author} [{successfulDownloads} / {totalVideos}] ❌")
                except Exception as e:
                    failedDownloads["fails"] += 1
                    failedDownloads["videosLabels"][index] = f"#{index} - {video.title} - {video.author}"
                    failedDownloads["videosLinks"][index] = video.watch_url
                    print(f"#{index} - {video.title} - {video.author} [{successfulDownloads} / {totalVideos}] ❌")
            
            print(f'\n✅ Finalizado download dos videos da playlist "{yt.title}" no formato "{downloadType}"!')
            print(f'  ✅ Bem Sucedidos: [{successfulDownloads} / {totalVideos}]')
            if failedDownloads["fails"] > 0:
                print(f'  ❌ Falharam: [{failedDownloads["fails"]} / {totalVideos}]')
                print(f'    ❌ Videos que falharam:')
                for failed in failedDownloads["videosLabels"]:
                    print(f'      ❌ {failedDownloads["videosLabels"][failed]} - ({failedDownloads["videosLinks"][failed]})')
        else:
            print(f"\n⏹️  Encerrado!")
            return 
    except Exception as e:
        print(f"❌ Ocorreu um erro ao tentar baixar uma playlist: {e}")
        return
    
downloadYoutube()