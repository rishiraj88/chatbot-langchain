import fitz

def extract_text_from_pdf(pdf_file_path):
    try:
        pdf_doc = fitz.open(pdf_file_path)
        pdf_text = ""

        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            pdf_text += page.get_text("text")
        
        pdf_doc.close()
        return pdf_text
    
    except Exception as e:
        return f"Error extracting text: {e}"
    
pdf_file = "Landon-Hotel.pdf"
extracted_pdf_text = extract_text_from_pdf(pdf_file)

file = open("data_text.txt", "w", encoding='utf-8')
file.write(extracted_pdf_text)