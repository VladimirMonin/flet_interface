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

def main(page: ft.Page):
    # Заголовок окна
    page.title = "Первое приложение на Flet"

    # Установка размера окна (актуальный синтаксис)
    page.window.width = 800
    page.window.height = 600

    # Создание и добавление элементов
    text = ft.Text(value="Привет, Flet!")
    button = ft.Button(text="Нажми меня")
    
    # Создание колонки с элементами
    content = ft.Column(controls=[text, button])
    
    # Добавление колонки на страницу
    page.add(content)

if __name__ == "__main__":
    ft.app(target=main)