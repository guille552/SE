import tkinter as tk
from tkinter import ttk
import experta

# Definición de hechos (facts)
class Enfermedad(experta.Fact):
    pass

class Sintoma(experta.Fact):
    pass

class Edad(experta.Fact):
    pass

class Adicciones(experta.Fact):
    pass

class Diagnostico(experta.Fact):
    pass

# Definición del sistema experto
class SistemaExperto(experta.KnowledgeEngine):

    @experta.Rule(Enfermedad(sintomas='si') & Edad(lambda x: x >= 18) & Adicciones('si'))
    def regla_1(self):
        self.declare(Diagnostico(enfermedad="Intoxicación Alimentaria"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad(lambda x: x >= 18) & Adicciones('no'))
    def regla_2(self):
        self.declare(Diagnostico(enfermedad="Gripe"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad(lambda x: x < 18) & Adicciones('si'))
    def regla_3(self):
        self.declare(Diagnostico(enfermedad="Resfriado Común"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad(lambda x: x < 18) & Adicciones('no'))
    def regla_4(self):
        self.declare(Diagnostico(enfermedad="Gripe"))

    @experta.Rule(Enfermedad(sintomas='no'))
    def regla_5(self):
        self.declare(Diagnostico(enfermedad="Sin enfermedad identificada"))

def ejecutar_sistema_experto():
    engine = SistemaExperto()

    respuesta_sintomas = cuadro_sintomas.get()
    engine.reset()  
    engine.declare(Enfermedad(sintomas=respuesta_sintomas))

    try:
        respuesta_edad = int(cuadro_edad.get())
    except ValueError:
        cuadro_diagnostico.config(text="Por favor, ingrese una edad válida.")
        return

    engine.declare(Edad(respuesta_edad))

    respuesta_adicciones = cuadro_adicciones.get()
    engine.declare(Adicciones(respuesta_adicciones))

    engine.run()

    diagnostico = engine.facts[Diagnostico][-1]

    cuadro_diagnostico.config(text=f"El diagnóstico es: {diagnostico['enfermedad']}")

ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")
ventana.config(width=500, height=400)

etiqueta_sintomas = ttk.Label(ventana, text="¿Experimenta síntomas? (si/no):")
etiqueta_sintomas.pack()

cuadro_sintomas = ttk.Entry(ventana)
cuadro_sintomas.pack()

etiqueta_edad = ttk.Label(ventana, text="Ingrese su edad:")
etiqueta_edad.pack()

cuadro_edad = ttk.Entry(ventana)
cuadro_edad.pack()

etiqueta_adicciones = ttk.Label(ventana, text="¿Tiene adicciones? (si/no):")
etiqueta_adicciones.pack()

cuadro_adicciones = ttk.Entry(ventana)
cuadro_adicciones.pack()

boton_consultar = ttk.Button(ventana, text="Consultar diagnóstico", command=ejecutar_sistema_experto)
boton_consultar.pack()

cuadro_diagnostico = ttk.Label(ventana, text="Bienvenido al sistema médico")
cuadro_diagnostico.pack()

ventana.mainloop()
