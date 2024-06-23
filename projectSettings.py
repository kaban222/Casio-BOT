tok = "7144486478:AAGORaUAJlD_xcNoz29xsy9O99OZ3gWwBJU"
#tok = "6729627691:AAEmf-478dgb44IqDM3EsEtN3A_yTk9ZK6A"
id_vladelec = "870264076" #ваш id, можно получить в любом подходяящем боте. напрмер бот - get my id
Logs = "-4181636704"
kurs = 2000
limit = 500000
host = False
def get_combo_text(dice_value: int):
    """
    Возвращает то, что было на конкретном дайсе-казино
    :param dice_value: значение дайса (число)
    :return: массив строк, содержащий все выпавшие элементы в виде текста

    Альтернативный вариант (ещё раз спасибо t.me/svinerus):
        return [casino[(dice_value - 1) // i % 4]for i in (1, 4, 16)]
    """
    #           0       1         2        3
    values = ["BAR", "виноград", "лимон", "семь"]

    dice_value -= 1
    result = []
    for _ in range(3):
        result.append(values[dice_value % 4])
        dice_value //= 4
    return result
