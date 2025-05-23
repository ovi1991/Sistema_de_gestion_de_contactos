import json
import os
import re

class Contacto:
    def __init__(self,nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data):
        return Contacto(data['nombre'], data['telefono'], data['email'])
    


class GestionContactos:
    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    datos = json.load(f)
                    return [Contacto.from_dict(c) for c in datos]
            except Exception as e:
                print(f"Error al cargar contactos: {e}")
                return []
        return []
            
    def guardar_contactos(self):
        try:
            print("Guardando contactos...")
            with open(self.archivo, "w") as f:
                json.dump([c.to_dict() for c in self.contactos], f, indent=2)
        except Exception as e:
            print(f"Error al guardar contactos: {e}")
    
    def obtener_contactos(self):
        return [c.to_dict() for c in self.contactos]
    

    def agregar_contacto(self, nombre, telefono, email):
        if not nombre or not telefono or not email:
            raise ValueError("Todos los campos son obligatorios")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Correo electrónico inválido")

        nuevo = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo)
        self.guardar_contactos()
        return nuevo.to_dict()

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto.to_dict()
        return None

    def eliminar_contacto(self, nombre):
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre.lower() == nombre.lower():
                eliminado = self.contactos.pop(i)
                self.guardar_contactos()
                return eliminado.to_dict()
        return None
    
