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

def pregunta_11():
     """
     Construya una tabla que contenga `c0` y una lista separada por ',' de
     los valores de la columna `c4` del archivo `tbl1.tsv`.

     Rta/
          c0       c4
     0     0    b,f,g
     1     1    a,c,f
     2     2  a,c,e,f
     3     3      a,b
     ...
     37   37  a,c,e,f
     38   38      d,e
     39   39    a,d,f
     """
     dataframe = load_input("files/input/tbl1.tsv")
     dataframe = dataframe.groupby("c0")["c4"].apply(lambda x: ",".join(sorted(x.astype(str)))).reset_index()
     return dataframe