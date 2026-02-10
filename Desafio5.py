{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "719c2411-dca9-4003-97a4-fd011ea1b56e",
   "metadata": {},
   "source": [
    "# Desafio 5 - Manipulação de Dados (Bônus)\n",
    "Este desafio simula um cenário comum no DataViva: agrupar dados para visualização. Dado um array de objetos representando transações:\n",
    "\n",
    "[\n",
    "  { \"categoria\": \"Alimentação\", \"valor\": 10 },\n",
    "  \n",
    "  { \"categoria\": \"Transporte\", \"valor\": 5 },\n",
    "  \n",
    "  { \"categoria\": \"Alimentação\", \"valor\": 20 },\n",
    "  \n",
    "  { \"categoria\": \"Lazer\", \"valor\": 50 }\n",
    "]\n",
    "\n",
    "Escreva uma função que retorne um objeto (ou dicionário) somando os valores por categoria.\n",
    "\n",
    "Saída Esperada:\n",
    "{\n",
    "  \"Alimentação\": 30,\n",
    "  \"Transporte\": 5,\n",
    "  \"Lazer\": 50\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "212ea1cd-a8ad-49ca-a450-eee2fe5723b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#solução\n",
    "def concatena (lista): \n",
    "    #defini um novo dicionário que será a saída do programa\n",
    "    NovaLista = {}\n",
    "    #usei a função \"len \" do python para verificar o tamanho da minha lista de dicionário\n",
    "    num=len(lista)\n",
    "    # os dicionários possuem uma \"keys\" e \"values\" que são associados as \"keys\"\n",
    "    # acessei vada elemento da lista com um 'for' para percorrer os seus elementos, os dicionários, e outro for para percorrer as informações do dicio\n",
    "    for i in range(num):\n",
    "        for val in lista[i].values():\n",
    "            # nessas condições eu verifico se aquele valor, está no dicio. Se não está no dicionário, adiciona e sim se já está só acrescento ao valor\n",
    "            if val not in NovaLista:\n",
    "                NovaLista[val]=lista[i][\"valor\"]\n",
    "                #print(lista[i][\"valor\"]) verificando o fluxo do programa\n",
    "            elif val in NovaLista:\n",
    "                NovaLista[val]+=lista[i][\"valor\"]\n",
    "                #print(lista[i][\"valor\"])\n",
    "            # como só tem dois valores o break saí do loop e não adiciona informação númerica, pode testar comentando ele para vocês verem a saída\n",
    "            break\n",
    "                \n",
    "    #observação, acredito que essa não é a melhor solução, talvez tenha uma melhor, mais elegante, prática entre outros, \n",
    "    return (NovaLista)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "2068e809-11a8-47f9-af16-1ec06862a69d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Alimentação': 38, 'Transporte': 92, 'Lazer': 36}\n"
     ]
    }
   ],
   "source": [
    "#teste de execução do programa com uma lista modificada\n",
    "dicio =[\n",
    "  { \"categoria\": \"Alimentação\", \"valor\": 13 },\n",
    "  \n",
    "  { \"categoria\": \"Transporte\", \"valor\": 87 },\n",
    "  \n",
    "  { \"categoria\": \"Alimentação\", \"valor\": 21 },\n",
    "  \n",
    "  { \"categoria\": \"Lazer\", \"valor\": 36 },\n",
    "\n",
    "    { \"categoria\": \"Alimentação\", \"valor\": 4 },\n",
    "    \n",
    "      { \"categoria\": \"Transporte\", \"valor\": 5 }\n",
    "    \n",
    "]\n",
    "print (concatena(dicio))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "0ac285d4-0849-46d8-b090-0e265489c13f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for j in range(len(NovaLista)):\n",
    "#            print(NovaLista[j][\"categoria\"], lista[i][\"categoria\"])\n",
    "#\n",
    "#            if NovaLista[j][\"categoria\"]!= lista[i][\"categoria\"] :\n",
    "#                NovaLista.append(lista[i])\n",
    "#            elif NovaLista[j][\"categoria\"]== lista[i][\"categoria\"] :\n",
    "#                NovaLista[j][\"valor\"]=  NovaLista[j][\"valor\"] + lista[i][\"valor\"]\n",
    "#            else: \n",
    "#                print (\"erro\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fb6c478-2850-482a-9606-54de9ba17172",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f8e30e7-bc42-479e-ae52-ce59269ab1d3",
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
