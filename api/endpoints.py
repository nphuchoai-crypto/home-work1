# api/ (Tiền sảnh Presentation Layer): Nơi tiếp khách và gọi order, trả món

# endpoints.py (Lễ tân/ Bồi bàn): Nhận HTTP Request

# schemas.py (Menu/ Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation)
from fastapi import APIRouter
from typing import List
from core.easy_services import (filter_available, cart_total, order_message, 
                                classify_customer, active_users, lastest_order,
                                 daily_revenue, hide_password, order_code ) 
from api.schemas import (ProductInput, CartItem, OrderStatusInput, TotalSpentInput, 
                         UserInput, Order_IDInput)

router = APIRouter()
# API câu 1
@router.post("/api/products/available")
def api_filter_available(products: List[ProductInput]):
    # Chuyển đổi list các Pydantic Model thành list các dict
    products_list = [p.model_dump() for p in products]

    # Gọi hàm nghiệp vụ và trả kết quả
    filtered = filter_available(products_list)
    return filtered

# API câu 2
@router.post("/api/cart/total")
def api_cart_total(cart: List[CartItem]):
    cart_dict = [item.model_dump() for item in cart]

    total = cart_total(cart_dict)
    # Trả về dạng JSON
    return {"total": total}

# API câu 4
@router.post("/api/order/message")
def api_order_message(payload: OrderStatusInput):
    # Gọi hàm nghiệp vụ và trả kết quả
    message = order_message(payload.status)

    # JSON
    return {"message": message}
# API câu 13
@router.post("/api/customer/classify")
def api_classify_customer(payload: TotalSpentInput):
    # Gọi hàm nghiệp vụ và trả vê kết quả
    classification = classify_customer(payload.total_spent)
    return {"classification": classification}

# API câu 15
@router.post("/api/admin/users/active")
def api_get_active_users(user: List[UserInput]):
    # Chuyển đổi dữ liệu Pydantic thành list of Dictionaries thuần
    users_dict = [u.model_dump() for u in users]

    # Gọi hàm nghiệp vụ cốt lõi
    filtered_user = active_users(users_dict)

    # Trả về kết quả
    return {"active_users": filtered_user}



