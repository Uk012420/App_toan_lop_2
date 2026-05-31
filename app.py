import streamlit as st
import json
import random
import time
import streamlit.components.v1 as components

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
# 2. LÝ THUYẾT (GIỮ NGUYÊN)
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
        "phuong_phap": "- Chu vi hình tam giác = Tổng độ dài 3 cạnh.\n- Chu vi tứ giác/chữ nhật = Tổng độ dài 4 cạnh.\n(Nhớ kiểm tra xem các cạnh đã cùng đơn vị đo chưa nhé).",
        "sai_lam": "Chỉ cộng 2 cạnh rồi dừng lại, hoặc quên ghi đơn vị ở đáp án."
    },
    "Toán Tư Duy (Nền tảng NTT)": {
        "khai_niem": "Các bài toán đố đòi hỏi con phải suy luận, vẽ sơ đồ hoặc tưởng tượng tình huống thực tế.",
        "phuong_phap": "Bước 1: Đọc thật kỹ đề, gạch chân các con số.\nBước 2: Vẽ sơ đồ tóm tắt hoặc nháp ra giấy.\nBước 3: Tìm phép tính ẩn giấu. (Ví dụ toán tính tuổi: Mỗi năm mỗi người đều tăng thêm 1 tuổi).",
        "sai_lam": "Đọc lướt đề bài, thấy số là cộng/trừ ngay mà không suy nghĩ ý nghĩa của bài toán."
    }
}

