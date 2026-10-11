# Nombre del proyecto: Juego de la serpiente

## Integrantes
* Cristopher Alexander Yépez Arredondo

## Descripción
*   El usuario controla la dirección de la serpiente (arriba, abajo, izquierda, derecha) mediante las teclas de flecha, y el sistema valida que no se realicen giros de 180 grados sobre sí misma.
*   El computador genera la comida en una posición aleatoria dentro del tablero (usando `random`), asegurando que no aparezca sobre el cuerpo de la serpiente.
*   El sistema compara la posición de la cabeza de la serpiente con la comida y los bordes: si come, aumenta el puntaje; si choca, el juego termina.
*   Al terminar la partida (colisión), se muestra una pantalla de "Game Over" y se pregunta si se desea reiniciar presionando la tecla "R" (bucle de reinicio).
*   Una lista (`self.serpiente`) almacena las coordenadas de cada segmento del cuerpo, y variables (`self.puntaje`, `self.record`) llevan el marcador y el récord histórico.
*   Al reiniciar o finalizar, se muestra un resumen en pantalla con el puntaje final obtenido, el mejor récord y la opción de volver a jugar.
## Diagrama de Flujo
<p align="center">
  <img width="334" height="558" alt="image" src="https://github.com/user-attachments/assets/fa5fb9fb-e2db-4d22-b88b-4ef130b2fc68" />
</p>
Juego de la serpiente
