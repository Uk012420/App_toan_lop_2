import json
import random

questions = []
id_counter = 1

def add_q(typ, q_text, ans, lvl):
    global id_counter
    questions.append({
        "id": f"Q_{id_counter}",
        "type": typ,
        "question": q_text,
        "answer": str(ans),
        "level": lvl
    })
    id_counter += 1

# 1. DẠNG: Cộng Trừ phạm vi 1000
for _ in range(15): # Mức 1
    a, b = random.randint(100, 400), random.randint(100, 400)
    add_q("Cộng Trừ phạm vi 1000", f"Tính: {a} + {b} = ?", a + b, "Mức 1")
for _ in range(10): # Mức 2
    a, b = random.randint(150, 300), random.randint(50, 100)
    add_q("Cộng Trừ phạm vi 1000", f"Tìm x biết: x - {a} = {b}. Vậy x = ?", a + b, "Mức 2")
for _ in range(5):  # Mức 3
    num = random.randint(10, 50)
    add_q("Cộng Trừ phạm vi 1000", f"Tổng của số bé nhất có 3 chữ số (100) và số lớn nhất có 2 chữ số (99) rồi trừ đi {num} là bao nhiêu?", 100 + 99 - num, "Mức 3")

# 2. DẠNG: Bảng Nhân Chia (2,3,4,5)
for _ in range(15):
    a, b = random.randint(2, 5), random.randint(3, 10)
    if random.choice([True, False]):
        add_q("Bảng Nhân Chia (2,3,4,5)", f"Tính: {a} x {b} = ?", a * b, "Mức 1")
    else:
        add_q("Bảng Nhân Chia (2,3,4,5)", f"Tính: {a * b} : {a} = ?", b, "Mức 1")
for _ in range(10):
    a, b = random.randint(2, 5), random.randint(4, 9)
    add_q("Bảng Nhân Chia (2,3,4,5)", f"Mỗi hộp bánh có {a} chiếc bánh. Hỏi {b} hộp bánh như thế có tất cả bao nhiêu chiếc?", a * b, "Mức 2")
for _ in range(5):
    a, b = random.randint(3, 5), random.randint(2, 4)
    add_q("Bảng Nhân Chia (2,3,4,5)", f"Cô giáo có {a * b * 2} viên kẹo chia đều cho {a} bạn. Hỏi 2 bạn thì nhận được tổng cộng bao nhiêu viên kẹo?", b * 2 * 2, "Mức 3")

# 3. DẠNG: Đại lượng & Thời gian
for _ in range(15):
    a = random.randint(2, 9)
    add_q("Đại lượng & Thời gian", f"Đổi: {a} mét = ... xăng-ti-mét?", a * 100, "Mức 1")
for _ in range(10):
    a, b = random.randint(10, 40), random.randint(15, 30)
    add_q("Đại lượng & Thời gian", f"Cuộn dây xanh dài {a}cm, cuộn dây đỏ dài {b}cm. Cả hai cuộn dài bao nhiêu cm?", a + b, "Mức 2")
for _ in range(5):
    a = random.randint(1, 5)
    add_q("Đại lượng & Thời gian", f"Một sợi dây dài {a}m {a*10}cm. Hỏi sợi dây đó dài tổng cộng bao nhiêu cm?", a*100 + a*10, "Mức 3")

# 4. DẠNG: Hình học (Chu vi)
for _ in range(15):
    a, b, c = random.randint(10, 30), random.randint(10, 30), random.randint(10, 30)
    add_q("Hình học (Chu vi)", f"Tính chu vi hình tam giác có 3 cạnh lần lượt là {a}cm, {b}cm, {c}cm.", a + b + c, "Mức 1")
for _ in range(10):
    a, b = random.randint(10, 20), random.randint(5, 9)
    add_q("Hình học (Chu vi)", f"Một hình chữ nhật có chiều dài {a}cm, chiều rộng {b}cm. Tính chu vi hình chữ nhật đó.", (a + b) * 2, "Mức 2")
for _ in range(5):
    a = random.randint(10, 20)
    add_q("Hình học (Chu vi)", f"Một hình vuông có chu vi là {a * 4}cm. Hỏi một cạnh của hình vuông dài bao nhiêu cm?", a, "Mức 3")

# 5. DẠNG: Toán Tư Duy (Nền tảng NTT)
for _ in range(15):
    days = random.randint(1, 3) * 7
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Hôm nay là Thứ Hai, hỏi {days} ngày nữa là Thứ mấy? (Ghi đáp án không dấu: Thu Hai, Thu Ba...)", "Thu Hai", "Mức 1")
for _ in range(10):
    a, b, years = random.randint(8, 12), random.randint(4, 7), random.randint(3, 5)
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Hiện nay anh {a} tuổi, em {b} tuổi. Hỏi {years} năm nữa tổng số tuổi của hai anh em là bao nhiêu?", (a + years) + (b + years), "Mức 2")
for _ in range(5):
    a, b = random.randint(2, 5), random.randint(3, 6)
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Đàn gà nhà bác Năm có {a * 10} con. Bác bán đi một nửa, rồi lại mua thêm {b} con. Hỏi hiện tại bác có bao nhiêu con gà?", (a * 10 // 2) + b, "Mức 3")

# Lưu file JSON
with open("data_toan_lop_2.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
print(f"Đã tạo thành công {len(questions)} câu hỏi ĐỘC LẬP vào file data_toan_lop_2.json!")