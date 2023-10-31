import tkinter as tk
from tkinter import ttk
import experta
from experta import Rule, KnowledgeBase, InferenceEngine, abc

# Definir la base de conocimientos
base_conocimientos = KnowledgeBase()

# Definir las reglas
class GripeRule(Rule):
    def match(self, facts):
        fiebre = facts["fiebre"] >= 38
        tos = facts["tos"]
        return fiebre and tos

class InfluenzaRule(Rule):
    def match(self, facts):
        fiebre = facts["fiebre"] >= 39
        dolor_cabeza = facts["dolor_cabeza"]
        return fiebre and dolor_cabeza

class NeumoniaRule(Rule):
    def match(self, facts):
        fiebre = facts["fiebre"] >= 38
        dificultad_respirar = facts["dificultad_respirar"]
        return fiebre and dificultad_respirar

class GastroenteritisRule(Rule):
    def match(self, facts):
        diarrea = facts["diarrea"]
        vomito = facts[" vomito"]
        return diarrea and vomito

# Agregar las reglas a la base de conocimientos
base_conocimientos.add_rule(GripeRule())
base_conocimientos.add_rule(InfluenzaRule())
base_conocimientos.add_rule(NeumoniaRule())
base_conocimientos.add_rule(GastroenteritisRule())

# Crear la interfaz gráfica de usuario
ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")
ventana.config(width=500, height=400)

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
cuadro_diagnostico = ttk.Label(ventana, text="Bienvenido al sistema experto médico")
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

# Función para inferir el diagnóstico
def inferir_diagnostico(hechos):
    for regla, conclusion in base_conocimientos.items():
        coincidencias = [hecho for hecho in hechos if hecho in regla.split("y")]
        if all(coincidencias):
            return conclusion
    return None

# Iniciar la interfaz gráfica de usuario
ventana.mainloop()
