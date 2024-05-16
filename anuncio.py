from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio():
    SUB_TIPOS = ()
    FORMATO = ""

    def __init__(self, ancho, alto, sub_tipo, url_arrchivo = "", url_clic= ""):
        self.ancho = ancho
        self.alto = alto
        self.sub_tipo = sub_tipo
        self._url_archivo = url_arrchivo
        self.url_clic = url_clic
        
    @property
    def get_alto(self):
        return self.alto
    
    @property
    def get_ancho(self):
        return self.ancho
    
    @property
    def get_url_archivo(self):
        return self._url_archivo
    
    @property 
    def get_url_clic(self):
        return self.url_clic
    
    @property
    def get_sub_tipo(self):
        return self.sub_tipo
    
    @get_alto.setter
    def set_alto(self, alto):
        if alto > 0:
            self.alto = alto
        else:
            self.alto = 1
    
    @get_ancho.setter
    def set_ancho(self, ancho):
        if ancho > 0:
            self.ancho = ancho
        else:
            self.ancho = 1

    @get_url_archivo.setter
    def set_url_archivo(self, url_archivo):
        self._url_archivo = url_archivo

    @get_url_clic.setter
    def set_url_clic(self, url_clic):
        self.url_clic = url_clic

    @get_sub_tipo.setter
    def set_sub_tipo(self, tipos):
        if tipos not in self.SUB_TIPOS:
             raise SubTipoInvalidoError(f"Sub Tipo {tipos} no es valido.")
        else:
            self.sub_tipo = tipos

    @staticmethod
    def mostrar_formatos():
        print(f'FORMATO 1: {Anuncio.FORMATO}\n=========\n-{Anuncio.SUB_TIPOS[0]}\n-{Anuncio.SUB_TIPOS[1]}')

    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, duracion, sub_tipo, url_arrchivo="", url_clic=""):
        super().__init__(1, 1, sub_tipo, url_arrchivo, url_clic)
        self.duracion = duracion

    @property
    def get_duracion(self):
        return self.duracion
    
    @get_duracion.setter
    def set_duracion(self, duracion):
        if duracion > 0:
            self.duracion = duracion
        else:
            self.duracion = 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print( "RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    def __init__(self, ancho, alto, sub_tipo, url_arrchivo="", url_clic=""):
        super().__init__(ancho, alto, sub_tipo, url_arrchivo, url_clic)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self, ancho, alto, sub_tipo, url_arrchivo="", url_clic=""):
        super().__init__(ancho, alto, sub_tipo, url_arrchivo, url_clic)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

