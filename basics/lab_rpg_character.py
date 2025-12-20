full_dot = "●"
empty_dot = "○"


def create_character(name, strn, intl, rizz):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if (
        not isinstance(strn, int)
        or not isinstance(intl, int)
        or not isinstance(rizz, int)
    ):
        return "All stats should be integers"
    if strn < 1 or intl < 1 or rizz < 1:
        return "All stats should be no less than 1"
    if strn > 4 or intl > 4 or rizz > 4:
        return "All stats should be no more than 4"
    if strn + intl + rizz != 7:
        return "The character should start with 7 points"
    str_val = full_dot * strn + empty_dot * 9
    int_val = full_dot * intl + empty_dot * 9
    cha_val = full_dot * rizz + empty_dot * 9
    character_sheet = (
        f"{name}\nSTR {str_val[:10]}\nINT {int_val[:10]}\nCHA {cha_val[:10]}"
    )
    return character_sheet


print(create_character("chuck", 1, 2, 4))
