import xml.etree.ElementTree as ET

def clean_tree(element):
    # Supprime le namespace des balises
    if '}' in element.tag:
        element.tag = element.tag.split('}', 1)[1]

    # Supprime le texte
    element.text = None
    element.tail = None

    # Traite les enfants
    for child in element:
        clean_tree(child)

tree = ET.parse("Pellican_1-Tim_TOC.xml")
root = tree.getroot()

clean_tree(root)

tree.write("structure.xml", encoding="utf-8", xml_declaration=True)