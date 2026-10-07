# api/ (Tiền sảnh Presentation Layer): Nơi tiếp khách và gọi order, trả món

# endpoints.py (Lễ tân/ Bồi bàn): Nhận HTTP Request

# schemas.py (Menu/ Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation)
from fastapi import APIRouter
from typing import List
from core.easy_services import (filter_available, cart_total, cheapest_product, lastest_order, order_message, 
                                classify_customer, active_users, lastest_order,
                                 daily_revenue, hide_password, order_code ) 
from api.schemas import (ProductInput, CartItem, ProductPriceInput, OrderStatusInput, TotalSpentInput, 
                         UserInput, Order_IDInput, TransactionInput, OrderCodeInput)

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
    users_dict = [u.model_dump() for u in user]

    # Gọi hàm nghiệp vụ cốt lõi
    filtered_user = active_users(users_dict)

    # Trả về kết quả
    return {"active_users": filtered_user}

# API câu 16
@router.post("/api/orders/lastest")
def api_get_lastest_order(orders: List[Order_IDInput]):
    # Chuyển đổi dữ liệu Pydantic thành list of Dictionaries thuần
    orders_dict = [o.model_dump() for o in orders]

    # Gọi hàm nghiệp vụ cốt lõi
    lastest_order_result = lastest_order(orders_dict)

    # Trả về kết quả
    return({"lastest_order": lastest_order_result})

# API câu 17
@router.post("/api/transactions/daily_revenue")
def api_daily_revenue(transactions: List[TransactionInput]):
    # Chuyển đổi dữ liệu Pydantic thành list of Dictionaries thuần
    transaction_dict = [t.model_dump() for t in transactions]

    # Gọi hàm nghiệp vụ cốt lõi
    total_revenue = daily_revenue(transaction_dict)

    # Trả về kết quả
    return({"total_revenue": total_revenue})

# API câu 18
@router.post("/api/admin/users/hide_password")
def api_hide_password(users: List[UserInput]):
    # Chuyển đổi dữ liệu Pydantic thành list of Dictionaries thuần
    users_dict = [u.model_dump() for u in users]

    # Gọi hàm nghiêpj vụ cốt lõi
    hidden_password_users = hide_password(users_dict)

    # Trả về kết quả
    return {"users": hidden_password_users}

# API câu 19
@router.post("/api/orders/code")
def api_orders_code(payload: OrderCodeInput):
    # Gọi hàm nghiệp vụ cốt lõi
    order_code_result = order_code(payload.order_id)

    # Trả về kết quả
    return {"order_code": order_code_result}

# API (câu 22) Tìm sản phẩm có giá thấp nhất
@router.post("/api/products/cheapest")
def api_cheapest_product(products: List[ProductPriceInput]):
    products_dict = [product.model_dump() for product in products]

    return cheapest_product(products_dict)
    
    



    




