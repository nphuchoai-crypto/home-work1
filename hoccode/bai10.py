from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def add_vat(price: float, vat_percent: float) -> float:
	return price * (100 + vat_percent) / 100


class InvoiceInput(BaseModel): # Schema, qui định kiểu dữ liệu đầu vào cho API (スキーマ)
	price: float
	vat_percent: float


@app.post("/api/invoices/add-vat") # Endpoint, định nghĩa hướng dẫn và URL cho API
def api_calculate_invoice_total(invoice: InvoiceInput):
	return {
		"price_after_vat": add_vat(invoice.price, invoice.vat_percent)
	}


if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)
