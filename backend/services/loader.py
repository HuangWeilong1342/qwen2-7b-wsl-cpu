import fitz  # PyMuPDF

from backend.utils.logger import logger


def load_pdf(pdf_path: str) -> str:
    """
    读取 PDF，返回全部文本
    """

    logger.info(f"Loading PDF: {pdf_path}")

    try:
        doc = fitz.open(pdf_path)

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        logger.info("PDF loaded successfully.")

        return text

    except Exception as e:
        logger.error(f"Failed to load PDF: {e}")
        raise
