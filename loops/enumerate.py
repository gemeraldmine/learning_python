languages = ["Spanish", "English", "Russian", "Chinese"]

# 2 starts enum at 2 instead of 0
for index, language in enumerate(languages, 2):
    print(f"Index {index} and language {language}")
