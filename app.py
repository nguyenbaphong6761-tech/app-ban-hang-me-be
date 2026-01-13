import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Tư Vấn Bán Hàng", layout="centered")

st.title("🛒 AI Tư Vấn Sản Phẩm Mẹ & Bé")
st.write("Nhập nhu cầu – AI gợi ý sản phẩm phù hợp")

api_key = st.text_input("🔑 OpenAI API Key", type="password")
if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

products = [
    {
        "name": "Khăn quấn chũn cao cấp",
        "price": "320.000đ",
        "desc": "Giúp bé ngủ sâu, hạn chế giật mình"
    },
    {
        "name": "Đệm chống trào ngược",
        "price": "890.000đ",
        "desc": "Giảm ọc sữa, hỗ trợ tiêu hóa"
    }
]

need = st.text_area(
    "📌 Nhu cầu của bạn",
    "Bé 2 tháng tuổi ngủ không sâu"
)

if st.button("🤖 AI tư vấn"):
    with st.spinner("AI đang tư vấn..."):
        product_text = "\n".join(
            [f"- {p['name']} ({p['price']}): {p['desc']}" for p in products]
        )

        prompt = f"""
        Bạn là chuyên gia tư vấn mẹ và bé.

        Nhu cầu khách hàng:
        "{need}"

        Danh sách sản phẩm:
        {product_text}

        - Gợi ý 1–2 sản phẩm phù hợp
        - Giải thích ngắn gọn
        - Kết thúc bằng CTA đặt hàng
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia tư vấn mẹ và bé tại Việt Nam."},
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("💬 Gợi ý cho bạn")
        st.write(res.choices[0].message.content)

        st.markdown("---")
        st.markdown("### 📲 Đặt hàng ngay")
        st.markdown(
            "👉 **[Chat Zalo với shop](https://zalo.me/0937937504)**"
        )
        st.markdown(
            "👉 **[Inbox Facebook](https://m.me/tenpage)**"
        )
