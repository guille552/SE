import tkinter as tk
from tkinter import ttk

# Base de Hechos (Fact Base)
base_de_hechos = {}

# Base de Conocimientos (Knowledge Base)
def reglas_inferencia(hechos):
    if hechos.get("fiebre") and hechos.get("tos"):
        return "Posible diagnóstico: Gripe"
    elif hechos.get("fiebre") and hechos.get("dolor_cabeza"):
        return "Posible diagnóstico: Influenza"
    elif hechos.get("fiebre") and hechos.get("dificultad_respirar"):
        return "Posible diagnóstico: Neumonía"
    elif hechos.get("diarrea") and hechos.get("vomito"):
        return "Posible diagnóstico: Gastroenteritis"
    else:
        return "No se puede determinar el diagnóstico"

# Motor de Inferencia (Inference Engine)
def inferir_diagnostico():
    diagnostico = reglas_inferencia(base_de_hechos)
    return diagnostico

def guardar_hechos(hechos):
    base_de_hechos.update(hechos)
    print(f"Hechos actualizados: {base_de_hechos}")

def consultar_diagnostico():
    diagnostico = inferir_diagnostico()
    if diagnostico is None:
        diagnostico = "No se puede determinar el diagnóstico"
    cuadro_diagnostico.config(text=f"El diagnóstico es: {diagnostico}")

ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")
ventana.config(width=500, height=400)

# Interfaz de Usuario
etiqueta_sintomas = ttk.Label(ventana, text="Síntomas:")
etiqueta_sintomas.pack()

cuadro_fiebre = ttk.Entry(ventana)
cuadro_fiebre.pack()
etiqueta_fiebre = ttk.Label(ventana, text="Fiebre (si/no):")
etiqueta_fiebre.pack()

cuadro_tos = ttk.Entry(ventana)
cuadro_tos.pack()
etiqueta_tos = ttk.Label(ventana, text="Tos (si/no):")
etiqueta_tos.pack()

cuadro_dolor_cabeza = ttk.Entry(ventana)
cuadro_dolor_cabeza.pack()
etiqueta_dolor_cabeza = ttk.Label(ventana, text="Dolor de cabeza (si/no):")
etiqueta_dolor_cabeza.pack()

cuadro_dificultad_respirar = ttk.Entry(ventana)
cuadro_dificultad_respirar.pack()
etiqueta_dificultad_respirar = ttk.Label(ventana, text="Dificultad para respirar (si/no):")
etiqueta_dificultad_respirar.pack()

cuadro_diarrea = ttk.Entry(ventana)
cuadro_diarrea.pack()
etiqueta_diarrea = ttk.Label(ventana, text="Diarrea (si/no):")
etiqueta_diarrea.pack()

cuadro_vomito = ttk.Entry(ventana)
cuadro_vomito.pack()
etiqueta_vomito = ttk.Label(ventana, text="Vómito (si/no):")
etiqueta_vomito.pack()

boton_guardar = ttk.Button(ventana, text="Guardar en la base de hechos", command=lambda: guardar_hechos({
    "fiebre": cuadro_fiebre.get().lower() == "si",
    "tos": cuadro_tos.get().lower() == "si",
    "dolor_cabeza": cuadro_dolor_cabeza.get().lower() == "si",
    "dificultad_respirar": cuadro_dificultad_respirar.get().lower() == "si",
    "diarrea": cuadro_diarrea.get().lower() == "si",
    "vomito": cuadro_vomito.get().lower() == "si",
}))
boton_guardar.pack()

boton_consultar = ttk.Button(ventana, text="Consultar diagnóstico", command=consultar_diagnostico)
boton_consultar.pack()

cuadro_diagnostico = ttk.Label(ventana, text="Bienvenido al sistema experto médico")
cuadro_diagnostico.pack()

ventana.mainloop()
