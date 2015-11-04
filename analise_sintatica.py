global indice = 0
tabela_de_simbolos = [(),(),()]

def analise_sintatica():
	verificar_producao_programa()

def verificar_producao_PROGRAMA():
	pegar_token("program")
	verificar_producao_NOME()
	pegar_token(";")
	verificar_producao_DECL_VAR()
	verificar_producao_DECL_FUNCOES()
	verificar_producao_BLOCO()

def verificar_producao_DECL_VAR():
	pegar_token("var")
	pegar_producao_VARIAVEIS()

def verificar_producao_NOME():
	#aqui tem que existir um if
	 verificar_producao_CHAR()
	 verificar_producao_NOME()

def pegar_token(termo):
	tupla_selecionada = tabela_de_simbolos[indice]
	indice = indice+1;
	if not (termo == tupla_selecionada[1])
		print "Erro"



analise_sintatica()