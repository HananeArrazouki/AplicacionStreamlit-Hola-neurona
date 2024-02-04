# Importar las librerias
import streamlit as st

# Añadir una imágen
st.image('img/neurona.png', width=450)

# Añadir un título
st.title('¡Hola neurona!')

"""
Primera forma:

"""

"""
   Función para representar y calcular la salida de una neurona con una entrada y un peso.

   Interfaz de Usuario:
   - Muestra un encabezado indicando la configuración de la neurona.
   - Utiliza un control deslizante para definir el peso de la única entrada.
   - Permite al usuario ingresar el valor de la entrada mediante un campo de entrada numérica.
   - Calcula la salida de la neurona multiplicando la entrada por el peso.
   - Presenta un botón para calcular y mostrar la salida cuando se presiona.
"""
def neurona_una_entrada():
   # Mostrar el encabezado
   st.header("Una neurona con una entrada y un peso")

   # Definir el peso mediante un control deslizante
   peso_1 = st.slider('Peso', 0.0, 5.0, key=1)

   # Ingresar el valor de la entrada mediante un campo numérico
   entrada_1 = st.number_input('Introduzca el valor de la entrada', key=2)

   # Calcular la salida de la neurona multiplicando la entrada por el peso
   salida_1 = entrada_1 * peso_1

   # Mostrar la salida cuando se presiona el botón "Calcular la salida"
   if st.button("Calcular la salida", key=3):
      st.write('La salida de la neurona es', salida_1)

"""
   Función que representa y calcula la salida de una neurona con dos entradas y dos pesos.

   Interfaz de Usuario:
   - Muestra un encabezado indicando la configuración de la neurona.
   - Utiliza dos controles deslizantes para definir los pesos de las dos entradas.
   - Permite al usuario ingresar los valores de las entradas mediante campos de entrada numérica.
   - Calcula la salida de la neurona como la suma ponderada de las entradas y pesos.
   - Presenta un botón para calcular y mostrar la salida cuando se presiona.
"""
def neurona_dos_entradas():
   # Mostrar el encabezado
   st.header("Una neurona con dos entradas y dos pesos")

   # Crear dos columnas para los controles de entrada
   col_2 = st.columns(2)

   # Definir el primer peso mediante un control deslizante
   peso_2_0 = col_2[0].slider('Peso w₀', 0.0, 5.0, key=4)

   # Definir el segundo peso mediante otro control deslizante
   peso_2_1 = col_2[1].slider('Peso w₁', 0.0, 5.0, key=5)

   # Ingresar el valor de la primera entrada mediante un campo numérico
   entrada_2_0 = col_2[0].number_input('Entrada x₀', key=6)

   # Ingresar el valor de la segunda entrada mediante otro campo numérico
   entrada_2_1 = col_2[1].number_input('Entrada x₁', key=7)

   # Calcular la salida de la neurona como la suma ponderada de entradas y pesos
   salida_2 = (entrada_2_0 * peso_2_0) + (entrada_2_1 * peso_2_1)

   # Mostrar la salida cuando se presiona el botón "Calcular la salida"
   if st.button("Calcular la salida", key=8):
      st.write('La salida de la neurona es', salida_2)

