# testa uma palavra introduzida pelo utilizador
# Se for "Spathiphyllum" escreve "Yes - Spathiphyllum is the best plant ever!"
# Senão se for "spathiphyllum" escreve "No, I want a big Spathiphyllum!"
# Senão escreve "Spathiphyllum! Not [input]!", sendo [input] a string introduzida

nome = input("Introduza um nome de flor: ")

if nome == "Spathiphyllum": print("Yes - Spathiphyllum is the best plant ever!")
elif nome == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", nome, "!", sep="") # print("Spathiphyllum! Not", nome+'!' )
