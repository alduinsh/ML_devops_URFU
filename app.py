# ПРИЛОЖЕНИЕ ДЛЯ ГЕНЕРАЦИИ ТЕКСТА
from transformers import pipeline

generator = pipeline("text-generation")
generator("МЫ БУДЕМ РАБОТАТЬ С ГЕНЕАРОТОРОМ ЧИСЕЛ, ЦВЕТОМ АВТО И МАРКОЙ БЕТОНА")
print(generator)
