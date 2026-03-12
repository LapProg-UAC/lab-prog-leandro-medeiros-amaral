def _processar_caractere(letra, des_atual, modo):
    """
    Processa um caractere individual aplicando o deslocamento da cifra de César.

    Parâmetros
    ----------
    letra : str
        O caractere a ser processado.
    des_atual : int
        O deslocamento atual a aplicar.
    modo : str
        'criptografar' para cifrar ou 'descriptografar' para decifrar.

    Retorno
    -------
    str
        O caractere processado.
    """
    if letra.isalpha():
        pos = ord(letra.lower()) - ord('a')
        nova_pos = (pos + des_atual) % 26 if modo == 'criptografar' else (pos - des_atual) % 26
        base = 'A' if letra.isupper() else 'a'
        return chr(nova_pos + ord(base))
    elif letra.isdigit():
        num = int(letra)
        novo_num = (num + des_atual) % 10 if modo == 'criptografar' else (num - des_atual) % 10
        return str(novo_num)
    return letra


def cifra_de_cesar(texto, deslocamento, modo='criptografar'):
    """
    Aplica a cifra de César a um texto, suportando deslocamentos únicos ou em array.

    Parâmetros
    ----------
    texto : str
        O texto a ser cifrado ou decifrado.
    deslocamento : int or list or tuple
        Deslocamento único (int) ou lista de deslocamentos para cada caractere alfanumérico.
    modo : str, opcional
        'criptografar' para cifrar (padrão) ou 'descriptografar' para decifrar.

    Retorno
    -------
    str
        O texto processado.
    """
    resultado = ""
    indice_letra = 0
    
    # Verifica se deslocamento é uma lista/array
    eh_array = isinstance(deslocamento, (list, tuple))

    for letra in texto:
        # Se deslocamento for array, usa o próximo elemento ciclando
        des_atual = deslocamento[indice_letra % len(deslocamento)] if eh_array else deslocamento
        
        caractere_processado = _processar_caractere(letra, des_atual, modo)
        resultado += caractere_processado
        
        if letra.isalpha() or letra.isdigit():
            indice_letra += 1

    return resultado

    
# Exemplo de uso
texto_original = "Ola, Mundo! 123"

# Com deslocamento único
deslocamento = 2
print("Com deslocamento único (3):")
print(cifra_de_cesar(texto_original, deslocamento, 'criptografar'))
print(cifra_de_cesar(cifra_de_cesar(texto_original, deslocamento, 'criptografar'), deslocamento, 'descriptografar'))

# Com deslocamento como array
deslocamento_array = [1, 2, 3, 5]
print("\nCom deslocamento como array [1, 2]:")
criptografado = cifra_de_cesar(texto_original, deslocamento_array, 'criptografar')
print(criptografado)
print(cifra_de_cesar(criptografado, deslocamento_array, 'descriptografar'))
