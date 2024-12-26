"""
ПЛАН УРОКА №2: Расширенные возможности Flet GUI
Продолжительность: 30 минут

ТЕМА: Работа с контейнерами и расположением элементов

1. ТЕОРИЯ (10 минут)
   - Container и его возможности
   - Row и Column для компоновки
   - Выравнивание и отступы
   - Размеры и ограничения

2. ПРАКТИКА (15 минут)
   - Создание карточки товара:
     * Container как основа
     * Row и Column для структуры
     * Изображение и текст
     * Стилизация и отступы
   - Обработка нажатий на карточку
   - Анимация при наведении

3. ЗАКРЕПЛЕНИЕ (5 минут)
   - Модификация карточки
   - Добавление новых элементов
   - Настройка внешнего вида

ДОМАШНЕЕ ЗАДАНИЕ:
1. Создать список карточек товаров
2. Добавить поиск по названию
3. Реализовать фильтрацию по цене

ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ:
- Python 3.7+
- flet>=0.9.0
- Изображения для карточек

РЕЗУЛЬТАТ УРОКА:
- Понимание работы с контейнерами
- Умение создавать сложные компоновки
- Навыки стилизации элементов
"""

import flet as ft


def main(page: ft.Page):
    # Заголовок окна
    page.title = "Примеры контейнеров"

    # Базовый контейнер с цветом фона и отступами
    basic_container = ft.Container(
        content=ft.Text("Базовый контейнер"),
        bgcolor="#f0f0f0",
        padding=10,
    )

    # Контейнер с границами, рамкой и скругелниями
    bordered_container = ft.Container(
        content=ft.Text("Контейнер с границами"),
        border=ft.border.all(2, "black"),
        border_radius=10,
        padding=10,
    )

    # Контейнер с тенью и градиентом
    gradient_container = ft.Container(
        content=ft.Text("Стилизованный контейнер", color="white"),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,  # Начальная точка градиента
            end=ft.alignment.bottom_right,  #  Конечная точка градиента
            colors=["#ff0000", "#0000ff"],  # Цвета градиента от и до
        ),
        padding=30,
        margin=10,
    )

    # Интерактивный контейнер
    interactive_container = ft.Container(
        content=ft.Text("Наведи на меня"),
        bgcolor="green",
        padding=20,
        border_radius=10,
        tooltip="Это интерактивный контейнер",
        animate=ft.animation.Animation(300, "easeOut"),
        on_hover=lambda e: print("Контейнер наведен"),
        on_click=lambda e: print("Контейнер нажат"),

    )

    page.add(basic_container, bordered_container, gradient_container, interactive_container)


# if __name__ == "__main__":
#     ft.app(target=main)

import flet as ft

class ContainerExamples(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.basic_container = ft.Container(
            content=ft.Text("Простой контейнер"),
            bgcolor="blue",
            padding=10,
        )

        self.bordered_container = ft.Container(
            content=ft.Text("Контейнер с границами"),
            border=ft.border.all(2, "red"),
            border_radius=10,
            padding=20,
        )

        self.gradient_container = ft.Container(
            content=ft.Text("Стильный контейнер", color="white"),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["blue", "red"]
            ),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLUE_GREY_300,
            ),
            padding=30,
            margin=10,
        )

        self.interactive_container = ft.Container(
            content=ft.Text("Наведи на меня"),
            bgcolor="green",
            padding=20,
            border_radius=5,
            on_click=lambda e: print("Клик!"),
            on_hover=lambda e: print("Наведение!"),
            tooltip="Это подсказка!",
        )

    def build(self):
        return ft.Column(controls=[
            self.basic_container,
            self.bordered_container,
            self.gradient_container,
            self.interactive_container
        ])

def main(page: ft.Page):
    page.title = "Примеры контейнеров (ООП)"
    container_examples = ContainerExamples()
    page.add(container_examples)

ft.app(target=main)
