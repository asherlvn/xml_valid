#this project helps the team to get good xml and xsd files
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import lxml.etree as ET


def select_xml_file():
    xml_file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    xml_file_entry.delete(0, tk.END)
    xml_file_entry.insert(tk.END, xml_file_path)


def select_xsd_file():
    xsd_file_path = filedialog.askopenfilename(filetypes=[("XSD Files", "*.xsd")])
    xsd_file_entry.delete(0, tk.END)
    xsd_file_entry.insert(tk.END, xsd_file_path)


def validate_xml():
    xml_file = xml_file_entry.get()
    xsd_file = xsd_file_entry.get()

    if not xml_file or not xsd_file:
        messagebox.showwarning("Error", "Please select both XML and XSD files.")
        return

    try:
        xml_tree = ET.parse(xml_file)
        xsd_tree = ET.parse(xsd_file)
        xml_schema = ET.XMLSchema(xsd_tree)

        if xml_schema.validate(xml_tree):
            messagebox.showinfo("Validation Result", "XML file is valid against the XSD file.")
        else:
            messagebox.showwarning("Validation Result", "XML file is not valid against the XSD file.")
    except ET.XMLSyntaxError as e:
        messagebox.showerror("Error", f"XML parsing error:\n\n{str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")


# Create the GUI
root = tk.Tk()
root.title("XML Validation")
root.geometry("600x350") #big window

# XML File Label and Entry
xml_file_label = tk.Label(root, text="XML File:")
xml_file_label.pack()
xml_file_entry = tk.Entry(root, width=50)
xml_file_entry.pack()

# XML File Button
xml_file_button = tk.Button(root, text="Select XML File", command=select_xml_file)
xml_file_button.pack()

# XSD File Label and Entry
xsd_file_label = tk.Label(root, text="XSD File:")
xsd_file_label.pack()
xsd_file_entry = tk.Entry(root, width=50)
xsd_file_entry.pack()

# XSD File Button
xsd_file_button = tk.Button(root, text="Select XSD File", command=select_xsd_file)
xsd_file_button.pack()

# Validate Button
validate_button = tk.Button(root, text="Validate XML", command=validate_xml)
validate_button.pack()

# Run the GUI
root.mainloop()
