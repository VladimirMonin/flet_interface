"""
ПЛАН УРОКА №1: Введение в Flet GUI
Продолжительность: 30 минут

ТЕМА: Создание первого оконного приложения на Flet

1. ТЕОРИЯ (10 минут)
   - Что такое Flet и зачем он нужен
   - Отличия от других GUI фреймворков
   - Базовая архитектура приложения
   - Концепция функционального подхода

2. ПРАКТИКА (15 минут) 
   - Создание окна приложения
   - Базовые виджеты:
     * Text - текстовые элементы
     * Button - кнопки
     * Column - вертикальное расположение
   - Обработка событий кнопок
   - Обновление интерфейса

3. ЗАКРЕПЛЕНИЕ (5 минут)
   - Изменение параметров окна
   - Добавление новых элементов
   - Стилизация виджетов

ДОМАШНЕЕ ЗАДАНИЕ:
1. Создать счетчик кликов
2. Добавить кнопку сброса
3. Реализовать цветовое оформление

ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ:
- Python 3.7+
- flet>=0.9.0

РЕЗУЛЬТАТ УРОКА:
- Понимание основ Flet
- Умение создавать простое приложение
- Навыки обработки событий
"""

import flet as ft
from flet import Icons  # иконки

# Используем каталог https://fonts.google.com/icons
# Названия цветов https://colorscheme.ru/html-colors.html


def main(page: ft.Page):
    # Заголовок окна
    page.title = "События и обновления"

    # Установим цвет фона
    page.bgcolor = "#E0FFFF"

    # Создаем текст который будем менять
    message = ft.Text(value="Этот текст изменится...", color="black")

    # Обработчик события для кнопки
    def button_cliced(e):
        message.value = "Кнопка была нажата!"
        message.color = "red"
        button.icon = Icons.DONE_ALL  # делаем другую иконку на кнопке
        button.bgcolor = "#FFA500"  # изменим цвет фона
        page.update()  # Обновляем страницу

    # Создаем кнопку c обработчиком события
    button = ft.Button(
        text="Изменить текст",
        on_click=button_cliced,
        color="white",
        bgcolor="#4682B4",
        elevation=5,  # тень
        tooltip="Подсказка при наведении",  # подсказка при наведении
        icon=Icons.STAR,  # Новый способ
    )
    # Размещение элементов
    content = ft.Column(controls=[message, button])
    page.add(content)


if __name__ == "__main__":
    ft.app(target=main)
