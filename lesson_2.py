import flet as ft
from flet import Icons

def main(page: ft.Page):
    page.title = "Примеры компоновки"
    page.padding = 20  # Отступы страницы

    # Горизонтальный ряд с выравниванием по центру
    header = ft.Row(
        controls=[
            ft.Icon(Icons.SHOPPING_CART, size=30, color="blue"),
            ft.Text("Магазин", size=20, weight="bold"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Вертикальная колонка с карточками товаров
    products = ft.Column(
        controls=[
            # Карточка товара 1
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(Icons.LAPTOP, size=40),
                        ft.Column(
                            controls=[
                                ft.Text("Ноутбук", size=16, weight="bold"),
                                ft.Text("100 000 руб.", color="green"),
                            ],
                            spacing=5,
                        )
                    ],
                    spacing=20,
                ),
                padding=10,
                border=ft.border.all(1, "grey"),
                border_radius=10,
            ),
            
            # Карточка товара 2
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(Icons.PHONE_ANDROID, size=40),
                        ft.Column(
                            controls=[
                                ft.Text("Смартфон", size=16, weight="bold"),
                                ft.Text("50 000 руб.", color="green"),
                            ],
                            spacing=5,
                        )
                    ],
                    spacing=20,
                ),
                padding=10,
                border=ft.border.all(1, "grey"),
                border_radius=10,
            ),
        ],
        spacing=10,  # Отступ между карточками
        width=400,   # Фиксированная ширина колонки
    )

    # Нижняя панель с кнопками
    footer = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="В корзину",
                icon=Icons.ADD_SHOPPING_CART,
            ),
            ft.ElevatedButton(
                text="Оформить",
                icon=Icons.PAYMENT,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Кнопки по краям
        width=400,  # Такая же ширина как у колонки
    )

    # Добавляем все элементы на страницу
    page.add(
        header,
        ft.Divider(),  # Разделительная линия
        products,
        ft.Divider(),
        footer,
    )

ft.app(target=main)
