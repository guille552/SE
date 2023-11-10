import tkinter as tk
from tkinter import ttk

base_de_hechos = {}

cuadro_fiebre = None
cuadro_tos = None
cuadro_dolor_cabeza = None
cuadro_dificultad_respirar = None
cuadro_diarrea = None
cuadro_vomito = None
combo_factores_riesgo = None
combo_factores_riesgo2 = None
combo_adicciones = None
combo_edad = None
cuadro_diagnostico = None

factores_riesgo = {
    "Ninguno": "",
    "Obesidad": "Aumento de peso, Dificultad para moverse",
    "Anorexia": "Pérdida de peso, Debilidad"
}

adicciones = ["Ninguno", "Alcoholismo", "Tabaquismo", "Drogadicción"]

def guardar_factores_riesgo():
    base_de_hechos["fiebre"] = cuadro_fiebre.instate(['selected'])
    base_de_hechos["tos"] = cuadro_tos.instate(['selected'])
    base_de_hechos["dolor_cabeza"] = cuadro_dolor_cabeza.instate(['selected'])
    base_de_hechos["dificultad_respirar"] = cuadro_dificultad_respirar.instate(['selected'])
    base_de_hechos["diarrea"] = cuadro_diarrea.instate(['selected'])
    base_de_hechos["vomito"] = cuadro_vomito.instate(['selected'])
    base_de_hechos["factores_riesgo"] = combo_factores_riesgo.get()
    if "Anorexia" in combo_factores_riesgo.get():
        combo_factores_riesgo2.set("Ninguno")
    if "Obesidad" in combo_factores_riesgo.get():
        combo_factores_riesgo2.set("Ninguno")
    if combo_adicciones.winfo_ismapped():
        base_de_hechos["adicciones"] = combo_adicciones.get()
    base_de_hechos["edad"] = int(combo_edad.get())
    print(f"Hechos guardados en la base de hechos: {base_de_hechos}")

def mostrar_interfaz_usuario():
    
    etiqueta_sintomas = ttk.Label(ventana, text="Síntomas:")
    etiqueta_sintomas.pack()

    etiqueta_sintomas = ttk.Label(ventana, text="")
    etiqueta_sintomas.pack()

    global cuadro_fiebre, cuadro_tos, cuadro_dolor_cabeza, cuadro_dificultad_respirar, cuadro_diarrea, cuadro_vomito
    cuadro_fiebre = ttk.Checkbutton(ventana, text="Fiebre")
    cuadro_fiebre.pack()

    cuadro_tos = ttk.Checkbutton(ventana, text="Tos")
    cuadro_tos.pack()

    cuadro_dolor_cabeza = ttk.Checkbutton(ventana, text="Dolor de cabeza")
    cuadro_dolor_cabeza.pack()

    cuadro_dificultad_respirar = ttk.Checkbutton(ventana, text="Dificultad para respirar")
    cuadro_dificultad_respirar.pack()

    cuadro_diarrea = ttk.Checkbutton(ventana, text="Diarrea")
    cuadro_diarrea.pack()

    cuadro_vomito = ttk.Checkbutton(ventana, text="Vómito")
    cuadro_vomito.pack()

    etiqueta_edad = ttk.Label(ventana, text="Edad:")
    etiqueta_edad.pack()

    global combo_edad
    combo_edad = ttk.Combobox(ventana, values=[f"{i}-{i+9} años" for i in range(10, 60, 10)], state="readonly")
    combo_edad.pack()

    etiqueta_factores_riesgo = ttk.Label(ventana, text="Factores de Riesgo:")
    etiqueta_factores_riesgo.pack()

    global combo_factores_riesgo, combo_factores_riesgo2
    combo_factores_riesgo = ttk.Combobox(ventana, values=list(factores_riesgo.keys()), state="readonly")
    combo_factores_riesgo.pack()

    etiqueta_adicciones = ttk.Label(ventana, text="Adicciones:")
    etiqueta_adicciones.pack()

    global combo_adicciones
    combo_adicciones = ttk.Combobox(ventana, values=adicciones, state="readonly")
    combo_adicciones.pack()

    boton_guardar_nueva_enfermedad = ttk.Button(ventana, text="Agregar Nueva Enfermedad", command=abrir_ventana_agregar_enfermedad)
    boton_guardar_nueva_enfermedad.pack()

    boton_guardar_factores_riesgo = ttk.Button(ventana, text="Guardar sintomas", command=guardar_factores_riesgo)
    boton_guardar_factores_riesgo.pack()

    boton_consultar = ttk.Button(ventana, text="Consultar diagnóstico", command=inferir_diagnostico)
    boton_consultar.pack()

    cuadro_diagnostico = ttk.Label(ventana, text="Bienvenido al sistema experto médico")
    cuadro_diagnostico.pack()

def abrir_ventana_agregar_enfermedad():
    ventana_agregar_enfermedad = tk.Toplevel(ventana)
    ventana_agregar_enfermedad.title("Agregar Nueva Enfermedad")
    ventana_agregar_enfermedad.config(width=400, height=300)

    etiqueta_enfermedad = ttk.Label(ventana_agregar_enfermedad, text="Nombre de la Enfermedad:")
    etiqueta_enfermedad.pack()

    cuadro_enfermedad = ttk.Entry(ventana_agregar_enfermedad)
    cuadro_enfermedad.pack()

    etiqueta_sintomas = ttk.Label(ventana_agregar_enfermedad, text="Síntomas Relacionados:")
    etiqueta_sintomas.pack()

    global cuadro_fiebre, cuadro_tos, cuadro_dolor_cabeza, cuadro_dificultad_respirar, cuadro_diarrea, cuadro_vomito
    cuadro_fiebre = ttk.Checkbutton(ventana_agregar_enfermedad, text="Fiebre")
    cuadro_fiebre.pack()

    cuadro_tos = ttk.Checkbutton(ventana_agregar_enfermedad, text="Tos")
    cuadro_tos.pack()

    cuadro_dolor_cabeza = ttk.Checkbutton(ventana_agregar_enfermedad, text="Dolor de cabeza")
    cuadro_dolor_cabeza.pack()

    cuadro_dificultad_respirar = ttk.Checkbutton(ventana_agregar_enfermedad, text="Dificultad para respirar")
    cuadro_dificultad_respirar.pack()

    cuadro_diarrea = ttk.Checkbutton(ventana_agregar_enfermedad, text="Diarrea")
    cuadro_diarrea.pack()

    cuadro_vomito = ttk.Checkbutton(ventana_agregar_enfermedad, text="Vómito")
    cuadro_vomito.pack()

    boton_guardar_enfermedad = ttk.Button(ventana_agregar_enfermedad, text="Guardar Enfermedad", command=guardar_nueva_enfermedad)
    boton_guardar_enfermedad.pack()

def guardar_nueva_enfermedad():
    # Aquí puedes guardar la nueva enfermedad y los síntomas relacionados en tu base de conocimientos.
    pass

def reglas_inferencia(hechos):
    # Agrega aquí tus reglas de inferencia
    pass

def inferir_diagnostico():
    guardar_factores_riesgo()  # Guarda la base de hechos antes de inferir el diagnóstico
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

ventana = tk.Tk()
ventana.title("Sistema experto médico para la detección de enfermedades")
ventana.config(width=600, height=600)

mostrar_interfaz_usuario()

ventana.mainloop()
