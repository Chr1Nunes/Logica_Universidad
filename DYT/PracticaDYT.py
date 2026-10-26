hechos = {
    # Para el aguila real
    ("animal1", "tiene_plumas", True),
    ("animal1", "tarsos_emplumados", True),

    # Para el rinoceronte
    ("animal2", "tiene_pelo", True),
    ("animal2", "muy_pesado", True),
    ("animal2", "cuerno_hocico", True),

    # Para el hipopotamo
    ("animal3", "da_leche", True),
    ("animal3", "enorme", True),
    ("animal3", "gris", True),
    ("animal3", "vive_sumergido", True),
    
    # Para el guepardo
    ("animal4", "tiene_pelo", True),
    ("animal4", "come_carne", True),
    ("animal4", "color_leonado", True),
    ("animal4", "manchas_oscuras", True),

    # Para el tigre
    ("animal5", "da_leche", True),
    ("animal5", "come_carne", True),
    ("animal5", "color_leonado", True),
    ("animal5", "rayas_negras", True),

    # Para la jirafa
    ("animal6", "tiene_pelo", True),
    ("animal6", "tiene_pezunas", True),
    ("animal6", "cuello_largo", True),
    ("animal6", "manchas_oscuras", True),

    # Para la cebra
    ("animal7", "da_leche", True),
    ("animal7", "tiene_pezunas", True),
    ("animal7", "rayas_negras", True),

    # Para el pinguino
    ("animal8", "tiene_plumas", True),
    ("animal8", "nada", True),
    ("animal8", "blanco_negro", True),

    # Para el albatros
    ("animal9", "vuela", True),
    ("animal9", "pone_huevos", True),
    ("animal9", "vuela_muy_bien", True)
}

def motor_inferencia(hechos):
    conocimiento = set(hechos)
    deducciones = set()

    for sujeto, attr, val in conocimiento:
        if attr in ["tiene_pelo", "da_leche"] and val is True:
            deducciones.add((sujeto, "es_mamifero", True))
        if attr in ["tiene_plumas"] and val is True:
            deducciones.add((sujeto, "es_ave", True))
        if (sujeto, "vuela", True) in conocimiento and (sujeto, "pone_huevos", True) in conocimiento:
            deducciones.add((sujeto, "es_ave", True))

    conocimiento.update(deducciones)

    for sujeto, attr, val in conocimiento:
        if (sujeto, "es_mamifero", True) in conocimiento:
            if (sujeto, "come_carne", True) in conocimiento:
                deducciones.add((sujeto, "es_carnivoro", True))
            if (sujeto, "tiene_pezunas", True) in conocimiento:
                deducciones.add((sujeto, "es_ungulado", True))
            if (sujeto, "muy_pesado", True) in conocimiento and (sujeto, "cuerno_hocico", True) in conocimiento:
                deducciones.add((sujeto, "especie", "rinoceronte"))
            if (sujeto, "enorme", True) in conocimiento and (sujeto, "gris", True) in conocimiento and (sujeto, "vive_sumergido", True) in conocimiento:
                deducciones.add((sujeto, "especie", "hipopotamo"))

        if (sujeto, "es_carnivoro", True) in conocimiento:
            if (sujeto, "color_leonado", True) in conocimiento and (sujeto, "manchas_oscuras", True) in conocimiento:
                deducciones.add((sujeto, "especie", "guepardo"))
            if (sujeto, "color_leonado", True) in conocimiento and (sujeto, "rayas_negras", True) in conocimiento:
                deducciones.add((sujeto, "especie", "tigre"))
                
        if (sujeto, "es_ungulado", True) in conocimiento:
            if (sujeto, "cuello_largo", True) in conocimiento and (sujeto, "manchas_oscuras", True) in conocimiento:
                deducciones.add((sujeto, "especie", "jirafa"))
            if (sujeto, "rayas_negras", True) in conocimiento:
                deducciones.add((sujeto, "especie", "cebra"))
                
        if (sujeto, "es_ave", True) in conocimiento:
            if (sujeto, "nada", True) in conocimiento and (sujeto, "blanco_negro", True) in conocimiento:
                deducciones.add((sujeto, "especie", "pinguino"))
            if (sujeto, "vuela_muy_bien", True) in conocimiento:
                deducciones.add((sujeto, "especie", "albatros"))
            if (sujeto, "tarsos_emplumados", True) in conocimiento:
                deducciones.add((sujeto, "especie", "aguila_real"))
            if (sujeto, "planea_estable", True) in conocimiento:
                deducciones.add((sujeto, "especie", "aguila_real"))

        if (sujeto, "piel_gruesa_placas", True) in conocimiento and (sujeto, "gris", True) in conocimiento and (sujeto, "come_plantas", True) in conocimiento:
            deducciones.add((sujeto, "especie", "rinoceronte"))

    conocimiento.update(deducciones)
    return conocimiento

if __name__ == "__main__":
    resultados = motor_inferencia(hechos)
    
    print("Clasificaciones finales encontradas:")
    for hecho in sorted(resultados):
        if hecho[1] == "especie":
            print(f"El {hecho[0]} es un(a) {hecho[2]}")