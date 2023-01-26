import streamlit as st
st.set_page_config(layout="wide")
import numpy as np


# Clase Neuron
# Reutilizamos la clase Neuron del ejercicio anterior

class Neuron():
  def __init__ (self, weights, bias, func):  
    self.weights = weights
    self.bias = bias
    self.func = func

  def opera(self, x):      
      result = np.dot(self.weights, x) + self.bias 

      if self.func == "sigm":
        ejemplo = self.__sigmoide(result)
        return ejemplo
       
      elif self.func == 'relu':
        ejemplo = self.__relu(result)
        return ejemplo
      
      elif self.func == 'tanh':
        ejemplo = self.__tanh(result)
        return ejemplo
     
      else:
        print("Opcion erronea") # en caso de recibir una opción no existente
        

  def __sigmoide(self, x): # funcion privada
    y = (1/(1 + np.exp(-x)))
    return y

  def __relu(self, result): # funcion privada
    return max(0.0, result)
      
  def __tanh(self, result): # funcion privada
    return np.tanh(result)

  def changeWeights(self, weights): # cambio de peso
    self.weights = weights
    print(f"El nuevo peso ", self.weights)
    return 

  def changeBias(self, bias): # cambio de sesgo
    self.bias = bias
    print(f"El nuevo sesgo es ", self.bias)
    return


st.title("Neurona")
# titulo de la pagina

st.image("https://concepto.de/wp-content/uploads/2018/09/neuronas2-e1537381557413.jpg",
            width=400)

st.header('Simulador de neurona')

neurona = st.slider('Escoge la cantidad de pesos y entradas que deseas.', 1, 10)





w = [] # lista para guardar los valores de los pesos
x = [] # lista para guardar los valores de las entradas

st.subheader("Pesos")


columnasw = st.columns(neurona) # columna de los pesos
for i, col in enumerate(columnasw):

  with col:
    peso = st.number_input(f'Introduce el peso', key = f'w{i}')
    w.append(peso)


st.markdown(f'$w$ = {w}') # muestra el total de pesos


st.subheader("Entradas")

columnasx = st.columns(neurona)
for j, colx in enumerate(columnasx):

  with colx:
    entrada = st.number_input(f'Escribe la entrada', key = f'x{j}') 

    x.append(entrada)

st.markdown(f'$x$ = {x}') # muestra el total de entradas






colsesg, colfun = st.columns(2) # columnas de sesgo y funcion

with colsesg:
    
    sesgo = st.number_input('Introduce el valor del sesgo', key = 'bias')
    st.markdown(f'$b$ = {sesgo}')


with colfun:

    funcion_op = st.selectbox('Escoge la función que desees', ['Sigmoide', 'ReLU', 'Tangente Hipérbolica'])
    st.text(f'Has escogido:  {funcion_op}')
    # Creamos el dicicionario FUNCTIONS para mostrar las opciones 
    # y no el valor de funcion_op para que quede más bonito

    FUNCTIONS = {'Sigmoide' : 'sigm', 'ReLU' : 'relu', 'Tangente Hipérbolica' : 'tanh'}

if st.button('Calcular la salida: '):
  neuron = Neuron(weights=peso, bias=sesgo, func=FUNCTIONS[funcion_op])
  calculo = neuron.opera(entrada)

  st.text(f'El resultado es tras haber escogido {neurona} pesos/entradas y la funcion  {funcion_op} es {calculo}')
