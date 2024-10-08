import os
import sys
import PyPDF2

def split_pdf(file_path, max_size_mb):
    max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to Bytes
    pdf_reader = PyPDF2.PdfReader(file_path)

    current_pdf_writer = PyPDF2.PdfWriter()
    current_pdf_size = 0
    part_number = 1

    for page_number in range(len(pdf_reader.pages)):
        current_pdf_writer.add_page(pdf_reader.pages[page_number])
        current_pdf_size += os.path.getsize(file_path) / len(pdf_reader.pages)  # Approximate page size

        if current_pdf_size >= max_size_bytes or page_number == len(pdf_reader.pages) - 1:
            output_file = f'split_part_{part_number}.pdf'
            with open(output_file, 'wb') as output_pdf:
                current_pdf_writer.write(output_pdf)
            print(f'Created: {output_file}')
            part_number += 1
            current_pdf_writer = PyPDF2.PdfWriter()
            current_pdf_size = 0

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python split_pdf.py <path_to_pdf> <max_size_mb>")
        sys.exit(1)

    split_pdf(sys.argv[1], int(sys.argv[2]))
