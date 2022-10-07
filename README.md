# Orbita-Satelital

Se busca comprender como se describe la trayectoria de un satélite lanzado desde la Tierra hacia el sistema Plutón - Caronte. Plutón siendo el planeta, y Caronte su respectiva luna.

La trayectoria responde a un sistema de ecuaciones diferenciales que surge de plantear la Ley de Newton para los cuerpos que lo conforman (satélite, planeta, luna).

Para observar los diferentes comportamientos, se parte de una serie de parámetros modificables que buscan diferenciar la interacción individual o conjunta de los componentes del sistema. Es decir, se puede considerar únicamente la presencia de Plutón, agregarle Caronte, y además considerar como posible o no la rotación entre ellos, así como la velocidad deseada.

Para la resolución analítica e iterativa, se pueden utilizar diferentes métodos como Euler Explícito, Runge Kutta 2 y Runge Kutta 4. Se definen la cantidad de pasos y de iteraciones, y la velocidad de lanzamiento del satélite.

En función de estos datos, obtenemos la trayectoria gráficamente y como un vector, y el error obtenido.

Como motivo del estudio de la influencia de la rotación entre cuerpos, se realizaron dos scripts extra, para encontrar de forma experimental los Puntos de Lagrange del sistema.
