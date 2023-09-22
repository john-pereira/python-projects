FILEPATH = r"files\todos.txt";

def get_todos(filepath=FILEPATH):
    """Read the txt file and return its content."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos_args, filepath=FILEPATH):
    """Write in the txt file from the user input."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)

# Este código será executado se o script for executado como programa principal
if __name__ == "__main__":
    # Coloque sua lógica principal do programa aqui
    print("Este script está sendo executado diretamente.")
    # Você pode chamar funções, definir variáveis e fazer outras coisas aqui.

# Este código não será executado se o script for importado como um módulo
