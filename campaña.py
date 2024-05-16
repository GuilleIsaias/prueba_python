from error import LargoExcedidoError
from anuncio import Anuncio, Video
from datetime import date

class Campaña():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.lista_anuncios = []

    @property
    def get_nombre(self):
        return self.nombre
    
    @get_nombre.setter
    def set_nombre(self, nombre: str):
        if len(nombre) > 250:
            raise LargoExcedidoError("El largo del nombre no debe exceder 250 caracteres")
        else: 
            self.nombre = nombre

    @property
    def get_fecha_inicio(self):
        return self.fecha_inicio
    
    @get_fecha_inicio.setter
    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    @property
    def get_fecha_termino(self):
        return self.fecha_termino
    
    @get_fecha_termino.setter
    def set_fecha_termino(self, fecha_termino):
        self.fecha_termino = fecha_termino

    @property
    def get_anuncios(self):
        return self.lista_anuncios

    def set_anuncios(self, anuncio: Video):
        self.lista_anuncios.append(anuncio)

    def __str__(self) -> str:
        cont = {"Video":0, "Display": 0, "Social": 0}
        for anuncio in self.lista_anuncios:
                tipo = type(anuncio).__name__
                cont[tipo] += 1
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {cont['Video']} Video, {cont['Display']} Display, {cont['Social']} Social"
