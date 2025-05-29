import fitz  # PyMuPDF
import camelot

def pdf_agent(file_path):
    # Open PDF
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Extract tables with camelot (returns list of tables)
    tables = camelot.read_pdf(file_path, pages='all')
    tables_data = [table.df.to_dict() for table in tables]

    # Prepare output summary (preview text + page count + tables)
    preview = text[:500].replace("\n", " ")  # first 500 chars
    
    output = {
        "filename": file_path.split("/")[-1],
        "content_preview": preview,
        "page_count": doc.page_count,
        "tables_extracted": tables_data
    }
    return output

