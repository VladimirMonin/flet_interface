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



    page.add(basic_container, bordered_container)


if __name__ == "__main__":
    ft.app(target=main)
