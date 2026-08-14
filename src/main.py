import os
from dotenv import load_dotenv

def print_author():
    load_dotenv()  # Загружаем переменные из .env
    author = os.getenv('AUTHOR')  # Читаем переменную AUTHOR
    print(f"Автор проекта: {author}")  # Печатаем имя автора

# Вызываем функцию — программа заканчивается принтом
print_author()   
