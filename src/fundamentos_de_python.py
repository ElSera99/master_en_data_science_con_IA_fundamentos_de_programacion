#!/usr/bin/env python3

"""
El objetivo de este challenge es aplicar lo aprendido en Python con base en la sesión y lecturas.
Deberás demostrar competencia en:
1) Manejo de datos (variables y tipos)
2) Interactividad (captura/procesamiento de input)
3) Organización de la información (listas y diccionarios).
"""

class Contacto:
    """
    Clase de tipo Contacto que será utilizado para almacenar y 
    obtener la información del contacto.
    """
    def __init__(self, nombre:str, telefono:int, correo:str) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo if correo else ""

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre:str) -> None:
        self.nombre = nombre
        return

    def get_telefono(self) -> int:
        return self.telefono

    def set_telefono(self, telefono:int) -> None:
        self.telefono = telefono
        return

    def get_correo(self) -> str:
        return self.correo

    def set_correo(self, correo:str) -> None:
        self.correo = correo
        return


class Agenda:
    """
    Clase de tipo agenda que sera utilizada para almacenar multiples contactos.
    """
    def __init__(self) -> None:
        self.contactos = []

    def importar_contactos_csv(self, path:str|Path) -> bool:
        pass

    def guardar_contactos_csv(self, nombre_archivo: str, path:str|Path) -> bool:
        pass

    def agregar_contacto(self) -> bool:
        # Obtener entrada de datos del usuario
        nombre = input("Introduce el nombre del contacto: ")
        numero = int(input("Introduce el numero del contacto: "))
        correo = input("Introduce el correo del contacto: ")

        # Crear y guardar contacto
        try:
            nuevo_contacto = self._crear_contacto(nombre, numero, correo)
            self.contactos.append(nuevo_contacto)

            return True
        except Exception as e:
            return False

    def borrar_contacto() -> bool
        pass

    def actualizar_contacto() -> bool
        pass

    def _crear_contacto(self, nombre:str, numero:int, correo:str) -> Contacto:
        contacto = Contacto(nombre, numero, correo) 
        return contacto
