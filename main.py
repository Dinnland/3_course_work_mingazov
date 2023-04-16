# Основной файл

from utils import *

def main():
    path = 'operations.json'
    # questions = load_data_from_file(path)
    # e = load_data_from_file(path)
    f = razdel_po_oper_json(path)
    return f

a = main()
# print(f"{a}\n")
print(a)
if __name__ == "__main__":
    main()
