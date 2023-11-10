import tkinter as tk
from tkinter import ttk

# Definir lista de opciones para el ComboBox de tiempo desde que se presentaron los síntomas
opciones_tiempo_sintomas = ["1 día", "1 semana", "1 mes"]

# Base de Hechos (Fact Base)
base_de_hechos = {}

# Lista de Factores de Riesgo con Síntomas
factores_riesgo = {
    "Ninguno": "",
    "Desórdenes Alimenticios": "Pérdida o aumento de peso, Cambios en los hábitos alimenticios",
    "Adicciones": "Consumo de sustancias adictivas",
}

# Función para guardar factores de riesgo y otros datos en la base de hechos
def guardar_factores_riesgo():
    # Se guarda cada síntoma y su valor en la base de hechos
    base_de_hechos["fiebre"] = cuadro_fiebre_var.get()
    base_de_hechos["tos"] = cuadro_tos_var.get()
    base_de_hechos["dolor_cabeza"] = cuadro_dolor_cabeza_var.get()
    base_de_hechos["dificultad_respirar"] = cuadro_dificultad_respirar_var.get()
    base_de_hechos["diarrea"] = cuadro_diarrea_var.get()
    base_de_hechos["vomito"] = cuadro_vomito_var.get()
    
    # Se obtienen los factores de riesgo seleccionados
    factores_seleccionados = combo_factores_riesgo.get()
    base_de_hechos["factores_riesgo"] = factores_seleccionados
    
    # Se guarda la edad
    base_de_hechos["edad"] = int(combo_edad.get().split('-')[0])

    # Se imprime la base de hechos actualizada
    print(f"Hechos guardados en la base de hechos: {base_de_hechos}")

# Base de Conocimientos
def reglas_inferencia(hechos):
    if "Desórdenes Alimenticios" in hechos["factores_riesgo"] and hechos.get("dolor_cabeza") and hechos.get("vomito"):
        return "Posible diagnóstico: Gastroenteritis"
    elif "Adicciones" in hechos["factores_riesgo"] and hechos.get("adicciones"):
        return "Posible diagnóstico: Problemas relacionados con adicciones"
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
        "edad": base_de_hechos.get("edad", 0),
    }

    diagnostico = reglas_inferencia(hechos)
    cuadro_diagnostico.config(text=f"El diagnóstico es: {diagnostico}")

# Interfaz de Usuario
ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")

# Centrar la ventana en la pantalla
ancho_ventana = 550
alto_ventana = 250
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x_ventana = (ancho_pantalla / 2) - (ancho_ventana / 2)
y_ventana = (alto_pantalla / 2) - (alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int(x_ventana)}+{int(y_ventana)}")

# Marco para Edad y Factor de Riesgo
marco_edad_riesgo = ttk.Frame(ventana, padding=(10, 5))
marco_edad_riesgo.grid(row=0, column=0, columnspan=6, pady=(10, 0), sticky="w")

etiqueta_edad = ttk.Label(marco_edad_riesgo, text="Edad:")
etiqueta_edad.grid(row=0, column=0, pady=(0, 10), sticky="w")

rango_edad = ["{}-{} años".format(i, i + 9) for i in range(10, 70, 10)]
combo_edad = ttk.Combobox(marco_edad_riesgo, values=rango_edad, state="readonly")
combo_edad.grid(row=0, column=1, pady=(0, 10), sticky="w")

etiqueta_factores_riesgo = ttk.Label(marco_edad_riesgo, text="Factores de Riesgo:")
etiqueta_factores_riesgo.grid(row=1, column=0, pady=(0, 10), padx=(10, 0), sticky="w")

combo_factores_riesgo = ttk.Combobox(marco_edad_riesgo, values=list(factores_riesgo.keys()), state="readonly")
combo_factores_riesgo.grid(row=1, column=1, pady=(0, 10), sticky="w")

# Marco para Síntomas
marco_sintomas = ttk.Frame(ventana, padding=(10, 5))
marco_sintomas.grid(row=1, column=0, columnspan=6, pady=(10, 0), sticky="w")

etiqueta_sintomas = ttk.Label(marco_sintomas, text="Síntomas:")
etiqueta_sintomas.grid(row=0, column=0, columnspan=6, pady=(0, 10), sticky="w")

cuadro_fiebre_var = tk.BooleanVar()
cuadro_fiebre = ttk.Checkbutton(marco_sintomas, text="Fiebre", variable=cuadro_fiebre_var)
cuadro_fiebre.grid(row=1, column=0, padx=5, sticky="w")

cuadro_tos_var = tk.BooleanVar()
cuadro_tos = ttk.Checkbutton(marco_sintomas, text="Tos", variable=cuadro_tos_var)
cuadro_tos.grid(row=1, column=1, padx=5, sticky="w")

cuadro_dolor_cabeza_var = tk.BooleanVar()
cuadro_dolor_cabeza = ttk.Checkbutton(marco_sintomas, text="Dolor de cabeza", variable=cuadro_dolor_cabeza_var)
cuadro_dolor_cabeza.grid(row=1, column=2, padx=5, sticky="w")

cuadro_dificultad_respirar_var = tk.BooleanVar()
cuadro_dificultad_respirar = ttk.Checkbutton(marco_sintomas, text="Dificultad para respirar", variable=cuadro_dificultad_respirar_var)
cuadro_dificultad_respirar.grid(row=1, column=3, padx=5, sticky="w")

cuadro_diarrea_var = tk.BooleanVar()
cuadro_diarrea = ttk.Checkbutton(marco_sintomas, text="Diarrea", variable=cuadro_diarrea_var)
cuadro_diarrea.grid(row=1, column=4, padx=5, sticky="w")

cuadro_vomito_var = tk.BooleanVar()
cuadro_vomito = ttk.Checkbutton(marco_sintomas, text="Vómito", variable=cuadro_vomito_var)
cuadro_vomito.grid(row=1, column=5, padx=5, sticky="w")

# Marco para Tiempo de los Síntomas
marco_tiempo_sintomas = ttk.Frame(ventana, padding=(10, 5))
marco_tiempo_sintomas.grid(row=2, column=0, columnspan=6, pady=(10, 0), sticky="w")

etiqueta_tiempo_sintomas = ttk.Label(marco_tiempo_sintomas, text="Tiempo desde que se presentaron los síntomas:")
etiqueta_tiempo_sintomas.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

combo_tiempo_sintomas = ttk.Combobox(marco_tiempo_sintomas, values=opciones_tiempo_sintomas, state="readonly")
combo_tiempo_sintomas.grid(row=0, column=2, columnspan=2, pady=(0, 10), sticky="w")

# Marco para Botones
marco_botones = ttk.Frame(ventana, padding=(10, 5))
marco_botones.grid(row=3, column=0, columnspan=6, pady=(10, 0), sticky="w")

boton_guardar_factores_riesgo = ttk.Button(marco_botones, text="Guardar síntomas", command=guardar_factores_riesgo)
boton_guardar_factores_riesgo.grid(row=0, column=0, pady=(0, 10), sticky="w")

boton_consultar = ttk.Button(marco_botones, text="Consultar diagnóstico", command=inferir_diagnostico)
boton_consultar.grid(row=0, column=1, pady=(0, 10), padx=(10, 0), sticky="w")

cuadro_diagnostico = ttk.Label(marco_botones, text="Bienvenido al sistema experto médico")
cuadro_diagnostico.grid(row=0, column=2, columnspan=2, pady=(0, 10), padx=(10, 0), sticky="w")

ventana.mainloop()