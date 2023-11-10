import tkinter as tk
from tkinter import ttk

# Base de Hechos (Fact Base)
base_de_hechos = {}

# Lista de Factores de Riesgo con Síntomas
factores_riesgo = {
    "Ninguno": "",
    "Obesidad": "Aumento de peso, Dificultad para moverse",
    "Anorexia": "Pérdida de peso, Debilidad"
}

# Lista de Adicciones
adicciones = ["Ninguno", "Alcoholismo", "Tabaquismo", "Drogadicción"]

# Función para guardar factores de riesgo y otros datos en la base de hechos
def guardar_factores_riesgo():
    # Se guarda cada síntoma y su valor en la base de hechos
    base_de_hechos["fiebre"] = cuadro_fiebre.get().lower() == "si"
    base_de_hechos["tos"] = cuadro_tos.get().lower() == "si"
    base_de_hechos["dolor_cabeza"] = cuadro_dolor_cabeza.get().lower() == "si"
    base_de_hechos["dificultad_respirar"] = cuadro_dificultad_respirar.get().lower() == "si"
    base_de_hechos["diarrea"] = cuadro_diarrea.get().lower() == "si"
    base_de_hechos["vomito"] = cuadro_vomito.get().lower() == "si"
    
    # Se obtienen los factores de riesgo seleccionados
    factores_seleccionados = combo_factores_riesgo.get()
    base_de_hechos["factores_riesgo"] = factores_seleccionados
    
    # Se deshabilita Anorexia y Obesidad en el otro combo box
    if "Anorexia" in factores_seleccionados:
        combo_factores_riesgo2.set("Ninguno")
    if "Obesidad" in factores_seleccionados:
        combo_factores_riesgo2.set("Ninguno")

    # Se obtienen las adicciones seleccionadas
    if combo_adicciones.winfo_ismapped():
        adicciones_seleccionadas = combo_adicciones.get()
        base_de_hechos["adicciones"] = adicciones_seleccionadas
    
    # Se guarda la edad
    base_de_hechos["edad"] = int(combo_edad.get())

    # Se imprime la base de hechos actualizada
    print(f"Hechos guardados en la base de hechos: {base_de_hechos}")

# Base de Conocimientos
def reglas_inferencia(hechos):
    if "Obesidad" in hechos["factores_riesgo"] and hechos.get("fiebre") and hechos.get("dificultad_respirar"):
        return "Posible diagnóstico: Neumonía"
    elif "Anorexia" in hechos["factores_riesgo"] and hechos.get("dolor_cabeza") and hechos.get("vomito"):
        return "Posible diagnóstico: Gastroenteritis"
    elif hechos["edad"] >= 60 and hechos.get("dificultad_respirar"):
        return "Posible diagnóstico: Neumonía en Adulto Mayor"
    elif hechos.get("fiebre") and hechos.get("tos"):
        return "Posible diagnóstico: Gripe"
    elif hechos.get("fiebre") and hechos.get("dolor_cabeza"):
        return "Posible diagnóstico: Influenza"
    elif hechos.get("fiebre") and hechos.get("dificultad_respirar"):
        return "Posible diagnóstico: Neumonía"
    elif hechos.get("diarrea") and hechos.get("vomito"):
        return "Posible diagnóstico: Gastroenteritis"
    elif hechos.get("fiebre") and hechos.get("congestion_nasal"):
        return "Posible diagnóstico: Resfriado Común"
    elif hechos.get("fiebre_alta") and hechos.get("dolor_muscular"):
        return "Posible diagnóstico: Dengue"
    elif hechos.get("dificultad_para_respirar") and hechos.get("sibilancias"):
        return "Posible diagnóstico: Ataque de Asma"
    elif hechos.get("fiebre") and hechos.get("dolor_abdominal"):
        return "Posible diagnóstico: Infección Intestinal"
    else:
        return "No se puede determinar el diagnóstico"

# Motor de Inferencia (Inference Engine)
def inferir_diagnostico():
    hechos = {
        "fiebre": base_de_hechos.get("fiebre", False),
        "tos": base_de_hechos.get("tos", False),
        "dolor_cabeza": base_de_hechos.get("dolor_cabeza", False),
        "dificultad_respirar": base_de_hechos.get("dificultad_respirar", False),
        "diarrea": base_de_hechos.get("diarrea", False),
        "vomito": base_de_hechos.get("vomito", False),
        "factores_riesgo": base_de_hechos.get("factores_riesgo", []),
        "adicciones": base_de_hechos.get("adicciones", []),
        "edad": base_de_hechos.get("edad", 0)
    }

    diagnostico = reglas_inferencia(hechos)
    cuadro_diagnostico.config(text=f"El diagnóstico es: {diagnostico}")

def consultar_diagnostico():
    inferir_diagnostico()

ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")
ventana.config(width=600, height=600)

# Interfaz de Usuario

etiqueta_sintomas = ttk.Label(ventana, text="Síntomas:")
etiqueta_sintomas.pack()

etiqueta_sintomas = ttk.Label(ventana, text="")
etiqueta_sintomas.pack()

etiqueta_edad = ttk.Label(ventana, text="Edad:")
etiqueta_edad.pack()

combo_edad = ttk.Combobox(ventana, values=list(range(10, 70)), state="readonly")
combo_edad.pack()

etiqueta_sintomas = ttk.Label(ventana, text="")
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

# Combo Box para Factores de Riesgo
etiqueta_factores_riesgo = ttk.Label(ventana, text="Factores de Riesgo:")
etiqueta_factores_riesgo.pack()

combo_factores_riesgo = ttk.Combobox(ventana, values=list(factores_riesgo.keys()), state="readonly")
combo_factores_riesgo.pack()

combo_factores_riesgo2 = ttk.Combobox(ventana, values=list(factores_riesgo.keys()), state="readonly")
combo_factores_riesgo2.pack()

# Combo Box para Adicciones
etiqueta_adicciones = ttk.Label(ventana, text="Adicciones:")
etiqueta_adicciones.pack()

# Combo box de adicciones
combo_adicciones = ttk.Combobox(ventana, values=adicciones, state="readonly")
combo_adicciones.pack()

# Botón para Guardar Factores de Riesgo
boton_guardar_factores_riesgo = ttk.Button(ventana, text="Guardar síntomas", command=guardar_factores_riesgo)
boton_guardar_factores_riesgo.pack()

# Botón para Consultar Diagnóstico
boton_consultar = ttk.Button(ventana, text="Consultar diagnóstico", command=consultar_diagnostico)
boton_consultar.pack()

cuadro_diagnostico = ttk.Label(ventana, text="Bienvenido al sistema experto médico")
cuadro_diagnostico.pack()

ventana.mainloop()
