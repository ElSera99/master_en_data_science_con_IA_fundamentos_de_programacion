#!/usr/bin/env python3

"""
El objetivo de este challenge es aplicar lo aprendido en Python con base en la sesión y lecturas.
Deberás demostrar competencia en:
1) Manejo de datos (variables y tipos)
2) Interactividad (captura/procesamiento de input)
3) Organización de la información (listas y diccionarios).
"""

import logging
from pathlib import Path

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
        """
        TO DO:
            - Revisitar una estructura de datos diferente para almacenar y leer los contactos mas rapido: hasmap?
            - Revisitar implementacion: deberia ser privada o publica el atributo de contactos?
        """
        self.contactos = []
        logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s', level=logging.INFO)

    def importar_contactos_csv(self, path:str|Path) -> bool:
        """
        TO DO:
            - Implementar
        """
        pass

    def guardar_contactos_csv(self, nombre_archivo: str, path:str|Path) -> bool:
        """
        TO DO:
            - Implementar
        """
        pass

    def agregar_contacto(self) -> None:
        """
        TO DO:
            - Validar que las entradas sean validas
            - Crear condicion para que el correo sea opcional
            - Validar que el contacto sea creado correctamente
        """
        logging.debug("Proceso de añadir contacto iniciado")

        # Obtener entrada de datos del usuario
        nombre = input("Introduce el nombre del contacto: ")
        telefono = int(input("Introduce el telefono del contacto: "))
        correo = input("Introduce el correo del contacto: ")

        # Crear y guardar contacto
        nuevo_contacto = self._crear_contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)

        logging.debug("Proceso para añadir contacto finalizado")
        logging.info("Contacto creado.")

        return

    def ver_contacto(self, nombre:str) -> None:
        logging.debug("Proceso para ver contacto iniciado")
        for contacto in self.contactos:
            if contacto.get_nombre() == nombre:
                print(f"Nombre del contacto: {contacto.get_nombre()}")
                print(f"Telefono del contacto: {contacto.get_telefono()}")
                print(f"Correo del contacto: {contacto.get_correo()}")
                break
        logging.debug("Proceso para ver contacto finalizado")


    def borrar_contacto(self, nombre:str) -> None:
        """
        TO DO:
            - Validar que el contacto a eliminar sea el correcto
        """
        logging.debug("Proceso para borrar contacto iniciado")
        # Borrar contacto
        for i in enumerate(self.contactos):
            if self.contactos[i].get_nombre() == nombre:
                deleted = self.contactos.pop(i)
                print("Contacto a borrar:")
                print(f"Nombre: {deleted.get_nombre()}")
                print(f"Telefono: {deleted.get_telefono()}")
                print(f"Correo: {deleted.get_correo()}")
                break
        logging.debug("Proceso para borrar contacto finalizado")

        logging.info("Contacto borrado correctamente")
        return

    def actualizar_contacto(self, nombre:str) -> bool:
        """
        TO DO:
            - Crear condiciones para solo modificar los atributos necesarios
        """
        logging.debug("Proceso para actualizar contacto iniciado")
        for contacto in self.contactos:
            if contacto.get_nombre() == nombre:
                # Obtener nuevos valores
                nuevo_nombre = input("Introduzca el nuevo nombre: ")
                nuevo_numero = int(input("Introduzca el nuevo telefono: "))
                nuevo_correo = input("Introduzca el nuevo correo: ")

                # Actualizar
                contacto.set_nombre(nuevo_nombre)
                contacto.set_numero(nuevo_numero)
                contacto.set_correo(nuevo_correo)

                break
        logging.debug("Proceso para actualizar contacto finalizado")
        logging.info("Contacto actualizado correctamente")
        return 

    def _crear_contacto(self, nombre:str, numero:int, correo:str) -> Contacto:
        logging.debug("Proceso para crear instancia de contacto iniciado")
        contacto = Contacto(nombre, numero, correo)
        logging.debug("Proceso para crear instancia de contacto finalizado")
        return contacto


if __name__ == "__main__":
    agenda:Agenda = Agenda()
    nombre:str = "Serafin Tierrafria Baez"

    agenda.agregar_contacto()
    agenda.ver_contacto(nombre)

