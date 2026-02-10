{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "719c2411-dca9-4003-97a4-fd011ea1b56e",
   "metadata": {},
   "source": [
    "# Desafio 2 - Verificador de Palíndromo\n",
    "Crie uma função que receba uma palavra (string) e retorne \"true\" se ela for um palíndromo e \"false\" caso contrário.\n",
    "\n",
    "Definição: Palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.\n",
    "\n",
    "Exemplos: \"arara\" (true), \"ovo\" (true), \"casa\" (false)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ff3df503-31b6-4e43-975f-c67653c77d24",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# solução\n",
    "def VerificaPalindromo(palavra):\n",
    "# primeiro usei uma função lower para transformar todas as letras em todas maiúsculas ou todas minúsculas.\n",
    "    palavra = palavra.lower()\n",
    "# depois minha ideia é verificar a quantidade de letras da palavra usando a função \"len\" do próprio Python, \n",
    "# lembrando que é uma str e no python o indice da str começa no zero.\n",
    "# exemplo: ovo tem três letras, disto O está no indice 0, V está no indice 1 e O está no 2.\n",
    "    cont = len(palavra) ; num = 0\n",
    "# usando o while para percorrer str e assim verificar se é um palindromo, ou seja, verificar se a primeira letra é igual a última \n",
    "    while (cont != 0):\n",
    "        \n",
    "        #print (cont-1, num)\n",
    "        #print (palavra[num], palavra[cont-1]), usei os prints para verificar o fluxo do programa\n",
    "        if palavra[num] != palavra[cont-1]:\n",
    "            return False \n",
    "        # para ele percorrer toda palavra e não ficar um loop errado é necessário modificar as variáveis num e cont\n",
    "        num = num+1\n",
    "        cont = cont-1\n",
    "    return True\n",
    "# no caso não seria necessário verificar todas as letras como fiz pode-se fazer só até a metade das letras, se for par, ou metade mais um se for impar\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "212ea1cd-a8ad-49ca-a450-eee2fe5723b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#testando o programa\n",
    "text = input (\"Digite uma palavra: \")\n",
    "print(VerificaPalindromo(text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2068e809-11a8-47f9-af16-1ec06862a69d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ac285d4-0849-46d8-b090-0e265489c13f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
