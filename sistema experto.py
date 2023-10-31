# Importar las bibliotecas necesarias
import tkinter as tk
from tkinter import ttk

# Definir la base de conocimientos
base_conocimientos = {
    "si fiebre >= 38 y tos, entonces enfermedad = gripe": True,
    "si fiebre >= 39 y dolor de cabeza, entonces enfermedad = influenza": True,
    "si fiebre >= 38 y dificultad para respirar, entonces enfermedad = neumonía": True,
    "si fiebre >= 39 y dolor de garganta, entonces enfermedad = amigdalitis": True,
    "si fiebre >= 38 y sarpullido, entonces enfermedad = varicela": True,
    "si fiebre >= 38 y vómitos, entonces enfermedad = gastroenteritis": True,
}

# Definir la base de hechos
base_hechos = {
    "fiebre": 38,
    "tos": True,
    "dolor de cabeza": False,
    "dolor de garganta": True,
    "sarpullido": False,
    "vómitos": True,
}

# Implementar el motor de inferencia
def inferir_diagnostico(hechos):
    for regla, conclusion in base_conocimientos.items():
        coincidencias = [hecho for hecho in hechos if hecho in regla.split("y")]
        if all(coincidencias):
            return conclusion
    return None

# Crear la interfaz gráfica de usuario
ventana = tk.Tk()


# Agregar un título a la ventana
ventana.title("Sistema experto médico")

# Agregar un cuadro de entrada para los hechos
cuadro_entrada = ttk.Entry(ventana)
cuadro_entrada.pack()

# Agregar un botón de guardar en la base de hechos
boton_guardar = ttk.Button(ventana, text="Guardar en la base de hechos")
boton_guardar.pack()

# Agregar un botón de consultar el diagnóstico
boton_consultar = ttk.Button(ventana, text="Consultar diagnóstico")
boton_consultar.pack()

# Agregar un cuadro de texto para mostrar el diagnóstico
cuadro_diagnostico = ttk.Label(ventana)
cuadro_diagnostico.pack()

# Agregar el evento al botón de guardar en la base de hechos
boton_guardar.config(command=lambda: guardar_hechos(cuadro_entrada.get()))

# Agregar el evento al botón de consultar el diagnóstico
boton_consultar.config(command=lambda: consultar_diagnostico())

# Función para guardar los hechos en la base de conocimientos
def guardar_hechos(hechos):
    base_conocimientos.update({hechos: True})
    print(f"Los hechos {hechos} se han guardado en la base de conocimientos.")

# Función para consultar el diagnóstico
def consultar_diagnostico():
    hechos = cuadro_entrada.get()
    diagnostico = inferir_diagnostico(hechos)
    if diagnostico is None:
        diagnostico = "No se puede determinar el diagnóstico"
    cuadro_diagnostico.config(text=f"El diagnóstico es: {diagnostico}")

# Iniciar la interfaz gráfica de usuario
ventana.mainloop()