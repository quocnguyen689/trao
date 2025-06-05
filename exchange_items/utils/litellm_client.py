import openai

client = openai.OpenAI(
    api_key="sk-lncyFnWaD14nhE5FCbxRSw",
    base_url="https://llm.chotot.org"
)

def generate_short_description(subject: str, body: str, category_name: str, region_name: str) -> str:
    # Example function to generate a short description using the client
    content =f"""
                Bạn là một copywriter chuyên viết content Gen Z cho sàn thương mại điện tử.
                Dựa trên thông tin sản phẩm sau (subject, mô tả, danh mục, khu vực), hãy viết một mô tả ngắn gọn, hấp dẫn, đúng style Gen Z, tối đa 15 từ, dùng emoji (nếu phù hợp), không viết nghiêm túc hay dài dòng.
                Input:
                Tên sản phẩm (subject): {subject}
                Mô tả chi tiết (body): {body}
                Danh mục: {category_name}
                Khu vực: {region_name}
                Output yêu cầu:
                Một dòng mô tả duy nhất, tối đa 15 từ
                Mang tone vui vẻ, trẻ trung, đơn giản
                Dùng tiếng lóng hoặc emoji nếu cần
    """.format(
        subject=subject,
        body=body,
        category_name=category_name,
        region_name=region_name
    )

    response = client.chat.completions.create(
        model="gpt-4o",  # model to send to the proxy
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return response.choices[0].message.content

def suggest_collections(ad_response):
    """
    Suggest relevant collections based on Chotot ad response
    Args:
        ad_response (dict): Response from Chotot ad listing API
    Returns:
        list: List of suggested collection names with scores
    """
    # Extract key information
    ad_info = ad_response.get('ad', {})
    subject = ad_info.get('subject', '')
    category = ad_info.get('category_name', '')
    body = ad_info.get('body', '')
    condition = ad_info.get('condition_ad_name', '')
    price = ad_info.get('price_string', '')
    region = ad_info.get('region_name', '')

    prompt = """Bạn là một chuyên gia về xu hướng Gen Z và là người quản lý các bộ sưu tập (collections) trên sàn thương mại điện tử.

Thông tin về sản phẩm:
- Tên sản phẩm: {0}
- Mô tả: {1}
- Danh mục: {2}
- Tình trạng: {3}
- Giá: {4}
- Khu vực: {5}

Dựa trên thông tin sản phẩm trên, hãy gợi ý 6 collections phù hợp nhất từ danh sách dưới đây. Các collections được gợi ý phải:
1. Phù hợp với tính chất sản phẩm
2. Phù hợp với thị hiếu và cách dùng từ của Gen Z
3. Tạo được sự thu hút và trending
4. Có tính chất community (nơi những người có cùng sở thích tụ họp)

Danh sách collections theo nhóm:

**Thời trang & Phong cách (Fashion & Personal Items)**
1.  Street Style Chất
2.  Vibes Retro Cực Đã
3.  Style Bền Vững Ngay
4.  Phụ Kiện Siêu Xinh
5.  Giày Fresh Mỗi Ngày
6.  Kit Đồ Làm Đẹp
7.  Hàng Limited Hiếm
8.  Outfit Chất Lừ Đây
9.  Đồ Si Tuyển Chọn
10. Trang Sức Độc Lạ
11. Hub Thời Trang Alt
12. Thời Trang Y2K Xịn
13. Spotlight Brand Indie
14. Custom Quần Áo Ngay
15. Góc Sneakerhead

**Điện tử & Công nghệ (Electronics & Tech)**
16. Lên Đời Công Nghệ
17. Gear Game Thủ Chất
18. Kit Đồ Sáng Tạo
19. Nhà Thông Minh Nay
20. Deal Phone Ngon
21. Đồ Công Nghệ Cổ
22. Âm Thanh Đỉnh Cao
23. Build PC Ước Mơ
24. Công Nghệ Di Động
25. Setup Stream Ngay
26. Tech Ngon Bổ Rẻ
27. Hub Đồ Coding
28. Trải Nghiệm VR Real
29. Zone Drone Siêu Vui
30. Tech Đeo Tay Nay

**Sở thích, Giải trí & Thể thao (Hobbies, Leisure & Sports)**
31. Hub Sở Thích Đây
32. Trung Tâm Game Thủ
33. Kho Báu Sưu Tầm
34. Đồ Dã Ngoại Chất
35. Góc Mọt Sách Xịn
36. Nhạc Cụ Đam Mê
37. Fitness Khởi Đầu Ngay
38. Shop Đồ Vẽ Art
39. Board Game Hội Tụ
40. Kit Đồ Tự Làm
41. Đồ Lướt Ván Chất
42. Merch Band Xịn Sò
43. Fan Điện Ảnh Đây
44. Gear Nhiếp Ảnh Pro
45. Góc Craft Vui Vẻ

**Thú cưng (Pets)**
46. Zone Bạn Bốn Chân
47. Đồ Pet Siêu Cưng
48. Góc Pet Độc Lạ
49. Bạn Lông Vũ Vui
50. Setup Hồ Cá Xinh
51. Outfit Pet Cute
52. Đồ Chơi Pet Ngập
53. Thức Ăn Pet Khoẻ
54. Thiên Đường Pet Nhỏ
55. Chỗ Hội Yêu Chó

**Đồ gia dụng & Nội thất (Household Items & Furniture)**
56. Setup Phòng Trọ Chất
57. Nâng Cấp Nhà Ngay
58. Decor Kiểu Boho
59. Style Sống Tối Giản
60. Gia Dụng Xanh Sạch
61. Hội Yêu Cây Đây
62. Gadget Bếp Hay Ho
63. Góc Chill Tại Gia
64. Thiết Bị Nhà Thông Minh
65. Nội Thất Tái Chế
66. Makeover Phòng Xinh
67. Đồ Setup Góc Học
68. Zone Đèn Mood Chill
69. Chill Ban Công Ngay
70. Quirky Home Decor

**Sách Truyện Tri Thức (Books & Knowledge)**
71. Truyện Tranh Đỉnh Cao
72. Sách Self-Help GenZ
73. Tiểu Thuyết Trending
74. BookTok Gợi Ý Xịn
75. Artbook & Sách Ảnh

**Thiết Kế & Decor Nhà GenZ (GenZ Home Design & Decor)**
76. DIY Nhà Xinh Lung Linh
77. Góc Gaming Siêu Ngầu
78. Nội Thất Minimal Cool
79. Phủ Xanh Không Gian Chill
80. Đèn Mood Sống Ảo

**Xe cộ (Vehicles)**
81. Xe Xanh Hôm Nay
82. Hub Hội Xe Đạp
83. Deal Xe Đầu Đời
84. Team Xe Máy Điện
85. Zone Độ Xe Chất
86. Xế Cổ Cực Ngầu
87. Di Chuyển Điện Nay
88. Đồ Xe Fixie Xịn
89. Campus Cruiser Deals
90. E-Scooter Cực Hot

**Tổng hợp, Du lịch & Ẩm thực (Miscellaneous, Travel & Food)**
91. Món Ngon Mỗi Ngày
92. Guide Quán Ăn Ngon
93. Deal Du Lịch Rẻ
94. Kit WFH Cần Thiết
95. Setup Góc Học Xịn
96. Quà Tặng Độc Đáo
97. Sống Xanh Hiện Đại
98. Đồ Handmade Local
99. Gear Đi Quẩy Chất
100. Trải Nghiệm Chất Lượng

Output yêu cầu:
- Theo format JSON như mẫu sau: collection_id, name, score, reason
- Với mỗi collection, giải thích ngắn gọn (1-2 câu) tại sao nó phù hợp với sản phẩm và Gen Z
- Sử dụng ngôn ngữ Gen Z, emoji và hashtag nếu phù hợp"""

    content = prompt.format(subject, body, category, condition, price, region)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return response.choices[0].message.content
    

print(generate_short_description(
    subject="Iphone 13 128Gb hồng, pin 100%",
    body="Máy đẹp keng, pin 100%, mua chưa đầy 1 năm, không trầy xước, fullbox.",
    category_name="Điện thoại",
    region_name="TP.HCM"
))

print(suggest_collections(
    ad_response={
        "ad": {
            "subject": "Iphone 13 128Gb hồng, pin 100%",
            "body": "Máy đẹp keng, pin 100%, mua chưa đầy 1 năm, không trầy xước, fullbox.",
            "category_name": "Điện thoại",
            "region_name": "TP.HCM",
            "condition_ad_name": "Còn Mới 99%",
            "price_string": "1000000",
            "region": "TP.HCM"
        }
    }
))