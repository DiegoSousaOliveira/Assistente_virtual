import flet as ft
from assistantVt import VirtualAssistant

def main(page: ft.Page):
    page.title = 'Assistente Virtual'
    
    # settings of page
    page.bgcolor = ft.colors.WHITE

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ACCOUNT_CIRCLE),
        leading_width=50,
        title=ft.Text(
            "Maria ASV",
            expand=True,
            text_align=ft.TextAlign.CENTER),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Checked item", checked=False
                    ),
                ]
            ),
        ],
    )

    virtualAssistant = (VirtualAssistant(page=page))

    page.add(virtualAssistant)

    page.update()

    page.run_thread(virtualAssistant.main)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='./assets')