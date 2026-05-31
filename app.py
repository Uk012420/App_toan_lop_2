import streamlit as st
import json
import random

# ==========================================
# 1. CẤU HÌNH GIAO DIỆN & ẨN MENU
# ==========================================
st.set_page_config(page_title="Toán Lớp 2 - Nền tảng Tư duy", page_icon="🧸", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# 2. DỮ LIỆU LÝ THUYẾT LỚP 2
# ==========================================
THEORY_DATA = {
    "Cộng Trừ phạm vi 1000": {
        "khai_niem": "Thực hiện phép tính cộng, trừ với các số có 3 chữ số.",
        "phuong_phap": "Bước 1: Đặt tính thẳng cột (Hàng trăm thẳng hàng trăm, chục thẳng chục, đơn vị thẳng đơn vị).\nBước 2: Tính từ PHẢI sang TRÁI (từ hàng đơn vị trước).\nLưu ý: Nhớ cộng/trừ số nhớ sang hàng tiếp theo!",
        "sai_lam": "Quên không cộng số nhớ, hoặc đặt tính các số không thẳng cột với nhau."
    },
    "Bảng Nhân Chia (2,3,4,5)": {
        "khai_niem": "Nhân là cộng nhiều số giống nhau. Chia là chia đều thành các phần bằng nhau.",
        "phuong_phap": "- Học thuộc lòng các bảng nhân, chia từ 2 đến 5.\n- Mẹo: Phép nhân có tính chất giao hoán (Ví dụ: 3 x 4 cũng bằng 4 x 3 = 12).",
        "sai_lam": "Nhầm lẫn giữa dấu cộng và dấu nhân (Ví dụ sai: 2 x 3 = 5)."
    },
    "Đại lượng & Thời gian": {
        "khai_niem": "Đo độ dài (m, dm, cm, mm), cân nặng (kg) và thời gian (ngày, giờ, tháng).",
        "phuong_phap": "- Ghi nhớ quy đổi: 1m = 10dm = 100cm; 1dm = 10cm.\n- Muốn cộng trừ các số đo, chúng phải CÙNG MỘT ĐƠN VỊ đo.",
        "sai_lam": "Cộng trực tiếp các số khác đơn vị (Ví dụ sai: 1m + 20cm = 21). Phải đổi 1m = 100cm rồi mới cộng: 100 + 20 = 120cm."
    },
    "Hình học (Chu vi)": {
        "khai_niem": "Chu vi của một hình là độ dài đường bao quanh hình đó.",
        "phuong_phap": "- Chu vi hình tam giác = Tổng độ dài 3 cạnh.\n- Chu vi hình tứ giác = Tổng độ dài 4 cạnh.\n(Nhớ kiểm tra xem các cạnh đã cùng đơn vị đo chưa nhé).",
        "sai_lam": "Chỉ cộng 2 cạnh rồi dừng lại, hoặc quên ghi đơn vị ở đáp án."
    },
    "Toán Tư Duy (Nền tảng NTT)": {
        "khai_niem": "Các bài toán đố đòi hỏi con phải suy luận, vẽ sơ đồ hoặc tưởng tượng tình huống thực tế.",
        "phuong_phap": "Bước 1: Đọc thật kỹ đề, gạch chân các con số.\nBước 2: Vẽ sơ đồ tóm tắt hoặc nháp ra giấy.\nBước 3: Tìm phép tính ẩn giấu. (Ví dụ toán tính tuổi: Mỗi năm mỗi người đều tăng thêm 1 tuổi).",
        "sai_lam": "Đọc lướt đề bài, thấy số là cộng/trừ ngay mà không suy nghĩ ý nghĩa của bài toán."
    }
}

# ==========================================
# 3. GIAO DIỆN HỌC TẬP CHÍNH
# ==========================================
try:
    with open("data_toan_lop_2.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
except:
    st.error("Lỗi tải dữ liệu. Nhớ đưa file data_toan_lop_2.json vào cùng thư mục nhé!")
    st.stop()

list_types = list(set([q["type"] for q in questions]))

# --- MENU BÊN TRÁI ---
st.sidebar.title("🌟 Góc Học Tập Của Con")
mode = st.sidebar.radio("Hôm nay con muốn học gì?", ["📚 Ôn từng dạng toán", "📝 Thi thử khám phá"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Mẹo nhỏ:** Đọc kỹ đề bài trước khi nhập đáp án con nhé!")

# --- CHẾ ĐỘ 1: ÔN TẬP ---
if mode == "📚 Ôn từng dạng toán":
    st.title("📚 Chinh Phục Toán Lớp 2")
    selected_type = st.sidebar.selectbox("Con chọn thử thách nào:", list_types)
    
    if 'current_topic' not in st.session_state or st.session_state.current_topic != selected_type:
        st.session_state.current_topic = selected_type
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.answered = False

    filtered_questions = [q for q in questions if q["type"] == selected_type]
    total_questions = len(filtered_questions)
    
    tab_lt, tab_th = st.tabs(["📖 Xem Bí Kíp", "✍️ Bắt Đầu Làm Bài"])
    
    with tab_lt:
        theory = THEORY_DATA.get(selected_type, {})
        st.header(f"Bí kíp: {selected_type}")
        st.info(f"**📌 Cần nhớ:** {theory.get('khai_niem', '')}")
        st.success(f"**💡 Cách giải:**\n{theory.get('phuong_phap', '')}")
        st.warning(f"**⚠️ Cẩn thận nhầm lẫn:** {theory.get('sai_lam', '')}")

    with tab_th:
        if total_questions > 0:
            index = st.session_state.current_index
            if index < total_questions:
                q = filtered_questions[index]
                st.write(f"**Câu {index + 1} / {total_questions}** | 🌟 **Điểm: {st.session_state.score}**")
                st.progress((index + 1) / total_questions)
                
                with st.form(key=f"form_{q['id']}"):
                    st.info(f"**Đề bài:** {q['question']}")
                    user_ans = st.text_input("Ghi kết quả của con:")
                    btn_check = st.form_submit_button("Kiểm tra")
                    
                if btn_check:
                    if user_ans.strip().lower() == q["answer"].strip().lower():
                        st.success("🎉 Quá giỏi! Con đúng rồi!")
                        st.balloons()
                        if not st.session_state.answered:
                            st.session_state.score += 1
                            st.session_state.answered = True
                    else:
                        st.error(f"❌ Tiếc quá. Đáp án đúng là: {q['answer']}. Con thử lại ở câu sau nhé!")
                        st.session_state.answered = True
                        
                if st.button("Sang câu tiếp theo ➡️"):
                    st.session_state.current_index += 1
                    st.session_state.answered = False
                    st.rerun()
            else:
                st.success("🏆 HOÀN THÀNH XUẤT SẮC!")
                st.write(f"🎯 Điểm của con: {st.session_state.score} / {total_questions}")
                if st.button("🔄 Luyện tập lại từ đầu"):
                    st.session_state.current_index = 0
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.rerun()

# --- CHẾ ĐỘ 2: THI THỬ ---
elif mode == "📝 Thi thử khám phá":
    st.title("📝 Đề Thi Khám Phá Tư Duy (10 Câu)")
    
    if 'exam_generated' not in st.session_state or not st.session_state.exam_generated:
        exam_qs = []
        for t in list_types:
            qs_of_type = [q for q in questions if q["type"] == t]
            if len(qs_of_type) >= 2: exam_qs.extend(random.sample(qs_of_type, 2))
            else: exam_qs.extend(qs_of_type)
        random.shuffle(exam_qs)
        st.session_state.exam_qs = exam_qs[:10]
        st.session_state.exam_generated = True
        st.session_state.exam_submitted = False

    if not st.session_state.exam_submitted:
        with st.form("exam_form"):
            user_answers = {}
            for i, q in enumerate(st.session_state.exam_qs):
                st.markdown(f"**Câu {i+1}:** {q['question']}")
                user_answers[q['id']] = st.text_input(f"Đáp án:", key=f"exam_{q['id']}")
                st.write("---")
            
            if st.form_submit_button("✅ NỘP BÀI"):
                st.session_state.user_answers = user_answers
                st.session_state.exam_submitted = True
                st.rerun()
    else:
        st.header("📊 KẾT QUẢ CUỘC THI")
        total_score = 0
        for q in st.session_state.exam_qs:
            if st.session_state.user_answers[q['id']].strip().lower() == q["answer"].strip().lower():
                total_score += 1
                
        st.write(f"### 🌟 Số câu đúng: {total_score} / {len(st.session_state.exam_qs)}")
        if total_score == len(st.session_state.exam_qs):
            st.success("Tuyệt đỉnh! Con có tố chất học Toán vô cùng tuyệt vời!")
            st.balloons()
        else:
            st.info("Cố gắng rèn luyện thêm con nhé, mỗi ngày tiến bộ một chút!")
        
        if st.button("🔄 Thi lại đề khác"):
            st.session_state.exam_generated = False
            st.rerun()