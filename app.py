import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Bán Hàng", layout="centered")

st.title("🤖 AI Tư Vấn Bán Hàng")

# ===== THÔNG TIN SHOP =====
shop_name = st.text_input("🏪 Tên shop", "Shop Mẹ & Bé ABC")
zalo_link = st.text_input("📲 Link Zalo", "https://zalo.me/090XXXXXXX")
fb_link = st.text_input("📘 Link Facebook", "https://m.me/tenpage")

st.markdown("---")

# ===== API KEY =====
api_key = st.text_input("🔑 OpenAI API Key", type="password")
if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

# ===== SẢN PHẨM =====
products = st.text_area(
    "📦 Danh sách sản phẩm (mỗi dòng 1 sản phẩm)",
    """Khăn quấn chũn - 320.000đ - Giúp bé ngủ sâu
Đệm chống trào ngược - 890.000đ - Giảm ọc sữa"""
)

need = st.text_area(
    "🧑‍🍼 Nhu cầu khách hàng",
    "Bé 2 tháng tuổi ngủ không sâu"
)

if st.button("🤖 AI tư vấn"):
    with st.spinner("AI đang tư vấn..."):
        prompt = f"""
        Bạn là chuyên gia tư vấn bán hàng cho shop: {shop_name}

        Nhu cầu khách:
        "{need}"

        Danh sách sản phẩm:
        {products}

        - Chọn sản phẩm phù hợp
        - Giải thích dễ hiểu
        - Văn phong bán hàng nhẹ nhàng
        - Kết thúc bằng CTA đặt hàng
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là AI bán hàng cho shop Việt Nam."},
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("💬 Tư vấn từ AI")
        st.write(res.choices[0].message.content)

        st.markdown("### 📞 Đặt hàng")
        st.markdown(f"👉 **[Chat Zalo]({zalo_link})**")
        st.markdown(f"👉 **[Inbox Facebook]({fb_link})**")
