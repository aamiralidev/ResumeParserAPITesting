import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from APIs import affinda, apilayer, sovren, superparser, hirize, hrflow, edenai
from dotenv import load_dotenv
from Exporters.jsonexporter import JsonExporter

load_dotenv('.env')


RESUME_PATH = None
OUTPUT_PATH = None
SELECTED_APIS = []
APIS = {
    'Affinda': affinda.Affinda,
    'APILayer': apilayer.APILayer,
    'SuperParser': superparser.SuperParser,
    'HRFlow.ai': hrflow.Hrflow,
    'SOVREN': sovren.SOVREN,
    'Hirize': hirize.Hirize,
    'EdenAI': edenai.EdenAIResumeParser
}

# Function to generate the output JSON based on selected APIs
def generate_output():
    selected_apis = [api_name for api_name, var in zip(api_names, api_vars) if var.get() == 1]
    
    # Check if at least one API is selected
    if not selected_apis:
        messagebox.showerror("Error", "Please select at least one API.")
        return
    
    # Ask the user for the output folder
    output_folder = filedialog.askdirectory()
    
    # Check if an output folder is selected
    if not output_folder:
        return
    
    global RESUME_PATH
    global OUTPUT_PATH

    if not RESUME_PATH:
        messagebox.showerror("Error", "Please select resume first.")
        return
    
    OUTPUT_PATH = output_folder
    SELECTED_APIS = selected_apis
    for api in selected_apis:
        client = APIS[api]()
        JsonExporter.export(os.path.join(OUTPUT_PATH, f'{api}.json'), client.parse(RESUME_PATH))
    # Add your code here to process selected APIs and generate the output

# Function to open a file dialog for uploading a resume
def upload_resume():
    global RESUME_PATH
    filetypes = [
        ("PDF Files", "*.pdf"),
        ("Word Files", "*.docx *.doc")
    ]
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        RESUME_PATH = file_path
        # Check the file extension to ensure it's a PDF or Word file
        if file_path.lower().endswith(('.pdf', '.docx', '.doc')):
            filename = os.path.basename(file_path)
            resume_label.config(text=f"Uploaded Resume: {filename}")
        else:
            messagebox.showerror("Error", "Invalid file format. Please select a PDF or Word document.")


root = tk.Tk()
root.geometry("700x500")
root.minsize(700, 500)
root.maxsize(700, 500)
root.title('USE RESUME PARSING APIS')

frame1 = tk.Frame(root, relief='sunken')
frame1.pack(fill=tk.BOTH, pady=30)

frame2 = tk.Frame(root, relief='sunken')
frame2.pack(fill=tk.BOTH, pady=30)

label = tk.Label(frame2, text="Select the APIs, click the button to test them", font=('Georgia 8'))
label.pack(pady=10)

frame3 = tk.Frame(root, relief='sunken')
frame3.pack(fill=tk.BOTH, pady=10, padx=200)

# Create and place check buttons for API selection
api_vars = []
api_count = 0
api_names = APIS.keys()

for api_name in api_names:
    var = tk.IntVar()
    api_vars.append(var)
    ttk.Checkbutton(frame3, text=api_name, variable=var).grid(row=api_count // 4, column=api_count % 4, padx=5, pady=5, sticky="w")
    api_count += 1

# Create the "Upload Resume" button
upload_button = ttk.Button(root, text="Upload Resume", command=upload_resume)
upload_button.pack()
# Create a Label to display the selected resume file
resume_label = tk.Label(root, text="")
resume_label.pack(pady=10)
# Create the "Generate Output" button
generate_button = ttk.Button(root, text="Generate Results", command=generate_output)
generate_button.pack()

root.mainloop()

