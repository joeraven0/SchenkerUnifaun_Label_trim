from PyPDF2 import PdfWriter, PdfReader
import subprocess
import os
import glob
import shutil
from datetime import datetime

MAP_SOKVAG = r"C:\Users\jr\Dropbox\Automatisering\Schenker"
PREFIX = 'prt*'
FILE_EXTENSION = '.pdf'
INPUT_DIR = 'crop_input'
OUTPUT_DIR = 'crop_output'
COMBINE_PDFS = 1  # Sätt till 1 för att kombinera PDFs, 0 för att hålla dem separata.

def get_schenker_files():
    search_pattern = os.path.join(MAP_SOKVAG, PREFIX + FILE_EXTENSION)
    files = glob.glob(search_pattern)

    original_names = [os.path.basename(f) for f in files]
    new_names = ["crop_" + name.replace(" ", "_") for name in original_names]

    return original_names, new_names

def crop_schenker(filename, combined_writer=None):
    reader = PdfReader(filename)
    writer = PdfWriter() if combined_writer is None else combined_writer

    for page in reader.pages:
        page.cropbox.upper_left = (20, 640)
        page.cropbox.lower_right = (283, 20)
        writer.add_page(page)

    if combined_writer is None:
        write_pdf(writer, filename)

    return writer

def write_pdf(writer, filename):
    with open(filename, 'wb') as fp:
        writer.write(fp)

def move_files(original_name, new_name):
    shutil.move(os.path.join(MAP_SOKVAG, original_name), os.path.join(MAP_SOKVAG, INPUT_DIR, original_name))
    shutil.move(os.path.join(MAP_SOKVAG, new_name), os.path.join(MAP_SOKVAG, OUTPUT_DIR, new_name))

if __name__ == '__main__':
    os.makedirs(os.path.join(MAP_SOKVAG, INPUT_DIR), exist_ok=True)
    os.makedirs(os.path.join(MAP_SOKVAG, OUTPUT_DIR), exist_ok=True)

    original_files, new_files = get_schenker_files()
    # Kontrollera om listan över originalfiler är tom
    if not original_files:
        print("Inga PDF-filer hittades. Programmet avslutas. Säkerställ filsökväg är ok.")
        exit()  # Avsluta programmet
    combined_writer = None
    if COMBINE_PDFS:
        combined_writer = PdfWriter()

    for orig, new in zip(original_files, new_files):
        print(orig)
        print(new)
        if COMBINE_PDFS:
            crop_schenker(os.path.join(MAP_SOKVAG, orig), combined_writer)
        else:
            crop_schenker(os.path.join(MAP_SOKVAG, orig), os.path.join(MAP_SOKVAG, OUTPUT_DIR, new))
            move_files(orig, new)
            subprocess.Popen(['start', os.path.join(MAP_SOKVAG, OUTPUT_DIR, new)], shell=True)

    if COMBINE_PDFS:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        combined_filename = os.path.join(MAP_SOKVAG, OUTPUT_DIR, f"combined_{timestamp}.pdf")
        write_pdf(combined_writer, combined_filename)
        for orig in original_files:
            shutil.move(os.path.join(MAP_SOKVAG, orig), os.path.join(MAP_SOKVAG, INPUT_DIR, orig))
        subprocess.Popen(['start', combined_filename], shell=True)