"""
   Función que representa y calcula la salida de una neurona con tres entradas y sesgo.

   Interfaz de Usuario:
   - Muestra un encabezado indicando la configuración de la neurona.
   - Utiliza tres controles deslizantes para definir los pesos de las tres entradas.
   - Permite al usuario ingresar los valores de las entradas mediante campos de entrada numérica.
   - Incluye un campo de entrada para definir el valor del sesgo.
   - Calcula la salida de la neurona como la suma ponderada de entradas y pesos, más el sesgo.
   - Presenta un botón para calcular y mostrar la salida cuando se presiona.
"""
def neurona_tres_entradas_sesgo():
   # Mostrar el encabezado
   st.header("Una neurona con tres entradas y sesgo")

   # Crear tres columnas para los controles de entrada
   col_3 = st.columns(3)

   # Definir los pesos mediante controles deslizantes
   peso_3_0 = col_3[0].slider('Peso w₀', 0.0, 5.0, key=9)
   peso_3_1 = col_3[1].slider('Peso w₁', 0.0, 5.0, key=10)
   peso_3_2 = col_3[2].slider('Peso w₂', 0.0, 5.0, key=11)

   # Ingresar los valores de las entradas mediante campos numéricos
   entrada_3_0 = col_3[0].number_input('Entrada x₀', key=12)
   entrada_3_1 = col_3[1].number_input('Entrada x₁', key=13)
   entrada_3_2 = col_3[2].number_input('Entrada x₂', key=14)

   # Ingresar el valor del sesgo mediante un campo numérico
   sesgo = st.number_input('Introduzca el valor del sesgo', key=15)

   # Calcular la salida de la neurona como la suma ponderada de entradas y pesos, más el sesgo
   salida_3 = (entrada_3_0 * peso_3_0) + (entrada_3_1 * peso_3_1) + (entrada_3_2 * peso_3_2) + sesgo

   # Mostrar la salida cuando se presiona el botón "Calcular la salida"
   if st.button("Calcular la salida", key=16):
      st.write('La salida de la neurona es', salida_3)

# Crear pestañas para diferentes configuraciones de entrada en la neurona
entradas = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Llamar a las funciones correspondientes según la pestaña seleccionada
with entradas[0]:
   neurona_una_entrada()

with entradas[1]:
   neurona_dos_entradas()

with entradas[2]:
   neurona_tres_entradas_sesgo()


"""
Segunda forma:

"""

# Crear pestañas para diferentes configuraciones de entrada en la neurona
# entradas = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# # Configuración para una neurona con una entrada y un peso
# with entradas[0]:
#    st.header("Una neurona con una entrada y un peso")
#    peso_1 = st.slider('Peso', 0.0, 5.0, key=1)
#    entrada_1 = st.number_input('Introduzca el valor de la entrada', key=2)

#    # Calcular la salida de la neurona
#    salida_1 = entrada_1 * peso_1

#    # Mostrar la salida cuando se presiona el botón
#    if st.button("Calcular la salida", key=3):
#       st.write('La salida de la neurona es', salida_1)

# # Configuración para una neurona con dos entradas y dos pesos
# with entradas[1]:
#    st.header("Una neurona con dos entradas y dos pesos")
#    col_2 = st.columns(2)
#    peso_2_0 = col_2[0].slider('Peso w₀', 0.0, 5.0, key=4)
#    peso_2_1 = col_2[1].slider('Peso w₁', 0.0, 5.0, key=5)

#    entrada_2_0 = col_2[0].number_input('Entrada x₀', key=6)
#    entrada_2_1 = col_2[1].number_input('Entrada x₁', key=7)

#    salida_2 = (entrada_2_0 * peso_2_0) + (entrada_2_1 * peso_2_1)

#    if st.button("Calcular la salida", key=8):
#       st.write('La salida de la neurona es', salida_2)

# # Configuración para una neurona con tres entradas y sesgo
# with entradas[2]:
#    st.header("Una neurona con tres entradas y bias")
#    col_3 = st.columns(3)
#    peso_3_0 = col_3[0].slider('Peso w₀', 0.0, 5.0, key=9)
#    peso_3_1 = col_3[1].slider('Peso w₁', 0.0, 5.0, key=10)
#    peso_3_2 = col_3[2].slider('Peso w₂', 0.0, 5.0, key=11)

#    entrada_3_0 = col_3[0].number_input('Entrada x₀', key=12)
#    entrada_3_1 = col_3[1].number_input('Entrada x₁', key=13)
#    entrada_3_2 = col_3[2].number_input('Entrada x₂', key=14)

#    sesgo = st.number_input('Introduzca el valor del sesgo', key=15)

#    salida_3 = (entrada_3_0 * peso_3_0) + (entrada_3_1 * peso_3_1) + (entrada_3_2 * peso_3_2) + sesgo

#    if st.button("Calcular la salida", key=16):
#       st.write('La salida de la neurona es', salida_3)