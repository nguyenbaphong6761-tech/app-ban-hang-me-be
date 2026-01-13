import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Tư Vấn Bán Hàng", layout="centered")

st.title("🛒 AI Tư Vấn Bán Hàng")
st.write("Nhập nhu cầu – AI sẽ gợi ý sản phẩm phù hợp")

# Nhập API key
api_key = st.text_input("🔑 OpenAI API Key", type="password")
if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

# Danh sách sản phẩm (bạn đổi sau)
products = [
    {
        "name": "Khăn quấn chũn cho bé",
        "price": "320.000đ",
        "desc": "Giúp bé ngủ ngon, hạn chế giật mình"
    },
    {
        "name": "Đệm chống trào ngược",
        "price": "890.000đ",
        "desc": "Hỗ trợ tiêu hóa, giảm ọc sữa ban đêm"
    }
]

need = st.text_area(
    "📌 Nhu cầu của bạn",
    "Bé 2 tháng tuổi ngủ hay giật mình"
)

if st.button("🤖 AI tư vấn ngay"):
    with st.spinner("AI đang phân tích..."):
        product_text = "\n".join(
            [f"- {p['name']} ({p['price']}): {p['desc']}" for p in products]
        )

        prompt = f"""
        Bạn là chuyên gia tư vấn bán hàng trung thực.

        Nhu cầu khách hàng:
        "{need}"

        Danh sách sản phẩm:
        {product_text}

        Hãy gợi ý sản phẩm phù hợp, giải thích ngắn gọn, dễ hiểu,
        kết thúc bằng lời mời liên hệ đặt hàng.
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia tư vấn bán hàng."},
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("💬 Gợi ý cho bạn")
        st.write(res.choices[0].message.content)

        st.markdown("---")
        st.markdown("📞 **Liên hệ đặt hàng:**")
        st.markdown("👉 Zalo: **090xxxxxxx**")
