import tkinter as tk
import random

# Configuración de dimensiones y velocidad
ANCHO = 600
ALTO = 500
ALTO_PANEL = 60
TAMANO_BLOQUE = 20
VELOCIDAD = 110  # Milisegundos por fotograma

class JuegoSnake:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de la Serpiente")
        self.root.resizable(False, False)

        # Lienzo (Canvas) donde se dibuja el juego
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="#1e1e2e", highlightthickness=0)
        self.canvas.pack()

        # Variables de estado
        self.direccion = "Right"
        self.siguiente_direccion = "Right"
        self.puntaje = 0
        self.record = 0
        self.game_over = False

        # Eventos de teclado
        self.root.bind("<KeyPress>", self.cambiar_direccion)

        # Iniciar
        self.reiniciar_juego()
        self.actualizar_juego()

    def reiniciar_juego(self):
        # Posición inicial de la serpiente (3 bloques en el centro)
        self.serpiente = [
            (300, 260),
            (280, 260),
            (260, 260)
        ]
        self.direccion = "Right"
        self.siguiente_direccion = "Right"
        self.puntaje = 0
        self.game_over = False
        self.generar_comida()

    def generar_comida(self):
        cols = ANCHO // TAMANO_BLOQUE
        rows = (ALTO - ALTO_PANEL) // TAMANO_BLOQUE
        
        while True:
            self.comida_x = random.randint(0, cols - 1) * TAMANO_BLOQUE
            self.comida_y = random.randint(ALTO_PANEL // TAMANO_BLOQUE, rows + (ALTO_PANEL // TAMANO_BLOQUE) - 1) * TAMANO_BLOQUE
            # Asegurar que la comida no aparezca encima de la serpiente
            if (self.comida_x, self.comida_y) not in self.serpiente:
                break

    def cambiar_direccion(self, evento):
        tecla = evento.keysym
        if tecla in ("Left", "Right", "Up", "Down"):
            # Evitar giro de 180 grados sobre sí mismo
            if (tecla == "Left" and self.direccion != "Right") or \
               (tecla == "Right" and self.direccion != "Left") or \
               (tecla == "Up" and self.direccion != "Down") or \
               (tecla == "Down" and self.direccion != "Up"):
                self.siguiente_direccion = tecla
        elif tecla.lower() == "r" and self.game_over:
            self.reiniciar_juego()

    def actualizar_juego(self):
        if not self.game_over:
            self.direccion = self.siguiente_direccion
            cabeza_x, cabeza_y = self.serpiente[0]

            # Mover la cabeza según la dirección
            if self.direccion == "Left":
                cabeza_x -= TAMANO_BLOQUE
            elif self.direccion == "Right":
                cabeza_x += TAMANO_BLOQUE
            elif self.direccion == "Up":
                cabeza_y -= TAMANO_BLOQUE
            elif self.direccion == "Down":
                cabeza_y += TAMANO_BLOQUE

            nueva_cabeza = (cabeza_x, cabeza_y)

            # Comprobar colisiones
            if cabeza_x < 0 or cabeza_x >= ANCHO or cabeza_y < ALTO_PANEL or cabeza_y >= ALTO or nueva_cabeza in self.serpiente:
                self.game_over = True
            else:
                # Comprobar si come la comida
                if cabeza_x == self.comida_x and cabeza_y == self.comida_y:
                    self.puntaje += 1
                    if self.puntaje > self.record:
                        self.record = self.puntaje
                    self.generar_comida()
                else:
                    self.serpiente.pop()

                self.serpiente.insert(0, nueva_cabeza)

            self.dibujar()

        self.root.after(VELOCIDAD, self.actualizar_juego)

    def dibujar(self):
        self.canvas.delete(tk.ALL)

        # Fondo general
        self.canvas.create_rectangle(0, 0, ANCHO, ALTO, fill="#1e1e2e", outline="")

        # --- DIBUJAR CUADRÍCULA GUÍA ---
        for x in range(0, ANCHO, TAMANO_BLOQUE):
            self.canvas.create_line(x, ALTO_PANEL, x, ALTO, fill="#252538", width=1)
        for y in range(ALTO_PANEL, ALTO, TAMANO_BLOQUE):
            self.canvas.create_line(0, y, ANCHO, y, fill="#252538", width=1)
        # -------------------------------

        # Panel superior de puntaje
        self.canvas.create_rectangle(0, 0, ANCHO, ALTO_PANEL, fill="#181825", outline="")
        self.canvas.create_line(0, ALTO_PANEL, ANCHO, ALTO_PANEL, fill="#45475a", width=2)

        # Textos de puntaje y récord
        self.canvas.create_text(25, 30, text=f"Puntaje: {self.puntaje}", fill="#cdd6f4", font=("Segoe UI", 14, "bold"), anchor="w")
        self.canvas.create_text(ANCHO - 25, 30, text=f"Récord: {self.record}", fill="#cdd6f4", font=("Segoe UI", 14, "bold"), anchor="e")

        # Dibujar comida
        fx, fy = self.comida_x, self.comida_y
        self.canvas.create_oval(fx + 2, fy + 2, fx + TAMANO_BLOQUE - 2, fy + TAMANO_BLOQUE - 2, fill="#f38ba8", outline="")

        # Dibujar serpiente
        for i, (sx, sy) in enumerate(self.serpiente):
            color = "#a6e3a1" if i == 0 else "#6cd86e"
            self.canvas.create_rectangle(sx + 1, sy + 1, sx + TAMANO_BLOQUE - 1, sy + TAMANO_BLOQUE - 1, fill=color, outline="")

        # Pantalla de Game Over
        if self.game_over:
            x1, y1, x2, y2 = 130, 140, 470, 360
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#181825", outline="#45475a", width=2)
            
            self.canvas.create_text(ANCHO // 2, y1 + 45, text="¡FIN DEL JUEGO!", fill="#f38ba8", font=("Segoe UI", 20, "bold"))
            self.canvas.create_text(ANCHO // 2, y1 + 100, text=f"Puntaje Final: {self.puntaje}", fill="#cdd6f4", font=("Segoe UI", 14))
            self.canvas.create_text(ANCHO // 2, y1 + 135, text=f"Mejor Récord: {self.record}", fill="#a6e3a1", font=("Segoe UI", 14))
            self.canvas.create_text(ANCHO // 2, y1 + 190, text="Presiona [R] para Reintentar", fill="#cdd6f4", font=("Segoe UI", 12, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoSnake(root)
    root.mainloop()