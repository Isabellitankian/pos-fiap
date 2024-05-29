from unidecode import unidecode

def limpar_texto(texto):
    """ Remove acentos e caracteres especiais 
     Transforma a string em letras maiúsculas."""
    
    texto_sem_acento = unidecode(texto)

    texto_maiusculo = texto_sem_acento.upper()

    return texto_maiusculo