from campaña import Campaña
from anuncio import Video
from datetime import datetime
from error import Error, LargoExcedidoError
import os

video_anuncio = Video(8, "stream", "demo.mp4", "www.demo.cl")
camp = Campaña("hola mundo", "2024, 5, 15", "2024,5,16")

try:
    nuevo_nombre_campaña = (input("Ingrese un compre para la campaña: \n"))
    camp.set_nombre(nuevo_nombre_campaña)
except Exception as e:
    with open ("error.log", "w") as log:
        log.seek(0)
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0)
        log.close()




