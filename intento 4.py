#librerias 
import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

# Definir lista de opciones para el ComboBox de tiempo desde que se presentaron los síntomas
opciones_tiempo_sintomas = ["1 día", "1 semana", "1 mes"]

#----------------------------------------------------------------------------------#
# Base de Hechos (Fact Base)
base_de_hechos = {}

#-----------------------------------------------------------------------------------#
# Lista de Factores de Riesgo con Síntomas
factores_riesgo = {
    "Ninguno": "",
    "Desórdenes Alimenticios": "Pérdida o aumento de peso, Cambios en los hábitos alimenticios",
    "Adicciones": "Consumo de sustancias adictivas",
}

#------------------------------------------------------------------------------------#
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

#---------------------------------------------------------------------------------------------------#
# Función para abrir la ventana de adquisición de conocimiento
def adquisicion_conocimiento():
    ventana_adquisicion = tk.Toplevel(ventana)
    ventana_adquisicion.title("Adquisición de Conocimiento")

    # Agregar una etiqueta para el texto
    etiqueta_texto = tk.Label(ventana_adquisicion, text="Por favor, ingrese los síntomas y factores de riesgo para agregar una nueva regla de inferencia:")
    etiqueta_texto.pack(pady=10)

    # Agregar un cuadro de texto para ingresar los síntomas
    cuadro_sintomas = tk.Entry(ventana_adquisicion)
    cuadro_sintomas.pack(pady=10)

    # Agregar un cuadro de texto para ingresar los factores de riesgo
    cuadro_factores_riesgo = tk.Entry(ventana_adquisicion)
    cuadro_factores_riesgo.pack(pady=10)

    # Agregar un botón para guardar la nueva regla de inferencia
    def guardar_regla():
        sintomas = cuadro_sintomas.get()
        factores_riesgo = cuadro_factores_riesgo.get()
        nueva_regla = f"if '{factores_riesgo}' in hechos['factores_riesgo'] and {sintomas}:\n    return 'Nuevo Diagnóstico'"
        print(f"Se ha agregado la siguiente regla de inferencia:\n{nueva_regla}")
        ventana_adquisicion.destroy()

    boton_guardar = tk.Button(ventana_adquisicion, text="Guardar", command=guardar_regla)
    boton_guardar.pack(pady=10)

    # Agregar un botón para cancelar la adquisición de conocimiento
    boton_cancelar = tk.Button(ventana_adquisicion, text="Cancelar", command=ventana_adquisicion.destroy)
    boton_cancelar.pack(pady=10)

#---------------------------------------------------------------------------------#
# Función para mostrar el diagnóstico en una ventana emergente
def mostrarDiagnostico(diagnostico, descripcion, rutaimagen):
    ventana_diagnostico = tk.Toplevel(ventana)
    ventana_diagnostico.title("Diagnóstico")

    # Agregar una etiqueta para el texto
    etiqueta_texto = tk.Label(ventana_diagnostico, text=diagnostico)
    etiqueta_texto.pack(pady=10)
    
    # Agregar una etiqueta para el texto
    etiqueta_descripcion = tk.Label(ventana_diagnostico, text=descripcion)
    etiqueta_descripcion.pack(pady=10)
  
    # Cargar una imagen
    imagen = PhotoImage(file=rutaimagen)  # Reemplaza con la ruta de tu propia imagen
    etiqueta_imagen = tk.Label(ventana_diagnostico, image=imagen)
    etiqueta_imagen.image = imagen
    etiqueta_imagen.pack(pady=10)
    
    # Boton de cerrar
    boton_cerrar = tk.Button(ventana_diagnostico, text="Cerrar", command=ventana_diagnostico.destroy)
    boton_cerrar.pack(pady=10)
    
    # En caso que no exista un diagnóstico, abrir el modulo de adquisición de conocimiento
   
    if diagnostico == "No se puede determinar el diagnóstico":
        messagebox.showinfo("No encontrado", "No se encontró un diagnóstico, se abrirá el módulo de adquisición de conocimiento")
        boton_adquisicion = tk.Button(ventana_diagnostico, text="Adquisición de conocimiento", command=adquisicion_conocimiento)
        boton_adquisicion.pack(pady=10)

#-----------------------------------------------------------------------#
# Base de Conocimientos
def reglas_inferencia(hechos):
    if "Desórdenes Alimenticios" in hechos["factores_riesgo"] and hechos.get("dolor_cabeza") and hechos.get("vomito"):
        return "Gastroenteritis"
    elif "Adicciones" in hechos["factores_riesgo"] and hechos.get("adicciones"):
        return "Problemas relacionados con adicciones"
    elif hechos.get("fiebre") and hechos.get("tos"):
        return "Gripe"
    elif hechos.get("fiebre") and hechos.get("dolor_cabeza"):
        return "influenza"
    elif hechos.get("fiebre") and hechos.get("dificultad_respirar"):
        return "Neumonía"
    elif hechos.get("diarrea") and hechos.get("vomito"):
        return "Gastroenteritis"
    elif hechos.get("fiebre") and hechos.get("congestion_nasal"):
        return "Resfriado Común"
    elif hechos.get("fiebre") and hechos.get("dolor_cabeza"):
        return "Dengue"
    elif hechos.get("dificultad_para_respirar") and hechos.get("tos"):
        return "Ataque de Asma"
    elif hechos.get("fiebre") and hechos.get("diarrea"):
        return "Infección Intestinal"
    else:
        return "No se puede determinar el diagnóstico"
    
#-----------------------------------------------------------------------------------#
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
    #cuadro_diagnostico.config(text=f"El diagnóstico es: #{diagnostico}")

    #mandar el diagnostico a una ventana emergente 
    mostrarDiagnostico(diagnostico, "Agregar una descripcion", "Imagenes/{}.png".format(diagnostico))   

#-----------------------------------------------------------------------#
# Interfaz de Usuario
ventana = tk.Tk()
ventana.title("Sistema Experto médico para la detección de enfermedades")

# Centrar la ventana en la pantalla
ancho_ventana = 550
alto_ventana = 250
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x_ventana = (ancho_pantalla / 2) - (ancho_ventana / 2)
y_ventana = (alto_pantalla / 2) - (alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int(x_ventana)}+{int(y_ventana)}")

#---------------------------------------------------------------------------------------#
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

#-------------------------------------------------------------------------------------------------------
# Marco para Botones
marco_botones = ttk.Frame(ventana, padding=(10, 5))
marco_botones.grid(row=3, column=0, columnspan=6, pady=(10, 0), sticky="w")

boton_guardar_factores_riesgo = ttk.Button(marco_botones, text="Guardar síntomas", command=guardar_factores_riesgo)
boton_guardar_factores_riesgo.grid(row=0, column=0, pady=(0, 10), sticky="w")

boton_consultar = ttk.Button(marco_botones, text="Consultar diagnóstico", command=inferir_diagnostico)
boton_consultar.grid(row=0, column=1, pady=(0, 10), padx=(10, 0), sticky="w")

cuadro_diagnostico = ttk.Label(marco_botones, text="Bienvenido al sistema experto médico")
cuadro_diagnostico.grid(row=0, column=2, columnspan=2, pady=(0, 10), padx=(10, 0), sticky="w")

ventana.mainloop() #iniciar los eventos 