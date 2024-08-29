import flet as ft

def main(page: ft.Page):
    # Setting up the page
    page.title = "Beer Listing"
    page.bgcolor = ft.colors.BLACK
    page.padding = ft.padding.all(20)
    
    # Filters Sidebar
    filters = ft.Container(
        content=ft.Column(
            [
                ft.Text("Filters", color=ft.colors.WHITE),
                ft.ElevatedButton("Filter 1", on_click=lambda e: print("Filter 1 clicked")),
                ft.ElevatedButton("Filter 2", on_click=lambda e: print("Filter 2 clicked")),
                ft.ElevatedButton("Filter 3", on_click=lambda e: print("Filter 3 clicked")),
            ],
            spacing=20,
        ),
        bgcolor=ft.colors.GREY,
        width=150,
        padding=20,
    )

    # Beer Listing Grid
    beer_grid = ft.GridView(
        expand=True,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10,
        controls=[
            ft.Container(
                content=ft.Image(src="beer_image.png", fit=ft.ImageFit.CONTAIN),
                bgcolor=ft.colors.WHITE,
                padding=20,
                border_radius=10,
            ) for _ in range(6)  # Example grid with 6 items
        ]
    )

    # Beer Detail Section
    beer_detail = ft.Container(
        content=ft.Column(
            [
                ft.Text("Beer Name", color=ft.colors.WHITE, style="headlineMedium"),
                ft.Container(
                    content=ft.Image(src="beer_image.png", fit=ft.ImageFit.CONTAIN),
                    bgcolor=ft.colors.GREY,
                    padding=20,
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                ft.Text("Beer Info:", color=ft.colors.WHITE, style="bodyMedium"),
                ft.Text("• Detail 1", color=ft.colors.WHITE),
                ft.Text("• Detail 2", color=ft.colors.WHITE),
                ft.Text("• Detail 3", color=ft.colors.WHITE),
            ],
            spacing=10,
        ),
        bgcolor=ft.colors.GREY,
        padding=20,
        width=300,
    )

    # Page Layout
    page.add(
        ft.Row(
            [
                filters,
                ft.VerticalDivider(color=ft.colors.GREY),
                ft.Column(
                    [
                        ft.Container(content=beer_grid, expand=True),
                        beer_detail,
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

# Running the app
ft.app(main)

