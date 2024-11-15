import tkinter as tk
from tkinter import font  # Asegura la importación de font
from escuelaBaile import EscuelaBaile
from claseBaile import ClaseBaile
from instructor import Instructor
from sesionBaile import SesionBaile
from alumno import Alumno
from nivelClase import NivelClase
from estiloBaile import EstiloBaile

# Programa principal que muestra toda la información en una única ventana, con formato de tabla
def main():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Información de la Escuela de Baile")
    ventana.geometry("500x400")

    # Estilo de fuente
    title_font = font.Font(size=14, weight="bold")
    section_font = font.Font(size=10, weight="bold")
    regular_font = font.Font(size=10)

    # Ejemplos de instancias
    escuela = EscuelaBaile("Danza y Vida", "Av. Principal 123", "9 AM - 9 PM")
    clase_salsa = ClaseBaile("Danza y Vida", "Av. Principal 123", "9 AM - 9 PM", "Salsa", 60)
    instructor = Instructor("Carlos Pérez", "Salsa", 10)
    sesion_salsa = SesionBaile("Escuela de Salsa", "Av. Principal 123", "9 AM - 9 PM", "Salsa", 60, "Carlos Pérez", "Salsa", 10, "2024-11-14")
    alumno = Alumno("Escuela de Salsa", "Av. Principal 123", "9 AM - 9 PM", "Salsa", 60, "Carlos Pérez", "Salsa", 10, "2024-11-14", "Ana López", 25)
    nivel_intermedio = NivelClase("Escuela de Salsa", "Av. Principal 123", "9 AM - 9 PM", "Salsa", 60, "Intermedio")
    estilo_salsa = EstiloBaile("Escuela de Salsa", "Av. Principal 123", "9 AM - 9 PM", "Salsa", 60, "Salsa Cubana")

    # Concatenar toda la información en un solo texto con formato
    informacion = (
        "INFORMACIÓN DE LA ESCUELA DE BAILE\n\n"
        "Escuela:\n"
        f"{escuela.info_escuela()}\n\n"
        "Clase:\n"
        f"{clase_salsa.info_clase()}\n\n"
        "Instructor:\n"
        f"{instructor.info_instructor()}\n\n"
        "Sesión:\n"
        f"{sesion_salsa.info_sesion()}\n\n"
        "Alumno:\n"
        f"{alumno.info_alumno()}\n\n"
        "Nivel:\n"
        f"{nivel_intermedio.info_nivel()}\n\n"
        "Estilo:\n"
        f"{estilo_salsa.info_estilo()}"
    )

    # Crear un widget Text para la información
    text_widget = tk.Text(ventana, wrap="word", padx=10, pady=10)
    text_widget.insert("1.0", informacion)

    # Aplicar estilos a la información
    text_widget.tag_add("title", "1.0", "1.end")
    text_widget.tag_config("title", font=title_font, foreground="blue")

    text_widget.tag_add("section", "3.0", "3.end", "6.0", "6.end", "9.0", "9.end", "12.0", "12.end", "15.0", "15.end", "18.0", "18.end", "21.0", "21.end")
    text_widget.tag_config("section", font=section_font, foreground="black")

    text_widget.tag_add("info", "4.0", "5.end", "7.0", "8.end", "10.0", "11.end", "13.0", "14.end", "16.0", "17.end", "19.0", "20.end", "22.0", "22.end")
    text_widget.tag_config("info", font=regular_font)

    # Deshabilitar edición del widget Text
    text_widget.config(state="disabled")
    text_widget.pack(fill="both", expand=True)

    # Ejecutar el bucle principal de la interfaz gráfica
    ventana.mainloop()

# Ejecuta el programa principal
if __name__ == "__main__":
    main()
