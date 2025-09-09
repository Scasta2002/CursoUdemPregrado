def calcular_capm(rf, beta, rm):
    """
    Calcula el rendimiento esperado usando el modelo CAPM.

    Parámetros:
    rf (float): Tasa libre de riesgo.
    beta (float): Beta del activo.
    rm (float): Rendimiento esperado del mercado.

    Retorna:
    float: Rendimiento esperado del activo.
    """
    return rf + beta * (rm - rf)