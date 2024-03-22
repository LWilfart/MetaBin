# Ouvrir le fichier en mode lecture
with open('03_nt', 'r') as f:
    lines = f.readlines()

# Initialiser une liste pour stocker les lignes à extraire
extracted_lines = []

# Indicateur pour savoir si nous sommes dans une section d'intérêt
inside_section = False

# Parcourir les lignes du fichier
for line in lines:
    line = line.strip()
    
    if line.startswith("Sequences producing significant alignments:"):
        inside_section = True
    elif inside_section and line:
        extracted_lines.append(line)
        inside_section = False

# Écrire les lignes extraites dans un nouveau fichier
with open('a_nt.txt', 'w') as new_file:
    for line in extracted_lines:
        new_file.write(line + '\n')
