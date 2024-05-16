class Error(Exception):
    def __init__(self, mensaje: str) -> None:
        self.mensaje = mensaje

class LargoExcedidoError(Error):
    def __init__(self) -> None:
        super().__init__()

class SubTipoInvalidoError(Error):
    def __init__(self) -> None:
        super().__init__()

