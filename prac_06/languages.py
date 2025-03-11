from programming_language import ProgrammingLanguage

def main():
    """Test code to show how to use ProgrammingLanguage."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    programming_languages = [python,ruby,visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)

main()