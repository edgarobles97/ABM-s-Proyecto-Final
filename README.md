# Love Match (Matching Markets) - Proyecto final Modelos Basados en Agentes 
## CIDE - 10/12/19


### Luis Eduardo García Ávalos
### Daniel Juárez Bautista
### Edgar Robles Díaz

#### Abstract
   Los modelos de pareo se han limitado a explorar la selección de agentes con modelos analíticos, haciendo énfasis en los entornos con información perfecta. Normalmente, en los mercados de parejas, los resultados de los modelos analíticos arrojan asignaciones eficientes. Sin embargo, el supuesto de información perfecta no es plausible para todos los mercados de parejas. 
  
   La contribución del modelo LoveMatch radica en que las asignaciones no siempre serán eficientes y proporciona un resultado diferente: si bien los individuos que no tienen cualidades muy deseadas por otros quedarán sin pareja, el modelo también arroja que existirán individuos con cualidades muy deseadas por otros pero que no serán emparejados. 
   
   Dentro de las principales características del modelo que generan cambios a comparación de los modelos tradicionales, está que los agentes solo observan a su vecindad y no todo el mercado. Esto lleva a resultados no eficientes donde, a diferencia de los modelos analíticos, aunque la proporción de agentes sea la misma, no todos se emparejan.

#### Descripción del modelo
   En este modelo se asigna a un númereo de agentes y se distribuyen de manera aleatoria en el grid (50x50). Su aparición es simultánea así como su interacción. En este modelo, los agentes hacen un Random walk en el grid y en cada paso evalúan a sus vecinos en un radio de una celda. Si encuentra agentes del sexo opuesto y si estos cumplen sus características esperadas y viceversa, entonces se realiza un match y ambos agentes desaparecen del modelo. En caso de que uno de los agentes no satisfaga las características del otro, entonces no se realiza un match y los agentes siguen en su camino aleatorio. Cada agente tiene un parámetro de paciencia, es decir, un número de ticks en el cual este abandona el grid. Cada agente tiene un contador que indica el número de ticks que ha pasado sin encontrar un match, si este número iguala a la paciencia individual de cada agente, entonces este abandona el grid y sale del modelo. El modelo finaliza cuando ya no quedan agentes en el grid. Asimismo, el modelo captura también, variables de interés respecto a cuantas parejas se hicieron y cuantos individuos se quedaron solteros
   
#### Características:
  
  - MultiGrid donde los agentes pueden compartir espacio dentro de la misma celda.
  
  - DataCollector donde se recopila la información relevante de los agentes: (género, belleza y riqueza, así como sus respectivas           expectativas y paciencia). Asimismo, también recopila información del modelo: (# matches, # solteros)
  
  - Parámetros iniciales que el usuario puede modificar (densidad de población y proporción de un género sobre otro)
  
  - Server donde se ajustan los parámetros para su visualización en un grid abstracto de tamaño 50x50

#### El repositorio consiste de cinco partes:
  
  - LoveMatch.py: Este script contiene al modelo base, LoveMatch, así como a los agentes y definen sus steps y schedules a seguir.
  
  - LoveMatchserver.py: En este script está toda la información relevante al ajuste de la visualización en un servidor local.
  
  - LoveMatchRun.py: Este script ejecuta el modelo y carga la variable server encontrada en el archivo anterior.
  
  - ODD y paper académico presentando el modelo.
  
  - Data Analysis: Subcarpeta con tres Jupyter Notebooks que contienen información estadística para tres versiones distintas del modelo.
  
     - En esta carpeta se extraen estadísticas descriptivas bajo tres circunstancias distintas. En primer lugar, se evalúa un modelo donde las expectativas de los agentes son menores a sus características. Es decir, estos tienen un nivel de belleza y riqueza mayor a lo que esperan. Esta versión se le denomina como (good). La segunda versión representa el caso contrario, donde las expectativas de los agentes superan a sus características personales. Este versión se conoce como (greedy). Finalmente, tenemos una extensión donde se evalúa el modelo cuando hay una desproporción entre el tipo (género) de los agentes. Esta versión se asigna como (unbalanced).
   
     - El propósito de este análisis consiste en modelar la dinámica de este matching market bajo diferentes circunstancias. En el primer y segundo jupyter notebook se modifican las preferencias y características de los agentes. En la tercera versión del modelo, se modifica la estructura poblacional de los agentes. 
   
        -Nota: la modificación de las expectativas de los agentes no está presente como un slider dentro de la visualización, es decir, la modificación se tuvo que realizar dentro de los parámetros del modelo. En la versión (good)  se utlizaron como parámetros una media de 0.5 y desviación de 0.6 para las expectativas y media de 1 y desviación de  0.3 para las características de los individuos. En la versión (greedy) se estableció una media de 1 y desviación de 0.3 para las expectativas y media de 0.7 y desviación de 0.3.
  
  

  
 
