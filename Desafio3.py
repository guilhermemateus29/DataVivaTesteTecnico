{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "719c2411-dca9-4003-97a4-fd011ea1b56e",
   "metadata": {},
   "source": [
    "# Desafio 3 - Encontrar Duplicados\n",
    "Dada uma lista de números inteiros, escreva uma função que identifique e retorne o número que aparece repetido.\n",
    "\n",
    "Entrada: $[1, 2, 3, 4, 2, 5]$\n",
    "\n",
    "Saída Esperada: $2$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "ff3df503-31b6-4e43-975f-c67653c77d24",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# solução\n",
    "#defirnir a função e dar um nome para ela\n",
    "def VerificaRepeticao(lista):\n",
    "    #verificar o tamanho da lista que inserida como parametro\n",
    "    cont = len (lista)\n",
    "    #criei uma lista para colocar os valores que se repetiram, se for uma lista muito grande pode ter mais de um valor repetido\n",
    "    repetidos = []\n",
    "    #usei dois laços para percorrer e comparar os elementos da lista um a um\n",
    "    for i in range(cont):\n",
    "        for j in range(cont):\n",
    "        #print(lista[i],lista[j]), verificar o fluxo do programa\n",
    "        # fazer as verificações e comparação dos elementos, não é necessário comprar o elemento se i=j, pois estou comparando o elemento com ele mesmo\n",
    "            if (lista[i]==lista[j] ) and (i!=j):\n",
    "                repetidos.append(lista[i])\n",
    "    # é acrescentado na lista os elementos com a função append, mas as comparações podem ser feitas mais de uma vez dependendo da lista \n",
    "    # a função set retira as repetições e retorna um {} e depois uso a função list para retornar uma lista\n",
    "    # acho que seria possível resolver sem usar o set, mas teria que fazer outro \"for \"\n",
    "    repetidos = set(repetidos)\n",
    "    \n",
    "    return list (repetidos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "212ea1cd-a8ad-49ca-a450-eee2fe5723b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "#exemplo e este de lista complicada\n",
    "L = [11,1,2,3,4,5,6,7,8,9,0,5,6,5, 5,6,5,6,5,6,5,6,12,15,16,22,23,14,19,11]\n",
    "print(VerificaRepeticao(L))"
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
