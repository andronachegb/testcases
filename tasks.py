import pc

pc1 = pc.pc("PC1")
print(f"Status of {pc1.name} is {pc1.status}")

pc1.power_on()
print(f"Status of {pc1.name} is {pc1.status}")