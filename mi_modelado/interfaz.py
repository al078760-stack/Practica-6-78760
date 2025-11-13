# interfaz.py
import tkinter as tk
from tkinter import ttk, messagebox
from analisis import generar_matriz_elevaciones
from diseno import calcular_pendientes, estadisticas_pendientes

class AplicacionPendientes:
    def _init_(self, root):
        self.root = root
        self.root.title("Análisis de Pendientes Topográficas")
        self.root.geometry("650x500")

        self.label_titulo = tk.Label(root, text="🏔️ Análisis de Pendientes Topográficas", 
                                     font=("Arial", 16, "bold"))
        self.label_titulo.pack(pady=10)

        self.btn_generar = tk.Button(root, text="Generar y Analizar Terreno", 
                                     command=self.analizar, font=("Arial", 12))
        self.btn_generar.pack(pady=10)

        self.tree = ttk.Treeview(root)
        self.tree.pack(pady=10)

        self.label_resultados = tk.Label(root, text="", font=("Arial", 12))
        self.label_resultados.pack(pady=10)

    def analizar(self):
        matriz = generar_matriz_elevaciones()
        pendientes = calcular_pendientes(matriz)
        max_p, min_p, prom_p = estadisticas_pendientes(pendientes)

        # Mostrar tabla
        self.mostrar_tabla(matriz)

        # Mostrar resultados
        resultado_texto = (
            f"📈 Pendiente Máxima: {max_p}%\n"
            f"📉 Pendiente Mínima: {min_p}%\n"
            f"⚖️ Pendiente Promedio: {prom_p}%"
        )
        self.label_resultados.config(text=resultado_texto)

        messagebox.showinfo("Análisis Completado", "El análisis de pendientes ha finalizado exitosamente.")

    def mostrar_tabla(self, matriz):
        for col in self.tree.get_children():
            self.tree.delete(col)

        filas = len(matriz)
        columnas = len(matriz[0])
        self.tree["columns"] = [f"C{j}" for j in range(columnas)]
        self.tree["show"] = "headings"

        for j in range(columnas):
            self.tree.heading(f"C{j}", text=f"Col {j+1}")

        for i in range(filas):
            self.tree.insert("", "end", values=matriz[i])

if _name_ == "_main_":
    root = tk.Tk()
    app = AplicacionPendientes(root)
    root.mainloop()