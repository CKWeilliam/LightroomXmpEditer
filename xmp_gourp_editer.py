import os
import xml.etree.ElementTree as ET


def update_xmp_text(file_path, new_text):
    with open(file_path, 'r') as xmp_file:
        xmp_content = xmp_file.read()

    # Find the "Group" element and update its text
    root = ET.fromstring(xmp_content)
    group_element = root.find(
        ".//crs:Group", namespaces={"crs": "http://ns.adobe.com/camera-raw-settings/1.0/"})

    for rdf_li in group_element.findall(".//rdf:li", namespaces={"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}):
        rdf_li.text = new_text

    modified_xmp_content = ET.tostring(root, encoding="utf-8").decode()
    # Save the modified XMP file
    with open(file_path, 'w') as xmp_file:
        xmp_file.write(modified_xmp_content)


def process_xmp_files_in_folder(folder_path, new_text):
    # List all files in the folder and process each XMP file
    for filename in os.listdir(folder_path):
        if filename.endswith(".xmp"):
            file_path = os.path.join(folder_path, filename)
            update_xmp_text(file_path, new_text)


folder_path = "./xmp_file_to_edit"
# Input the new group text
new_text = "WP Winter Light Presets"
process_xmp_files_in_folder(folder_path, new_text)
