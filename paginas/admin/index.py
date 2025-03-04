from nicegui_router import ui

# Página principal
def home():
    ui.label("Página principal")
    ui.button("Ir al login", on_click=lambda: ui.navigate("/login"))

# Página de login
def login():
    ui.label("Formulario de Login")
    ui.button("Regresar a la página principal", on_click=lambda: ui.navigate("/"))

# Registro de rutas
ui.page("/", home)
ui.page("/login", login)

# Iniciar el servidor
ui.run()
