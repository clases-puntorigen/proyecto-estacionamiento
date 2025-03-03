from nicegui_router import page, ui, component, use_state

from nicegui_router import page, ui

@page("/")
async def home():
    ui.label("Página principal")
    ui.button("Ir al admin", on_click=lambda: ui.navigate("/admin/index"))


def formulario(on_submit):
    def on_login():
        if username.value and password.value:
            on_submit({"username": username.value, "password": password.value})

    with ui.card(align_items="center").classes(
        "absolute-center w-[300px] ma-0 z-10"
    ).style(
        "background-color: #FFF; padding:0 0 0 0;"
    ):

        with ui.card_section().classes("w-full pa-0").style("background-color: #000; margin: 0;"):            
            ui.label("Acceso Restringido").classes("text-h6 q-mb-xs text-center text-white")
            
        with ui.card_section().classes("w-full").style("background-color: #FFF; padding-top: 20px; padding-bottom: 20px;"):
            username = ui.input("Usuario")
            password = ui.input(
                "Contraseña", password=True, password_toggle_button=True
            ).on("keydown.enter", on_login)
            with ui.card_actions().style("background-color: #fff; padding-bottom: 10px;"):
                ui.button("Ingresar", on_click=on_login).props("flat") 

@page
async def login():
    with ui.column():
        with ui.image('https://hips.hearstapps.com/hmg-prod/images/07-ss300p-ehra-lessien-1567611990-1-1567790807.jpg').classes("absolute-full object-cover z-0"):
            pass
        formulario(lambda datos: ui.notify(f"Usuario: {datos['username']}, Contraseña: {datos['password']}"))

ui.run()
