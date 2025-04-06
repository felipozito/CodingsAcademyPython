import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton,ReplyParameters, InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = "8022254585:AAHx-GP_74_N-Qdfa0ap6Ti3oV0zfjPfhQY"
bot = telebot.TeleBot(TOKEN)
# Base de datos mejorada
productos_db = {
    # Por categorías
    "ropa": {
        "camisetas": {
            "descripcion": "Camisetas de algodón 100%",
            "precios": {"Básica": 15.99, "Premium": 24.99, "Exclusiva": 32.50},
            "categoria": "ropa"
        },
        "pantalones": {
            "descripcion": "Pantalones de diversos materiales",
            "precios": {"Jeans": 39.99, "Chinos": 34.50, "Deportivos": 29.99},
            "categoria": "ropa"
        }
    },
    "calzado": {
        "zapatos": {
            "descripcion": "Zapatos para todas las ocasiones",
            "precios": {"Deportivos": 59.99, "Formales": 79.50, "Casuales": 49.99},
            "categoria": "calzado"
        },
        "sandalias": {
            "descripcion": "Sandalias cómodas y elegantes",
            "precios": {"Playa": 29.99, "Vestir": 45.50, "Deportivas": 39.99},
            "categoria": "calzado"
        }
    },
    "accesorios": {
        "relojes": {
            "descripcion": "Relojes de calidad premium",
            "precios": {"Analógico": 89.99, "Digital": 75.50, "Deportivo": 65.99},
            "categoria": "accesorios"
        },
        "gorras": {
            "descripcion": "Gorras de diferentes estilos",
            "precios": {"Béisbol": 19.99, "Pesca": 24.50, "Estilo urbano": 22.99},
            "categoria": "accesorios"
        }
    }
}
# Diccionario plano para búsquedas
todos_productos = {}
for categoria in productos_db.values():
    for producto, detalles in categoria.items():
        todos_productos[producto] = detalles

# Menú principal con 3 botones
def menu_principal():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        KeyboardButton("📦Productos"),
        KeyboardButton("🗂Categorías"),
        KeyboardButton("📞Contactos")
    )
    return markup

# Comandos iniciales
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.send_message(
        message.chat.id,
        "🛍️ *Bienvenido a nuestra tienda* 🛍️\n\n"
        "Selecciona una opción del menú:",
        reply_markup=menu_principal(),
        parse_mode="Markdown"
    )

# Manejar botones principales
@bot.message_handler(func=lambda m: m.text in ["📦Productos", "🗂Categorías", "📞Contactos"])
def handle_main_buttons(message):
    if message.text == "📦Productos":
        listar_todos_productos(message)
    elif message.text == "🗂Categorías":
        listar_categorias(message)
    elif message.text == "📞Contactos":
        enviar_contactos(message)

# Listar todos los productos
def listar_todos_productos(message):
    respuesta = "📦 *Todos nuestros productos:*\n\n"
    for producto, detalles in todos_productos.items():
        respuesta += f"🔹 *{producto}* - {detalles['descripcion']}\n"
        respuesta += "Precios: " + ", ".join([f"{k} (${v})" for k, v in detalles['precios'].items()]) + "\n\n"
    
    respuesta += "\nEscribe el nombre de un producto para más detalles."
    
    bot.send_message(
        message.chat.id,
        respuesta,
        parse_mode="Markdown",
        reply_markup=menu_principal()
    )
def listar_categorias(message):
    respuesta = "🗂 *Categorías disponibles:*\n\n"
    for categoria,productos in productos_db.items():
        respuesta += f"🔹 *{categoria.capitalize()}*:\n"
    bot.send_message ( message.chat.id, respuesta, parse_mode="Markdown", reply_markup=menu_principal() )
# Búsqueda por texto
@bot.message_handler(func=lambda m: True)
def handle_text_search(message):
    texto = message.text.lower()
    # Volver al menú principal
    if texto == "🔙 menú principal" or texto == "menu principal":
        send_welcome(message)
        return
    # Buscar producto por nombre
    resultados = []
    for producto, detalles in todos_productos.items():
        if texto in producto.lower():
            resultados.append((producto, detalles))
    
    if resultados:
        respuesta = f"🔍 *Resultados para '{texto}':*\n\n"
        for producto, detalles in resultados:
            respuesta += f"⭐ *{producto.capitalize()}* ({detalles['categoria'].capitalize()})\n"
            respuesta += f"{detalles['descripcion']}\n"
            respuesta += "💲 Precios:\n" + "\n".join([f"- {k}: ${v}" for k, v in detalles['precios'].items()]) + "\n\n"
        
        bot.send_message(
            message.chat.id,
            respuesta,
            parse_mode="Markdown",
            reply_markup=menu_principal()
        )
    else:
        bot.send_message(
            message.chat.id,
            f"No encontré productos con '{texto}'. Intenta con otro nombre o usa los botones del menú.",
            reply_markup=menu_principal()
        )

# Función de contactos
def enviar_contactos(message):
    contacto_msg = (
        "📞 *Contacta con nosotros:*\n\n"
        "📱 Teléfono: +1 234 567 890\n"
        "Horario: Lunes a Viernes - 9:00 a 18:00"
    )
    
    bot.send_message(
        message.chat.id,
        contacto_msg,
        parse_mode="Markdown",
        reply_markup=menu_principal()
    )

# Iniciar el bot
print("Bot de ventas iniciado y listo...")
for item in productos_db.values():
    for keys,producto in item.items():
        print(f"el producto es {keys} \n y tiene : {producto['precios']} \n")
bot.polling()
