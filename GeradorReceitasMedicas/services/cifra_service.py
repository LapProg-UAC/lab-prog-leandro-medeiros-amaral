def _processar_caractere(letra: str, deslocamento_atual: int, modo: str) -> str:
    """Processa um caractere individual aplicando o deslocamento da cifra de César.

    Args:
        letra: O caractere a ser processado.
        deslocamento_atual: O deslocamento atual a aplicar.
        modo: 'criptografar' para cifrar ou 'descriptografar' para decifrar.

    Returns:
        O caractere processado.
    """
    if letra.isalpha():
        pos = ord(letra.lower()) - ord('a')
        nova_pos = (pos + deslocamento_atual) % 26 if modo == 'criptografar' else (pos - deslocamento_atual) % 26
        base = 'A' if letra.isupper() else 'a'
        return chr(nova_pos + ord(base))
    elif letra.isdigit():
        num = int(letra)
        novo_num = (num + deslocamento_atual) % 10 if modo == 'criptografar' else (num - deslocamento_atual) % 10
        return str(novo_num)
    return letra


def cifrar(texto: str, deslocamento: int | list[int] | tuple[int, ...], modo: str = 'criptografar') -> str:
    """Aplica a cifra de César a um texto.

    Args:
        texto: O texto a ser cifrado ou decifrado.
        deslocamento: Deslocamento único ou lista de deslocamentos.
        modo: 'criptografar' ou 'descriptografar'.

    Returns:
        O texto processado.
    """
    resultado = ""
    indice_letra = 0
    eh_array = isinstance(deslocamento, (list, tuple))

    for letra in texto:
        des_atual = deslocamento[indice_letra % len(deslocamento)] if eh_array else deslocamento
        resultado += _processar_caractere(letra, des_atual, modo)
        
        if letra.isalpha() or letra.isdigit():
            indice_letra += 1

    return resultado
