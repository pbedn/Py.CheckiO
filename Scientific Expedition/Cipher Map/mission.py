def recall_password(cipher_grille, ciphered_password):
    def get_string(grille, password):
        return "".join(password[i][j] for i in range(4) for j in range(4) if grille[i][j] == 'X')

    def reverse_grille(grille):
        return tuple("".join(grille[j][i] for j in reversed(range(4))) for i in range(4))

    s = get_string(cipher_grille, ciphered_password)
    new_grille = reverse_grille(cipher_grille)

    for _ in range(3):
        s += get_string(new_grille, ciphered_password)
        new_grille = reverse_grille(new_grille)
    return s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
