import random

flashcards = {
    "Python": "A popular programming language",
    "OpenAI": "An artificial intelligence research laboratory",
    "GitHub": "A web-based platform for version control and collaboration",
    "HTML": "Hypertext Markup Language used for creating web pages",
    "CSS": "Cascading Style Sheets used for styling web pages",
    "JavaScript": "A programming language used for web development",
    "API": "Application Programming Interface",
    "JSON": "JavaScript Object Notation used for data interchange",
    "SQL": "Structured Query Language used for managing databases",
    "IDE": "Integrated Development Environment"
}

# Obtén una lista de las claves (palabras) de las flashcards
flashcard_keys = list(flashcards.keys())

# Mezcla las claves de forma aleatoria
random.shuffle(flashcard_keys)

# Recorre las claves y muestra las flashcards
for key in flashcard_keys:
    print("Flashcard:")
    print(key)
    input("Presiona Enter para ver la respuesta")
    print("Respuesta:")
    print(flashcards[key])
    print("------------------------")

print("Has completado todas las flashcards")
