{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "719c2411-dca9-4003-97a4-fd011ea1b56e",
   "metadata": {},
   "source": [
    "# Desafio 4 - Validação de Parênteses\n",
    "\n",
    "Dada uma string contendo apenas os caracteres ( , ) , { , } , ] e [ , determine se a string é válida. Uma string é válida se:\n",
    "\n",
    "Os parênteses abertos são fechados pelo mesmo tipo de parênteses.\n",
    "Os parênteses abertos são fechados na ordem correta.\n",
    "Exemplos:\n",
    "\n",
    "{[()]} ✅ Válido\n",
    "\n",
    "{[(])} ❌ Inválido (ordem errada)\n",
    "\n",
    "{{[[(]]}} ❌ Inválido (falta fechar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00284191-317c-423c-8904-98be4ec9bb0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "    #pode-se notar que entre dois caracteris tem que ter um número par de caracteris, para garantir a ordem correta\n",
    "    # notei isso observando um certo número de possibilidades, ou seja é uma conjectura interessante"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "212ea1cd-a8ad-49ca-a450-eee2fe5723b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#solução\n",
    "def VerificaValidade(texto):\n",
    "    # primeiro fazer uma verificação simples, se o número de caracteris for impar então a string está errada, pois todos estão em pares\n",
    "    if len(texto)%2!=0:\n",
    "        print(\"Inválido (excesso de caracteres)\")\n",
    "        return False\n",
    "    # disto verificar a ordem está certa, primeiro criar uma lista de caracteris e coloca-los separados lá\n",
    "    parceiros ={\")\": \"(\", \"}\": \"{\", \"]\":\"[\"}\n",
    "    partes = []\n",
    "    \n",
    "    #usar o for para acessar os caracteris da minha variável e verificar se esse caracter está no dicionário 'parceiros'\n",
    "    for c in texto:\n",
    "        #print(\"testando\", c) verificar o fluxo do programa\n",
    "        if c in parceiros:\n",
    "            #print(parceiros[c])verificar o fluxo do programa\n",
    "            #print(partes)verificar o fluxo do programa\n",
    "            #remover os parenteses de abertura que foram adicionados e verificar o programa\n",
    "            if not partes or partes.pop() != parceiros[c]:\n",
    "                return False\n",
    "        else:\n",
    "            # adicionar os parenteses de abertura\n",
    "            partes.append(c)\n",
    "        \n",
    "        # se o conjunto partes estiver vazio ele retorna 0, o que é false, disto é só negar o 0 que vira 1, que é verdadeiro em logica booleana           \n",
    "    return not partes\n",
    "    print(partes)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2068e809-11a8-47f9-af16-1ec06862a69d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#teste de execução\n",
    "test = \"{[()]}\"\n",
    "print(VerificaValidade(test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ac285d4-0849-46d8-b090-0e265489c13f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8274c979-8104-4111-8402-e2413795b30f",
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
