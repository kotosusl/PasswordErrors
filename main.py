class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


def check_len(password):
    try:
        if len(password) < 9:
            raise LengthError()
    except LengthError:
        return 1
    else:
        return 0


def check_letter(password):
    try:
        if password.lower() == password or password.upper() == password:
            raise LetterError()
    except LetterError:
        return 1
    else:
        return 0


def check_digit(password):
    nums = '1234567890'
    try:
        if not any([p in password for p in nums]):
            raise DigitError()
    except DigitError:
        return 1
    else:
        return 0


def check_seq(password):
    literals = 'qwertyuiop asdfghjkl zxcvbnm йцукенгшщзхъ фывапролджэ ячсмитьбю хъё жэё'
    try:
        if any([literals[p - 2:p + 1] in password.lower() for p in range(2, len(literals))]):
            raise SequenceError()
    except SequenceError:
        return 1
    else:
        return 0


def check_words(password):
    try:
        if password in open('top-9999-words.txt', encoding='utf=8').read().split('\n'):
            raise WordError()
    except WordError:
        return 1
    else:
        return 0


def check_password(password):
    global lengtherror, lettererror, digiterror, worderror, sequenceerror
    lettererror += check_letter(password)
    lengtherror += check_len(password)
    digiterror += check_digit(password)
    sequenceerror += check_seq(password)
    worderror += check_words(password)


file = open('top 10000 passwd.txt', encoding='utf-8').read()
lettererror = 0
lengtherror = 0
digiterror = 0
sequenceerror = 0
worderror = 0
for i in file.split('\n'):
    check_password(i)
print(f'DigitError - {digiterror}')
print(f'LengthError - {lengtherror}')
print(f'LetterError - {lettererror}')
print(f'SequenceError - {sequenceerror}')
print(f'WordError - {worderror}')

