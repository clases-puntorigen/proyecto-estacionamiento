from nicegui import ui

def mostrar_index():
    with ui.column():
        ui.label("Bienvenido al panel de administración de reservas")
        ui.button("Gestionar Estacionamientos", on_click=lambda: ui.notify('Función pendiente de implementación'))
        ui.button("Ver Reservas", on_click=lambda: ui.notify('Función pendiente de implementación'))
        ui.button("Gestionar Pagos", on_click=lambda: ui.notify('Función pendiente de implementación'))

mostrar_index()

#iniciar ui

ui.run()