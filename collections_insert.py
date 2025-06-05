from flask import Flask
from exchange_items import db, create_app
from exchange_items.models import Collection, User, Offer

# Initialize the Flask app and database connection
app = create_app()

# Collections data with categorical organization and icon URLs
collections_data = [
    # Thời trang & Phong cách (Fashion & Personal Items)
    {"name": "Street Style Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Vibes Retro Cực Đã", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Style Bền Vững Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Phụ Kiện Siêu Xinh", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Giày Fresh Mỗi Ngày", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Kit Đồ Làm Đẹp", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Hàng Limited Hiếm", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Outfit Chất Lừ Đây", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Đồ Si Tuyển Chọn", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Trang Sức Độc Lạ", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Hub Thời Trang Alt", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Thời Trang Y2K Xịn", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Spotlight Brand Indie", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Custom Quần Áo Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},
    {"name": "Góc Sneakerhead", "icon_url": "https://static.chotot.com/storage/categories/all-category/3000.png"},

    # Điện tử & Công nghệ (Electronics & Tech)
    {"name": "Lên Đời Công Nghệ", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Gear Game Thủ Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Kit Đồ Sáng Tạo", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Nhà Thông Minh Nay", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Deal Phone Ngon", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Đồ Công Nghệ Cổ", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Âm Thanh Đỉnh Cao", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Build PC Ước Mơ", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Công Nghệ Di Động", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Setup Stream Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Tech Ngon Bổ Rẻ", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Hub Đồ Coding", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Trải Nghiệm VR Real", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Zone Drone Siêu Vui", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},
    {"name": "Tech Đeo Tay Nay", "icon_url": "https://static.chotot.com/storage/categories/all-category/5000.png"},

    # Sở thích, Giải trí & Thể thao (Hobbies, Leisure & Sports)
    {"name": "Hub Sở Thích Đây", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Trung Tâm Game Thủ", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Kho Báu Sưu Tầm", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Đồ Dã Ngoại Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/4000.png"},
    {"name": "Góc Mọt Sách Xịn", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Nhạc Cụ Đam Mê", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Fitness Khởi Đầu Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/4000.png"},
    {"name": "Shop Đồ Vẽ Art", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Board Game Hội Tụ", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Kit Đồ Tự Làm", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Đồ Lướt Ván Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/4000.png"},
    {"name": "Merch Band Xịn Sò", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Fan Điện Ảnh Đây", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Gear Nhiếp Ảnh Pro", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Góc Craft Vui Vẻ", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},

    # Thú cưng (Pets)
    {"name": "Zone Bạn Bốn Chân", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Đồ Pet Siêu Cưng", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Góc Pet Độc Lạ", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Bạn Lông Vũ Vui", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Setup Hồ Cá Xinh", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Outfit Pet Cute", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Đồ Chơi Pet Ngập", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Thức Ăn Pet Khoẻ", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Thiên Đường Pet Nhỏ", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},
    {"name": "Chỗ Hội Yêu Chó", "icon_url": "https://static.chotot.com/storage/categories/all-category/12000.png"},

    # Đồ gia dụng & Nội thất (Household Items & Furniture)
    {"name": "Setup Phòng Trọ Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Nâng Cấp Nhà Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Decor Kiểu Boho", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Style Sống Tối Giản", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Gia Dụng Xanh Sạch", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Hội Yêu Cây Đây", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Gadget Bếp Hay Ho", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Góc Chill Tại Gia", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Thiết Bị Nhà Thông Minh",
     "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Nội Thất Tái Chế", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Makeover Phòng Xinh", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Đồ Setup Góc Học", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Zone Đèn Mood Chill", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Chill Ban Công Ngay", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Quirky Home Decor", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},

    # Sách Truyện Tri Thức (Books & Knowledge)
    {"name": "Truyện Tranh Đỉnh Cao", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Sách Self-Help GenZ", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Tiểu Thuyết Trending", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "BookTok Gợi Ý Xịn", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},
    {"name": "Artbook & Sách Ảnh", "icon_url": "https://static.chotot.com/storage/categories/all-category/7000.png"},

    # Thiết Kế & Decor Nhà GenZ (GenZ Home Design & Decor)
    {"name": "DIY Nhà Xinh Lung Linh",
     "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Góc Gaming Siêu Ngầu", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Nội Thất Minimal Cool",
     "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Phủ Xanh Không Gian Chill",
     "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},
    {"name": "Đèn Mood Sống Ảo", "icon_url": "https://static.chotot.com/storage/categories/all-category/14000.png"},

    # Xe cộ (Vehicles)
    {"name": "Xe Xanh Hôm Nay", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Hub Hội Xe Đạp", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Deal Xe Đầu Đời", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Team Xe Máy Điện", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Zone Độ Xe Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Xế Cổ Cực Ngầu", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Di Chuyển Điện Nay", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Đồ Xe Fixie Xịn", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "Campus Cruiser Deals", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},
    {"name": "E-Scooter Cực Hot", "icon_url": "https://static.chotot.com/storage/categories/all-category/1020.png"},

    # Tổng hợp, Du lịch & Ẩm thực (Miscellaneous, Travel & Food)
    {"name": "Món Ngon Mỗi Ngày", "icon_url": "https://static.chotot.com/storage/categories/all-category/9000.png"},
    {"name": "Guide Quán Ăn Ngon", "icon_url": "https://static.chotot.com/storage/categories/all-category/9000.png"},
    {"name": "Deal Du Lịch Rẻ", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Kit WFH Cần Thiết", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Setup Góc Học Xịn", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Quà Tặng Độc Đáo", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Sống Xanh Hiện Đại", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Đồ Handmade Local", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Gear Đi Quẩy Chất", "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
    {"name": "Trải Nghiệm Chất Lượng",
     "icon_url": "https://static.chotot.com/storage/categories/all-category/6000.png"},
]

users_data = [
    {"name": "John Doe", "type": "Seller"},
    {"name": "Jane Smith", "type": "Buyer"},
    {"name": "Alice Johnson", "type": "Seller"},
    {"name": "Bob Brown", "type": "Buyer"},
]

offers_data = [
    {"id": 1, "ads_id": 1, "owner_id": 1, "status": "new"},
    {"id": 2, "ads_id": 2, "owner_id": 1, "status": "new"},
    {"id": 3, "ads_id": 3, "owner_id": 2, "status": "new"},
    {"id": 4, "ads_id": 4, "owner_id": 2, "status": "new"},
    {"id": 5, "ads_id": 5, "owner_id": 3, "status": "new"},
]

with app.app_context():
    # # Create a test user first
    # for user_info in users_data:
    #     user = User(name=user_info["name"], type=user_info["type"])
    #     db.session.add(user)
    # db.session.commit()


    # Create a test offers data
    for offer_info in offers_data:
        offer = Offer(id=offer_info["id"], ads_id=offer_info["ads_id"], owner_id=offer_info["owner_id"], status=offer_info["status"])
        db.session.add(offer)
    db.session.commit()

    # Add collections with proper icon URLs
    # for collection_info in collections_data:
    #     collection = Collection(
    #         name=collection_info["name"],
    #         icon_url=collection_info["icon_url"]
    #     )
    #     db.session.add(collection)
    #
    # # Commit all changes
    # db.session.commit()
    # print(f"Added {len(collections_data)} collections")