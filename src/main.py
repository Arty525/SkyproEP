from src.masks import get_mask_account, get_mask_card_number

# Вывод функций
if __name__ == '__main__':
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("12345678901234567890"))
