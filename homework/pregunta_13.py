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

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    dataframe0 = load_input("files/input/tbl0.tsv")
    dataframe2 = load_input("files/input/tbl2.tsv")
    grouped = dataframe2.groupby("c0")["c5b"].sum()
    dataframe0 = dataframe0.merge(grouped, left_on="c0", right_on="c0")
    return dataframe0.groupby("c1")["c5b"].sum()

print(pregunta_13())