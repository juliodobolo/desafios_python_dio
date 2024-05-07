itens = []

for _ in range(3):
  novo_item = input()
  itens.append(novo_item)

print("Lista de Equipamentos:")
for item in itens:
    print(f"- {item}")
