from yandex_music import Client
from datetime import datetime as dt

'''
    Результатом работы этого кода будет 
    файл и треками, которые стали недоступны
    из-за отзыва правообладателем или какого-либо запрета.
    Результат будет выгружен в папку results внутри проекта.
    
    1) В консоли ввести команду: pip install -U yandex-music
    2) Токен можно получить установив это расширение для Google Chrome: 
       https://chromewebstore.google.com/detail/yandex-music-token/lcbjeookjibfhjjopieifgjnhlegmkib
    3) Запустить код
'''

TOKEN = 'тут должен быть ваш токен'

client = Client(TOKEN).init()

# Получение фамилии и имени + логина пользователя, для вставки в название результата.
info = f"{client.me['account']['login']}_{client.me['account']['full_name']}"

time = dt.now().strftime("%d.%m.%y_%H.%M")

# Получение плейлиста по идентификатору.
# 3 - идентификатор плейлиста "Мне нравится"
playlist = client.users_playlists(3)

# Получение информации по трекам из плейлиста
tracks = playlist.fetch_tracks()

with open(f'results\\{time}_{info}.txt', 'a', encoding='utf-8') as file:
    count = 0
    for track in tracks:
        # Получение информации по каждому треку
        full_track = track.track

        # Если у трека есть признак ошибки, то пишем в файл
        if full_track.error:
            count += 1
            print(f"{count}. {', '.join(full_track.artists_name())} - {full_track.title}", file=file)

    file.close()

