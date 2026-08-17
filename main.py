# main.py (Entry Point): Nơi khởi chạy ứng dụng
# Nó khởi tạo FastAPI app và dùng app.include_router(router) để gắn các API từ nơi khác vào
# Nhiệm vụ của nó chỉ là khởi chạy hệ thống
from fastapi import FastAPI
from api.endpoints import router
app = FastAPI(title="50 Bài tập Python Backend - Logic nghiệp vụ")

# Gắn các router từ file endpoints vào app chính
app.include_router(router)

# uvicorn main:app --reload - chạy code
# http://localhost:8000/docs - check api
