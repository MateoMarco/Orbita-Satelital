# Orbita-Satelital

Se busca comprender como se describe la trayectoria de un satélite lanzado desde la Tierra hacia el sistema Plutón - Caronte. Plutón siendo el planeta, y Caronte su respectiva luna.

La trayectoria responde a un sistema de ecuaciones diferenciales que surge de plantear la Ley de Newton para los cuerpos que lo conforman (satélite, planeta, luna).

Para observar los diferentes comportamientos, se parte de una serie de parámetros modificables que buscan diferenciar la interacción individual o conjunta de los componentes del sistema. Es decir, se puede considerar únicamente la presencia de Plutón, agregarle Caronte, y además considerar como posible o no la rotación entre ellos, así como la velocidad deseada.
Para la resolución analítica e iterativa, se pueden utilizar diferentes métodos como Euler Explícito, Runge Kutta 2 y Runge Kutta 4. Se definen la cantidad de pasos y de iteraciones, y la velocidad de lanzamiento del satélite.

En función de estos datos, obtenemos la trayectoria gráficamente y como un vector. 

Se estudia la precisión (error) de los tres métodos de resolución, comparandolos tanto a nivel de esfuerzo computacional, como de eficiencia.

<img width="248" alt="image" src="https://user-images.githubusercontent.com/115170998/194643733-2243ce70-0d07-4c98-a21d-bf54e7f14747.png">
<img width="280" alt="image" src="https://user-images.githubusercontent.com/115170998/194643761-4ad5a810-0cca-4313-bab8-26179a1c9244.png">

Se analizaron diferentes casos, teniendo en cuenta todas las variables posibles, obteniendo trayectorias elípticas, circulares perfectas, fallidos (choques).

<img width="278" alt="image" src="https://user-images.githubusercontent.com/115170998/194644207-0cb734c9-ce59-45a1-bf40-f265a47efce5.png">
<img width="254" alt="image" src="https://user-images.githubusercontent.com/115170998/194644239-e24e2fd4-64a3-4352-abe8-1a1d2dee359b.png">
<img width="225" alt="image" src="https://user-images.githubusercontent.com/115170998/194644384-4095d36f-cbf1-4920-80b2-2938e4664c56.png">

Tambien se obtuvo el rango de velocidades para el cuál el satélite no permanece orbitando alrededor del sistema, y sale expulsado.

<img width="213" alt="image" src="https://user-images.githubusercontent.com/115170998/194644567-11ba8879-2eec-4076-b1bb-130963b41707.png">

Finalmente, se realizó un análisis de la conservación de la energía del sistema, para los diferentes casos.

<img width="208" alt="image" src="https://user-images.githubusercontent.com/115170998/194644822-1d5cf1c6-2c1b-4f5d-976a-ab9baf2351b2.png">
<img width="209" alt="image" src="https://user-images.githubusercontent.com/115170998/194644847-0fcbab30-a61c-41e5-86a9-b1a1f5a4880d.png">
<img width="217" alt="image" src="https://user-images.githubusercontent.com/115170998/194644914-5d9b39f1-ae04-419a-9240-59763a7c57df.png">
<img width="196" alt="image" src="https://user-images.githubusercontent.com/115170998/194644938-7c032143-00ee-477b-8d09-323af50a6e18.png">
