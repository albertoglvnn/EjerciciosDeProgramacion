# PROGRAMA: Espectro Electromagnético
# Autor: (Tu nombre)
# Descripción: Calcula frecuencia, energía en J, eV y región del espectro
# a partir de la longitud de onda en nm


#Diego Cuevas, Gustavo Camela, Romero Mendoza, Gary Palafox, Jesus Solis, Angel Burgoin, Kevin Calleros

# Constantes físicas
c = 3.0e8              # Velocidad de la luz (m/s)
h = 6.626e-34          # Constante de Planck (J*s)
eV_conversion = 1.602e-19  # 1 eV en Joules

while True:
    print("\n====== ESPECTRO ELECTROMAGNÉTICO ======")
    
    # Validación de entrada
    while True:
        entrada = input("Ingresa la longitud de onda en nm (o escribe 'salir'): ")
        
        if entrada.lower() == "salir":
            print("\nPrograma finalizado correctamente.")
            exit()
        
        try:
            lambda_nm = float(entrada)
            
            if lambda_nm <= 0:
                print("Error: No existen longitudes de onda negativas ni iguales a cero.")
            else:
                break
                
        except ValueError:
            print("Error: Solo se permiten valores numéricos positivos.")

    # Conversión a metros
    lambda_m = lambda_nm * 1e-9

    # Cálculos físicos
    frecuencia = c / lambda_m
    energia_J = h * frecuencia
    energia_eV = energia_J / eV_conversion

    # Determinar región del espectro
    if lambda_nm < 0.01:
        region = "Rayos Gamma"
    elif lambda_nm < 10:
        region = "Rayos X"
    elif lambda_nm < 400:
        region = "Ultravioleta"
    elif lambda_nm <= 700:
        region = "Luz Visible"
    elif lambda_nm <= 1e6:
        region = "Infrarrojo"
    elif lambda_nm <= 1e9:
        region = "Microondas"
    else:
        region = "Ondas de Radio"

    # Determinar color si es visible
    color = ""
    if 380 <= lambda_nm < 450:
        color = "Violeta"
    elif 450 <= lambda_nm < 495:
        color = "Azul"
    elif 495 <= lambda_nm < 570:
        color = "Verde"
    elif 570 <= lambda_nm < 590:
        color = "Amarillo"
    elif 590 <= lambda_nm < 620:
        color = "Naranja"
    elif 620 <= lambda_nm <= 750:
        color = "Rojo"

    # Mostrar resultados
    print("\n----- RESULTADOS -----")
    print(f"Frecuencia: {frecuencia:.2e} Hz")
    print(f"Energía: {energia_J:.2e} J")
    print(f"Energía: {energia_eV:.2f} eV")
    print("Región:", region)

    if color:
        print("Color visible:", color)
        

