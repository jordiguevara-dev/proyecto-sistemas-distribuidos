import tkinter as tk
from tkinter import messagebox, ttk
import requests

# === CONFIGURACIÓN DE RED (CAMBIAR AQUÍ) ===
# Pon la IP Externa de tu VM 'instancia-middleware' de Google Cloud
IP_NUBE = "34.68.239.254"  
PUERTO_JAVA = "8080" # Asegúrate que sea el mismo que usa tu Java

BASE_URL = f"http://{IP_NUBE}:{PUERTO_JAVA}/api/inventario"
URL_PEDIDO = f"{BASE_URL}/pedido"
URL_LISTA = f"{BASE_URL}/lista"
URL_REGISTRO = f"{BASE_URL}/registrar"

class AppNeptuno:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema JORDI GUEVARA - DISTRIBUIDO")
        self.root.geometry("700x600")

        tk.Label(root, text="Sistema JORDI GUEVARA", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white", pady=10).pack(fill=tk.X)

        # --- SECCIÓN TABLA ---
        tk.Label(root, text="Inventario T1 (Remoto):", font=("Arial", 10, "bold")).pack(pady=5)
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Stock"), show="headings", height=8)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre del Producto")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(root, text="🔄 Sincronizar con Google Cloud", command=self.cargar_productos).pack()

        # --- SECCIÓN VENTA ---
        frame_venta = tk.LabelFrame(root, text=" Módulo de Ventas (Salida) ", padx=10, pady=10, fg="blue")
        frame_venta.pack(pady=10, padx=20, fill=tk.X)
        tk.Label(frame_venta, text="ID:").grid(row=0, column=0)
        self.ent_id_v = ttk.Entry(frame_venta, width=10); self.ent_id_v.grid(row=0, column=1)
        tk.Label(frame_venta, text="Cant:").grid(row=0, column=2)
        self.ent_cant_v = ttk.Entry(frame_venta, width=10); self.ent_cant_v.grid(row=0, column=3)
        ttk.Button(frame_venta, text="REALIZAR VENTA", command=self.enviar_pedido).grid(row=0, column=4, padx=10)

        # --- SECCIÓN REGISTRO ---
        frame_reg = tk.LabelFrame(root, text=" Registro de Nuevos Productos (Entrada) ", padx=10, pady=10, fg="green")
        frame_reg.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(frame_reg, text="Nuevo ID:").grid(row=0, column=0)
        self.reg_id = ttk.Entry(frame_reg, width=10); self.reg_id.grid(row=0, column=1)
        tk.Label(frame_reg, text="Nombre:").grid(row=0, column=2)
        self.reg_nom = ttk.Entry(frame_reg, width=20); self.reg_nom.grid(row=0, column=3)
        tk.Label(frame_reg, text="Stock Inicial:").grid(row=0, column=4)
        self.reg_stock = ttk.Entry(frame_reg, width=10); self.reg_stock.grid(row=0, column=5)
        
        ttk.Button(frame_reg, text="REGISTRAR", command=self.registrar_producto).grid(row=1, column=0, columnspan=6, pady=10)

        self.cargar_productos()

    def cargar_productos(self):
        try:
            for item in self.tabla.get_children(): self.tabla.delete(item)
            res = requests.get(URL_LISTA, timeout=5)
            for p in res.json():
                self.tabla.insert("", tk.END, values=(p['id'], p['nombre'], p['stock']))
        except Exception as e: 
            messagebox.showerror("Error", f"Middleware desconectado en {IP_NUBE}")

    def registrar_producto(self):
        try:
            data = {"id": int(self.reg_id.get()), "nombre": self.reg_nom.get(), "stock": int(self.reg_stock.get())}
            res = requests.post(URL_REGISTRO, json=data, timeout=5)
            messagebox.showinfo("Registro", res.text)
            self.cargar_productos()
        except Exception as e: messagebox.showerror("Error", f"Fallo al registrar: {e}")

    def enviar_pedido(self):
        try:
            res = requests.post(URL_PEDIDO, json={"id": int(self.ent_id_v.get()), "cantidad": int(self.ent_cant_v.get())}, timeout=5)
            messagebox.showinfo("Venta", res.text)
            self.cargar_productos()
        except Exception as e: messagebox.showerror("Error", f"Fallo en venta: {e}")

if __name__ == "__main__":
    root = tk.Tk(); app = AppNeptuno(root); root.mainloop()