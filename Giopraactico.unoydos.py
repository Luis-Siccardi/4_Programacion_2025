{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXCgf5WWQ0hvIXN1RMSQh+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Luis-Siccardi/4_Programacion_2025/blob/main/Giopraactico.unoydos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ew7LaseBjh8i",
        "outputId": "ab86d3f2-4dca-4114-9762-5acbd11708a0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "igrese sus numeros 2\n",
            "igrese sus numeros 3\n",
            "igrese sus numeros 4\n",
            "igrese sus numeros 5\n",
            "igrese sus numeros 6\n",
            "igrese sus numeros 6\n",
            "igrese sus numeros 6\n",
            "igrese sus numeros 5\n",
            "igrese sus numeros 4\n",
            "igrese sus numeros 3\n"
          ]
        }
      ],
      "source": [
        "\n",
        "numeros = []\n",
        "pares = []\n",
        "for i in range (10):\n",
        "    numUsuario=(int(input(\"igrese sus numeros \")))\n",
        "    numeros.append(numUsuario)\n",
        "    if numUsuario % 2 == 0:\n",
        "        pares.append(numUsuario)\n",
        "print(f\"los num pares son:{f}\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def contar_pronombres(texto):\n",
        "    pronombres = [\"él\", \"ella\", \"ellos\", \"ellas\", \"lo\", \"la\", \"los\", \"las\", \"usted\", \"nosotros\", \"nosotras\", ]\n",
        "    texto = texto.lower()  # eso se usa para que el texto seaa minuscula\n",
        "    contador = 0\n",
        "\n",
        "    # Contamos cuántas veces aparece cada pronombre en el texto\n",
        "    for pronombre in pronombres:\n",
        "        if pronombre in pronombres:  # Se sumar las veces que aparece el pronombre\n",
        "         contador += 1\n",
        "    return contador\n",
        "\n",
        "texto = \"\"\"Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba.\"\"\"\n",
        "\n",
        "#la cantidad de pronombres es igual a contar prononmbres obviamentwwe del texto\n",
        "cantidad_pronombres = contar_pronombres(texto)\n",
        "\n",
        "\n",
        "print(f\"El texto contiene {cantidad_pronombres} pronombres.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gEBTrN2Cm-7v",
        "outputId": "f59e1119-dbfa-474d-c0d1-ff48daca0ddc"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El texto contiene 11 pronombres.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "VU1MJUyPygN1",
        "outputId": "7828046a-d32a-4020-fc50-967d6a52fcb9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'str' object is not callable",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-50-1df8f7864d39>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'hol'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: 'str' object is not callable"
          ]
        }
      ]
    }
  ]
}