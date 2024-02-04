# Importar las librerias
import streamlit as st

# Añadir una imágen
st.image('img/neurona.png', width=450)

# Añadir un título
st.title('¡Hola neurona!')

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
entradas = st.radio("Seleccionar tipo de entrada", ["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Llamar a las funciones correspondientes según la pestaña seleccionada
if entradas == "Una entrada":
   neurona_una_entrada()
elif entradas == "Dos entradas":
   neurona_dos_entradas()
elif entradas == "Tres entradas y sesgo":
   neurona_tres_entradas_sesgo()



# # Create tabs for different configurations of input in the neuron
# selected_tab = st.radio("Seleccionar tipo de entrada", ["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# # Configuration for a neuron with one input and one weight
# if selected_tab == "Una entrada":
#     st.header("Una neurona con una entrada y un peso")
#     peso_1 = st.slider('Peso', 0.0, 5.0, key=1)
#     entrada_1 = st.number_input('Introduzca el valor de la entrada', key=2)

#     # Calculate neuron output
#     salida_1 = entrada_1 * peso_1

#     # Display the output when the button is pressed
#     if st.button("Calcular la salida", key=3):
#         st.write('La salida de la neurona es', salida_1)

# # Configuration for a neuron with two inputs and two weights
# elif selected_tab == "Dos entradas":
#     st.header("Una neurona con dos entradas y dos pesos")
#     col_2 = st.columns(2)
#     peso_2_0 = col_2[0].slider('Peso w₀', 0.0, 5.0, key=4)
#     peso_2_1 = col_2[1].slider('Peso w₁', 0.0, 5.0, key=5)

#     entrada_2_0 = col_2[0].number_input('Entrada x₀', key=6)
#     entrada_2_1 = col_2[1].number_input('Entrada x₁', key=7)

#     salida_2 = (entrada_2_0 * peso_2_0) + (entrada_2_1 * peso_2_1)

#     if st.button("Calcular la salida", key=8):
#         st.write('La salida de la neurona es', salida_2)

# # Configuration for a neuron with three inputs and bias
# elif selected_tab == "Tres entradas y sesgo":
#     st.header("Una neurona con tres entradas y bias")
#     col_3 = st.columns(3)
#     peso_3_0 = col_3[0].slider('Peso w₀', 0.0, 5.0, key=9)
#     peso_3_1 = col_3[1].slider('Peso w₁', 0.0, 5.0, key=10)
#     peso_3_2 = col_3[2].slider('Peso w₂', 0.0, 5.0, key=11)

#     entrada_3_0 = col_3[0].number_input('Entrada x₀', key=12)
#     entrada_3_1 = col_3[1].number_input('Entrada x₁', key=13)
#     entrada_3_2 = col_3[2].number_input('Entrada x₂', key=14)

#     sesgo = st.number_input('Introduzca el valor del sesgo', key=15)

#     salida_3 = (entrada_3_0 * peso_3_0) + (entrada_3_1 * peso_3_1) + (entrada_3_2 * peso_3_2) + sesgo

#     if st.button("Calcular la salida", key=16):
#         st.write('La salida de la neurona es', salida_3)