# ==========================================
# 3. TẢI DỮ LIỆU
# ==========================================
try:
    with open("data_toan_lop_2.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
except:
    st.error("Chưa có file dữ liệu. Bạn hãy chạy file tao_du_lieu_lop2.py trước nhé!")
    st.stop()

list_types = list(set([q["type"] for q in questions]))

# --- MENU BÊN TRÁI ---
st.sidebar.title("🌟 Góc Học Tập Của Con")
mode = st.sidebar.radio("Hôm nay con muốn học gì?", ["📚 Ôn từng dạng toán", "⏱️ Thi thử (Có bấm giờ)"])

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
        st.info(f"**📌 Cần nhớ:** {theory.get('khai_niem', '')}")
        st.success(f"**💡 Cách giải:**\n{theory.get('phuong_phap', '')}")
        st.warning(f"**⚠️ Cẩn thận nhầm lẫn:** {theory.get('sai_lam', '')}")

    with tab_th:
        if total_questions > 0:
            index = st.session_state.current_index
            if index < total_questions:
                q = filtered_questions[index]
                st.write(f"**Câu {index + 1} / {total_questions}** | 🌟 **Điểm: {st.session_state.score}**")
                with st.form(key=f"form_{q['id']}"):
                    st.info(f"**Đề bài:** {q['question']}")
                    user_ans = st.text_input("Ghi kết quả của con:")
                    btn_check = st.form_submit_button("Kiểm tra")
                    
                if btn_check:
                    if user_ans.strip().lower() == q["answer"].strip().lower():
                        st.success("🎉 Quá giỏi! Con đúng rồi!")
                        if not st.session_state.answered:
                            st.session_state.score += 1
                            st.session_state.answered = True
                    else:
                        st.error(f"❌ Tiếc quá. Đáp án đúng là: {q['answer']}.")
                        st.session_state.answered = True
                        
                if st.button("Sang câu tiếp theo ➡️"):
                    st.session_state.current_index += 1
                    st.session_state.answered = False
                    st.rerun()
            else:
                st.success(f"🏆 HOÀN THÀNH! Điểm của con: {st.session_state.score} / {total_questions}")
                if st.button("🔄 Luyện tập lại"):
                    st.session_state.current_index = 0
                    st.session_state.score = 0
                    st.rerun()

# --- CHẾ ĐỘ 2: THI THỬ CÓ BẤM GIỜ ---
elif mode == "⏱️ Thi thử (Có bấm giờ)":
    st.title("⏱️ Đề Thi Năng Lực (20 Phút)")
    
    # THUẬT TOÁN SINH ĐỀ CHUẨN 5 - 7 - 3
    if 'exam_generated' not in st.session_state or not st.session_state.exam_generated:
        q_m1 = [q for q in questions if q["level"] == "Mức 1"]
        q_m2 = [q for q in questions if q["level"] == "Mức 2"]
        q_m3 = [q for q in questions if q["level"] == "Mức 3"]
        
        # Bốc ngẫu nhiên
        exam_qs = random.sample(q_m1, min(5, len(q_m1))) + \
                  random.sample(q_m2, min(7, len(q_m2))) + \
                  random.sample(q_m3, min(3, len(q_m3)))
        
        random.shuffle(exam_qs) # Trộn đều thứ tự câu hỏi
        st.session_state.exam_qs = exam_qs
        st.session_state.exam_generated = True
        st.session_state.exam_submitted = False
        st.session_state.start_time = time.time() # Lưu thời điểm bắt đầu

    if not st.session_state.exam_submitted:
        st.warning("⚠️ Đề thi gồm 15 câu (Từ cơ bản đến Nâng cao). Con chú ý phân bổ thời gian nhé!")
        
        # CHÈN ĐỒNG HỒ ĐẾM NGƯỢC BẰNG JAVASCRIPT
        timer_html = """
        <div style="font-size: 24px; font-weight: bold; color: #ff4b4b; text-align: center; border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; background-color: #ffe6e6;">
            ⏱️ THỜI GIAN: <span id="time">20:00</span>
        </div>
        <script>
            var time_limit = 20 * 60; // 20 phút
            var timer = setInterval(function() {
                var minutes = parseInt(time_limit / 60, 10);
                var seconds = parseInt(time_limit % 60, 10);
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;
                document.getElementById('time').textContent = minutes + ":" + seconds;
                if (--time_limit < 0) {
                    clearInterval(timer);
                    document.getElementById('time').textContent = "HẾT GIỜ!";
                    document.getElementById('time').style.color = "red";
                }
            }, 1000);
        </script>
        """
        components.html(timer_html, height=70)

        with st.form("exam_form"):
            user_answers = {}
            for i, q in enumerate(st.session_state.exam_qs):
                st.markdown(f"**Câu {i+1} ({q['level']}):** {q['question']}")
                user_answers[q['id']] = st.text_input(f"Đáp án:", key=f"exam_{q['id']}")
                st.write("---")
            
            if st.form_submit_button("✅ NỘP BÀI"):
                # Tính thời gian làm bài
                time_taken = time.time() - st.session_state.start_time
                if time_taken > (20 * 60) + 10: # Trễ quá 10 giây coi như hết giờ
                    st.error("Con đã làm quá 20 phút rồi! Lần sau phải nhanh tay hơn nhé.")
                st.session_state.user_answers = user_answers
                st.session_state.time_taken = time_taken
                st.session_state.exam_submitted = True
                st.rerun()
    else:
        st.header("📊 KẾT QUẢ CUỘC THI")
        
        # Báo cáo thời gian
        mins = int(st.session_state.time_taken // 60)
        secs = int(st.session_state.time_taken % 60)
        st.info(f"⏱️ Con hoàn thành bài trong: **{mins} phút {secs} giây**")

        total_score = 0
        for q in st.session_state.exam_qs:
            if st.session_state.user_answers[q['id']].strip().lower() == q["answer"].strip().lower():
                total_score += 1
                
        st.write(f"### 🌟 Số câu đúng: {total_score} / {len(st.session_state.exam_qs)}")
        
        # Phân loại khen thưởng
        if total_score >= 12:
            st.success("🏆 Tuyệt đỉnh! Con hoàn toàn tự tin thi Nguyễn Tất Thành rồi!")
            st.balloons()
            st.snow()
        elif total_score >= 8:
            st.warning("👍 Rất tốt! Nhưng con thử kiểm tra lại các câu sai để rút kinh nghiệm nhé.")
        else:
            st.info("💪 Khó quá phải không? Không sao, mình về phần Ôn Tập rèn luyện thêm rồi quay lại phục thù nhé!")
        
        if st.button("🔄 Thi lại đề mới ngẫu nhiên"):
            st.session_state.exam_generated = False
            st.rerun()