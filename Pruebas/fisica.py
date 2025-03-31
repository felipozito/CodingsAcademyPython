import sympy as sp

formulas = {
    "MRU": {
        "instrucciones": "Movimiento Rectilíneo Uniforme: Útil para calcular velocidad constante, distancia o tiempo.",
        "formulas": ["v=d/t"]
    },
    "MRUV": {
        "instrucciones": "Movimiento Rectilíneo Uniformemente Variado: Para movimientos con aceleración constante.",
        "formulas": [
            "vf=vo+a*t",
            "d=vo*t+(1/2)*a*t^2",
            "vf^2=vo^2+2*a*d",
            "d=(vo+vf)/2*t"
        ]
    },
    "CAIDA LIBRE": {
        "instrucciones": "Caída Libre: Movimiento vertical bajo la acción de la gravedad (g=9.81 m/s²).",
        "formulas": [
            "vf=vo+9.81*t",
            "h=vo*t+1/2*9.81*t^2",
            "vf^2=vo^2+2*9.81*h"
        ]
    },
    "LANZAMIENTO VERTICAL": {
        "instrucciones": "Lanzamiento Vertical: Movimiento vertical hacia arriba contra la gravedad.",
        "formulas": [
            "vf=vo-9.81*t",
            "h=vo*t-1/2*9.81*t^2",
            "vf^2=vo^2-2*9.81*h"
        ]
    },
    "MCU": {
        "instrucciones": "Movimiento Circular Uniforme: Para objetos que se mueven en círculo a velocidad constante.",
        "formulas": [
            "v=l/t",
            "w=theta/t"
        ]
    },
    "MCUV": {
        "instrucciones": "Movimiento Circular Uniformemente Variado: Para movimientos circulares con aceleración constante.",
        "formulas": [
            "vf=vo+a*t",
            "l=vo*t+(1/2)*a*t^2",
            "vf^2=vo^2+2*a*l",
            "wf=wo+at*t",
            "theta=wo*t+(1/2)*at*t^2",
            "wf^2=wo^2+2*at*theta"
        ]
    },
    "LEY_DE_COULOMB": {
        "instrucciones": "Ley de Coulomb: Calcula la fuerza electrostática entre dos cargas puntuales.",
        "formulas": [
            "F=(9*10^9)*(q1*q2)/r^2"
        ]
    },
    "LEY_DE_COULOMB 2 CARGAS LINEA RECTA": {
        "instrucciones": "Ley de Coulomb para dos cargas en línea recta: Suma de fuerzas electrostáticas. RECORDAR  LA CARGA EN COMUN ES Q2",
        "formulas": [
            "Ft=((9*10^9)*(q1*q2)/r1^2) +((9*10^9)*(q2*q3)/r2^2)"
        ]},
    
    "ENERGIA": {
        "instrucciones": "Energía: Calcula diferentes tipos de energía (potencial, cinética, elástica).",
        "formulas": [
            "ep=m*9.81*h",
            "ec=1/2*m*v^2",
            "ek=1/2*k*x^2"
        ]
    },
    "TRABAJO": {
        "instrucciones": "Trabajo: Calcula el trabajo realizado por una fuerza constante.",
        "formulas": [
            "W=F*d"
        ]
    },
    "POTENCIA": {
        "instrucciones": "Potencia: Calcula la rapidez con que se realiza un trabajo.",
        "formulas": [
            "P=W/t"
        ]
    },
    "LEY DE OHM": {
        "instrucciones": "Ley de Ohm: Relaciona voltaje (V), corriente (I) y resistencia (R). P es la potencia.",
        "formulas": [
            "P=V^2/R",
            "P=I_^2*R",
            "P=V*I_",
            "I_=V/R",
        ]
    }
}
import sympy as sp
def convert_formulas_to_sympy(formulas):
    temas = {}
    instrucciones = {}
    ecuaciones = {}
    
    for tema, data in formulas.items():
        temas[tema] = tema
        instrucciones[tema] = data["instrucciones"]
        ecuaciones[tema] = []  # Initialize list for each tema
        
        for formula in data["formulas"]:
            left, right = formula.split('=')
            equation = (sp.sympify(left), sp.sympify(right))
            ecuaciones[tema].append(equation)
    return temas, instrucciones, ecuaciones
from time import sleep
from datetime import datetime

x=datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
print(type(x))



