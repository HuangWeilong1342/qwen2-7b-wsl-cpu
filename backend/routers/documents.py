from pathlib import Path

from fastapi import APIRouter, HTTPException

from scripts.build_index import build_index

router = APIRouter()

PDF_DIR = Path("data/pdf")


@router.get("/documents")
def get_documents():
    """
    获取知识库中的所有 PDF
    """

    documents = []

    for pdf in PDF_DIR.glob("*.pdf"):
        documents.append(pdf.name)

    documents.sort()

    return {
        "count": len(documents),
        "documents": documents
    }


@router.delete("/documents/{filename}")
def delete_document(filename: str):
    """
    删除 PDF，并自动重建知识库
    """

    pdf_path = PDF_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    # 删除文件
    pdf_path.unlink()

    # 重建索引
    build_index()

    return {
        "message": "Delete successful.",
        "filename": filename
    }
