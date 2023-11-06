import experta

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

class SistemaExperto(experta.KnowledgeEngine):

    @experta.Rule(Enfermedad(sintomas='si') & Edad('adulto') & Adicciones('si'))
    def regla_1(self):
        self.declare(Diagnostico(enfermedad="Intoxicación Alimentaria"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad('adulto') & Adicciones('no'))
    def regla_2(self):
        self.declare(Diagnostico(enfermedad="Gripe"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad('niño') & Adicciones('si'))
    def regla_3(self):
        self.declare(Diagnostico(enfermedad="Resfriado Común"))

    @experta.Rule(Enfermedad(sintomas='si') & Edad('niño') & Adicciones('no'))
    def regla_4(self):
        self.declare(Diagnostico(enfermedad="Gripe"))

    @experta.Rule(Enfermedad(sintomas='no'))
    def regla_5(self):
        self.declare(Diagnostico(enfermedad="Sin enfermedad identificada"))

def ejecutar_sistema_experto():
    engine = SistemaExperto()

    # Preguntar por síntomas
    respuesta_sintomas = input("¿Experimenta síntomas? (si/no): ")
    engine.declare(Enfermedad(sintomas=respuesta_sintomas))

    # Preguntar por edad
    respuesta_edad = input("¿Es usted un niño o un adulto? (niño/adulto): ")
    engine.declare(Edad(respuesta_edad))

    # Preguntar por adicciones
    respuesta_adicciones = input("¿Tiene adicciones? (si/no): ")
    engine.declare(Adicciones(respuesta_adicciones))

    # Ejecutar el sistema experto
    engine.run()

    # Obtener el diagnóstico
    diagnostico = engine.facts[Diagnostico][-1]

    print(f"El diagnóstico es: {diagnostico['enfermedad']}")

if __name__ == "__main__":
    ejecutar_sistema_experto()
