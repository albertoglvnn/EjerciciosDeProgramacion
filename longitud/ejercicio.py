def analizar_espectro(lambda_nm):
    # Constantes Físicas
    C = 299792458          # m/s
    H = 6.62607015e-34     # J*s
    EV_CONV = 1.602176634e-19 

    # Conversión a metros
    lambda_m = lambda_nm * 1e-9

    # Cálculos
    frecuencia = C / lambda_m
    energia_j = H * frecuencia
    energia_ev = energia_j / EV_CONV

    # Localización y Color
    color = "N/A"
    if lambda_nm < 10:
        localizacion = "Rayos Gamma / X"
    elif 10 <= lambda_nm < 380:
        localizacion = "Ultravioleta"
    elif 380 <= lambda_nm <= 750:
        localizacion = "Espectro Visible"
        if 380 <= lambda_nm < 450: color = "Violeta"
        elif 450 <= lambda_nm < 485: color = "Azul"
        elif 485 <= lambda_nm < 500: color = "Cian"
        elif 500 <= lambda_nm < 565: color = "Verde"
        elif 565 <= lambda_nm < 590: color = "Amarillo"
        elif 590 <= lambda_nm < 625: color = "Naranja"
        else: color = "Rojo"
    elif 750 < lambda_nm <= 1e6:
        localizacion = "Infrarrojo"
    else:
        localizacion = "Microondas / Radio"

    return frecuencia, energia_j, energia_ev, localizacion, color

# --- Bucle de consulta continua ---
print("Calculadora de Espectro Lista.")
print("Introduce el valor en nm y presiona Enter para el siguiente.")

while True:
    try:
        # El programa se detiene aquí hasta que tú escribas algo
        valor_nm = float(input("\nNueva lambda (nm): "))
        
        f, j, ev, loc, col = analizar_espectro(valor_nm)

        print(f"{' RESULTADOS ':=^40}")
        print(f"Frecuencia:    {f:.4e} Hz")
        print(f"Energía (J):   {j:.4e} J")
        print(f"Energía (eV):  {ev:.4f} eV")
        print(f"Ubicación:     {loc}")
        if col != "N/A":
            print(f"Color:         {col}")
        print("="*40)
        
    except ValueError:
        print(">> Por favor, ingresa solo números.")
        if 
    except KeyboardInterrupt:
        # Esto es por si quieres cerrar el programa con Ctrl+C
        print("\nPrograma finalizado.")
        break