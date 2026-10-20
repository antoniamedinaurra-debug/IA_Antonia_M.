
Sistema de Recomendación Inicial - IA Antonia M.
Primeros pasos en la plataforma.
def recomendar_elemento(preferencia_usuario, opciones_disponibles):

    Función básica que busca coincidencias entre las preferencias 
    del usuario y las opciones disponibles.

    recomendaciones = [opcion for opcion in opciones_disponibles if preferencia_usuario.lower() in opcion.lower()]
    return recomendaciones

if __name__ == "__main__":
    print("¡Bienvenida a tu entorno de desarrollo en GitHub Codespaces!")
    
    # Ejemplo de uso
    preferencia = "hotel"
    catalogo = ["Sistema de seguridad en hotel", "Gestión de blancos de housekeeping", "Enoturismo y experiencia", "Cocina tradicional"]
    
    resultados = recomendar_elemento(preferencia, catalogo)
    print(f"Resultados recomendados para '{preferencia}': {resultados}")
    
Pasos que hice para llegar aquí:
Primero, me cree una cuenta en github.com copilot.
Segundo, cree mi repositorio en github y comence a rellenar datos.
Tercero fui a google y busque visual studio code para clonar el codigo que me dio mi repositorio pero no pude hacerlo por politica de la pagina web entonces lo hice desde la misma pagina pero como git codespaces.
Cuarto, en la parte de codigo me fui a espacios de codigo y aprete crear espacio de codigo.
Quinto, comenze a poner el codiogo del documento inacap con mis datos de cuenta y nombre de repositorio.
Sexto, me cree una carpera donde poder hacer mi codigo inicial.
Septimo, dejo evidencia de mi esfuerso y desempeño.