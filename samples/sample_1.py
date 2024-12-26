import flet as ft

import flet as ft
import time


def main(page: ft.Page):
    page.title = "Поисковое приложение"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 50

    # Создаем текстовое поле для поиска
    search_field = ft.TextField(
        label="Поиск",
        width=400,
        border_radius=10,
        prefix_icon=ft.icons.SEARCH,
    )

    # Текст, который будет появляться под формой
    result_text = ft.Text(
        value="", size=16, color=ft.colors.GREY_700, text_align=ft.TextAlign.CENTER
    )

    def search_click(e):
        # Меняем цвет кнопки
        search_button.bgcolor = ft.colors.GREEN
        search_button.update()

        # Показываем текст
        result_text.value = f"Вы искали: {search_field.value}"
        result_text.update()

        # Через секунду возвращаем исходный цвет
        time.sleep(1)
        search_button.bgcolor = ft.colors.BLUE
        search_button.update()

    def clear_click(e):
        search_field.value = ""
        result_text.value = ""
        page.update()

    # Кнопка поиска
    search_button = ft.ElevatedButton(
        "Поиск",
        icon=ft.icons.SEARCH,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=search_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Кнопка очистки
    clear_button = ft.ElevatedButton(
        "Очистить",
        icon=ft.icons.CLEAR,
        bgcolor=ft.colors.RED_400,
        color=ft.colors.WHITE,
        on_click=clear_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Создаем контейнер с отступами для кнопок
    buttons_row = ft.Row(
        controls=[search_button, clear_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # Добавляем все элементы на страницу в колонку
    page.add(
        ft.Column(
            controls=[search_field, buttons_row, result_text],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main)
