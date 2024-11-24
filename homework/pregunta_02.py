"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import glob
import pandas as pd

# Carga los datos de un archivo.
def load_input(path: str):
    files = glob.glob(path)
    dataframe = pd.read_csv(
            files[0],
            header=None,
            delimiter="\t",
            index_col=None,
            skiprows=1
        )
    return dataframe

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    dataframe = load_input("files/input/tbl0.tsv")
    return dataframe.shape[1]