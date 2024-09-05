from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter()

# Defina o diretório onde as imagens serão salvas (use um caminho relativo ou absoluto, conforme necessário)
UPLOAD_DIRECTORY = "./uploaded_images"  # Caminho relativo
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Defina o caminho completo onde a imagem será salva
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
        
        # Salve o arquivo no diretório especificado
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return JSONResponse(content={"info": f"Arquivo '{file.filename}' salvo com sucesso!"}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
