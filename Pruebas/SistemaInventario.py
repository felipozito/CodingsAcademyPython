import tkinter as tk
from tkinter import messagebox, ttk

# Clase base abstracta para productos (Abstracción)
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    # Método abstracto (Polimorfismo)
    def get_tipo(self):
        raise NotImplementedError("Método abstracto")

# Clase derivada para productos electrónicos (Herencia)
class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia  # en meses
    
    def get_tipo(self):
        return "Electrónico"
    
    def get_info_extra(self):
        return f"Garantía: {self.garantia} meses"

# Clase derivada para productos alimenticios (Herencia)
class Alimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad
    
    def get_tipo(self):
        return "Alimenticio"
    
    def get_info_extra(self):
        return f"Caduca: {self.fecha_caducidad}"

# Clase para manejar el inventario (Encapsulamiento)
class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                return True
        return False
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def obtener_todos_productos(self):
        return self.productos
    
    def valor_total_inventario(self):
        return sum(p.calcular_valor_total() for p in self.productos)

# Interfaz gráfica con Tkinter
class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario POO")
        self.root.geometry("800x600")
        
        self.inventario = Inventario()
        
        self.crear_widgets()
        self.cargar_datos_ejemplo()
    
    def cargar_datos_ejemplo(self):
        # Agregar algunos productos de ejemplo
        self.inventario.agregar_producto(Electronico("Laptop", 1200, 5, 24))
        self.inventario.agregar_producto(Alimenticio("Leche", 2.5, 50, "2023-12-31"))
        self.inventario.agregar_producto(Electronico("Teléfono", 600, 10, 12))
        self.actualizar_lista()
    
    def crear_widgets(self):
        # Frame para el formulario
        form_frame = tk.LabelFrame(self.root, text="Agregar Producto", padx=10, pady=10)
        form_frame.pack(padx=10, pady=5, fill="x")
        
        # Campos del formulario
        tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.nombre_entry = tk.Entry(form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        
        tk.Label(form_frame, text="Precio:").grid(row=1, column=0, sticky="e")
        self.precio_entry = tk.Entry(form_frame)
        self.precio_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        
        tk.Label(form_frame, text="Cantidad:").grid(row=2, column=0, sticky="e")
        self.cantidad_entry = tk.Entry(form_frame)
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")
        
        tk.Label(form_frame, text="Tipo:").grid(row=3, column=0, sticky="e")
        self.tipo_var = tk.StringVar(value="Electrónico")
        self.tipo_menu = ttk.Combobox(form_frame, textvariable=self.tipo_var, 
                                    values=["Electrónico", "Alimenticio"])
        self.tipo_menu.grid(row=3, column=1, padx=5, pady=5, sticky="we")
        
        tk.Label(form_frame, text="Info Extra:").grid(row=4, column=0, sticky="e")
        self.info_extra_entry = tk.Entry(form_frame)
        self.info_extra_entry.grid(row=4, column=1, padx=5, pady=5, sticky="we")
        
        # Botones
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(button_frame, text="Agregar", command=self.agregar_producto).pack(side="left", padx=5)
        tk.Button(button_frame, text="Eliminar", command=self.eliminar_producto).pack(side="left", padx=5)
        tk.Button(button_frame, text="Buscar", command=self.buscar_producto).pack(side="left", padx=5)
        tk.Button(button_frame, text="Limpiar", command=self.limpiar_formulario).pack(side="left", padx=5)
        
        # Lista de productos
        list_frame = tk.LabelFrame(self.root, text="Inventario", padx=10, pady=10)
        list_frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        columns = ("Nombre", "Precio", "Cantidad", "Tipo", "Info Extra", "Valor Total")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", selectmode="browse")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        
        self.tree.pack(fill="both", expand=True)
        
        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Etiqueta para el valor total del inventario
        self.total_label = tk.Label(self.root, text="Valor total del inventario: $0.00", 
                                   font=("Arial", 10, "bold"))
        self.total_label.pack(pady=5)
    
    def agregar_producto(self):
        try:
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            tipo = self.tipo_var.get()
            info_extra = self.info_extra_entry.get()
            
            if not nombre:
                messagebox.showerror("Error", "El nombre no puede estar vacío")
                return
            
            if tipo == "Electrónico":
                producto = Electronico(nombre, precio, cantidad, int(info_extra))
            elif tipo == "Alimenticio":
                producto = Alimenticio(nombre, precio, cantidad, info_extra)
            else:
                messagebox.showerror("Error", "Tipo de producto no válido")
                return
            
            self.inventario.agregar_producto(producto)
            self.actualizar_lista()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
    
    def eliminar_producto(self):
        nombre = self.nombre_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del producto a eliminar")
            return
        
        if self.inventario.eliminar_producto(nombre):
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "Producto no encontrado")
    
    def buscar_producto(self):
        nombre = self.nombre_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del producto a buscar")
            return
        
        producto = self.inventario.buscar_producto(nombre)
        if producto:
            self.limpiar_formulario()
            self.nombre_entry.insert(0, producto.nombre)
            self.precio_entry.insert(0, str(producto.precio))
            self.cantidad_entry.insert(0, str(producto.cantidad))
            self.tipo_var.set(producto.get_tipo())
            
            if isinstance(producto, Electronico):
                self.info_extra_entry.insert(0, str(producto.garantia))
            elif isinstance(producto, Alimenticio):
                self.info_extra_entry.insert(0, producto.fecha_caducidad)
            
            messagebox.showinfo("Encontrado", f"Producto encontrado: {producto.nombre}")
        else:
            messagebox.showerror("No encontrado", "Producto no encontrado")
    
    def limpiar_formulario(self):
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.tipo_var.set("Electrónico")
        self.info_extra_entry.delete(0, tk.END)
    
    def actualizar_lista(self):
        # Limpiar la lista actual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Agregar todos los productos
        for producto in self.inventario.obtener_todos_productos():
            self.tree.insert("", tk.END, values=(
                producto.nombre,
                f"${producto.precio:.2f}",
                producto.cantidad,
                producto.get_tipo(),
                producto.get_info_extra(),
                f"${producto.calcular_valor_total():.2f}"
            ))
        
        # Actualizar el valor total del inventario
        self.total_label.config(text=f"Valor total del inventario: ${self.inventario.valor_total_inventario():.2f}")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()