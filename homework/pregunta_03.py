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
            delimiter="\t",
        )
    return dataframe

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    dataframe = load_input("files/input/tbl0.tsv")
    return dataframe.groupby("c1").size().rename("count")