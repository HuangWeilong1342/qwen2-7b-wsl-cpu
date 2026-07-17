from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from scripts.build_index import build_index

router = APIRouter()

PDF_DIR = Path("data/pdf")


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    上传 PDF 并重建知识库
    """

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    PDF_DIR.mkdir(parents=True, exist_ok=True)

    save_path = PDF_DIR / file.filename

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    build_index()

    return {
        "message": "Upload successful.",
        "filename": file.filename
    }
