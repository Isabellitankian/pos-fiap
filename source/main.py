from utils.function import limpar_texto

texto = """era uma vez uma menina chamada chapeuzinho vermelho. ela vivia com sua mãe em uma pequena aldeia perto da floresta. um dia, sua mãe pediu que ela 
levasse uma cesta de guloseimas para a vovó, que morava do outro lado da floresta. antes de sair, a mãe avisou: "não fale com estranhos e siga pelo caminho mais curto".

no meio do caminho, chapeuzinho encontrou um lobo. ele parecia amigável e perguntou para onde ela estava indo. ingenuamente, chapeuzinho contou sobre a visita à vovó. 
o lobo, esperto, sugeriu um caminho mais longo e floreado, dizendo que era mais bonito. enquanto chapeuzinho se distraía colhendo flores, o lobo correu para a casa da vovó,
 fingiu ser ela e a trancou no armário.

quando chapeuzinho chegou, notou algo estranho na vovó. "vovó, que olhos grandes você tem!" "são para te ver melhor", respondeu o lobo. "e que orelhas grandes!" 
"são para te ouvir melhor." "e que dentes grandes!" "são para te comer melhor!", disse o lobo, pulando da cama. chapeuzinho gritou, mas um lenhador que passava ouviu 
e correu para ajudar. ele espantou o lobo e resgatou a vovó. desde então, chapeuzinho prometeu nunca mais desobedecer sua mãe."""

#aplicando o método criado para formatação do texto

texto_processado = limpar_texto(texto)

print("TEXTO ORIGINAL: \n\n", texto, "\n")
print("TEXTO PROCESSADO: \n\n", texto_processado)