import json
import random

questions = []
id_counter = 1

def add_q(typ, q_text, ans, lvl, explain, hint=""):
    global id_counter
    questions.append({
        "id": f"Q_{id_counter}",
        "type": typ,
        "question": q_text,
        "answer": str(ans),
        "level": lvl,
        "explain": explain,
        "hint": hint
    })
    id_counter += 1

# 1. Cộng Trừ
for _ in range(15):
    a, b = random.randint(100, 400), random.randint(100, 400)
    add_q("Cộng Trừ phạm vi 1000", f"Tính: {a} + {b} = ?", a + b, "Mức 1", f"Con nhớ đặt tính thẳng cột rồi cộng từ phải sang trái nhé. {a} + {b} = {a+b}.")
for _ in range(10):
    a, b = random.randint(150, 300), random.randint(50, 100)
    add_q("Cộng Trừ phạm vi 1000", f"Tìm x biết: x - {a} = {b}. Vậy x = ?", a + b, "Mức 2", f"Muốn tìm số bị trừ (x), ta lấy hiệu ({b}) cộng với số trừ ({a}). x = {b} + {a} = {a+b}.")
for _ in range(5):
    num = random.randint(10, 50)
    add_q("Cộng Trừ phạm vi 1000", f"Tổng của số bé nhất có 3 chữ số và số lớn nhất có 2 chữ số rồi trừ đi {num} là bao nhiêu?", 100 + 99 - num, "Mức 3", f"Số bé nhất có 3 chữ số là 100. Số lớn nhất có 2 chữ số là 99. Ta có: 100 + 99 - {num} = {100+99-num}.", "Con hãy tìm xem 'số bé nhất có 3 chữ số' và 'số lớn nhất có 2 chữ số' là số mấy trước nhé!")

# 2. Nhân Chia
for _ in range(15):
    a, b = random.randint(2, 5), random.randint(3, 10)
    if random.choice([True, False]):
        add_q("Bảng Nhân Chia (2,3,4,5)", f"Tính: {a} x {b} = ?", a * b, "Mức 1", f"Con nhẩm lại bảng nhân {a} nhé: {a} x {b} = {a*b}.")
    else:
        add_q("Bảng Nhân Chia (2,3,4,5)", f"Tính: {a * b} : {a} = ?", b, "Mức 1", f"Con nhẩm xem {a} nhân mấy bằng {a*b} nhé. {a} x {b} = {a*b} nên {a*b} : {a} = {b}.")
for _ in range(10):
    a, b = random.randint(2, 5), random.randint(4, 9)
    add_q("Bảng Nhân Chia (2,3,4,5)", f"Mỗi hộp có {a} chiếc bánh. Hỏi {b} hộp như thế có tất cả bao nhiêu chiếc?", a * b, "Mức 2", f"Có {b} hộp, mỗi hộp {a} chiếc, con dùng phép nhân nhé: {a} x {b} = {a*b}.")
for _ in range(5):
    a, b = random.randint(3, 5), random.randint(2, 4)
    add_q("Bảng Nhân Chia (2,3,4,5)", f"Có {a * b * 2} viên kẹo chia đều cho {a} bạn. Hỏi 2 bạn thì nhận được bao nhiêu viên kẹo?", b * 2 * 2, "Mức 3", f"Tính 1 bạn có: {a*b*2} : {a} = {b*2} viên. Sau đó tính 2 bạn có: {b*2} x 2 = {b*2*2} viên.", "Bài này có 2 bước. Bước 1: Tìm số kẹo của 1 bạn. Bước 2: Tìm số kẹo của 2 bạn.")

# 3. Đại lượng
for _ in range(15):
    a = random.randint(2, 9)
    add_q("Đại lượng & Thời gian", f"Đổi: {a} mét = ... xăng-ti-mét?", a * 100, "Mức 1", f"1 mét = 100 xăng-ti-mét. Vậy {a} mét = {a*100} xăng-ti-mét.")
for _ in range(10):
    a, b = random.randint(10, 40), random.randint(15, 30)
    add_q("Đại lượng & Thời gian", f"Cuộn xanh dài {a}cm, cuộn đỏ dài {b}cm. Cả hai cuộn dài bao nhiêu cm?", a + b, "Mức 2", f"Con cộng chiều dài 2 cuộn lại nhé: {a} + {b} = {a+b} cm.")
for _ in range(5):
    a = random.randint(1, 5)
    add_q("Đại lượng & Thời gian", f"Sợi dây dài {a}m {a*10}cm. Hỏi sợi dây đó dài tổng cộng bao nhiêu cm?", a*100 + a*10, "Mức 3", f"{a}m = {a*100}cm. Cộng thêm {a*10}cm nữa là {a*100 + a*10}cm.", "Con nhớ đổi đơn vị mét (m) sang xăng-ti-mét (cm) trước khi cộng nhé!")

# 4. Hình học
for _ in range(15):
    a, b, c = random.randint(10, 30), random.randint(10, 30), random.randint(10, 30)
    add_q("Hình học (Chu vi)", f"Chu vi hình tam giác có 3 cạnh là {a}cm, {b}cm, {c}cm.", a + b + c, "Mức 1", f"Chu vi tam giác là tổng 3 cạnh: {a} + {b} + {c} = {a+b+c} cm.")
for _ in range(10):
    a, b = random.randint(10, 20), random.randint(5, 9)
    add_q("Hình học (Chu vi)", f"Hình chữ nhật có chiều dài {a}cm, chiều rộng {b}cm. Tính chu vi.", (a + b) * 2, "Mức 2", f"Chu vi = (Dài + Rộng) x 2. Tức là: ({a} + {b}) x 2 = {(a+b)*2} cm.")
for _ in range(5):
    a = random.randint(10, 20)
    add_q("Hình học (Chu vi)", f"Hình vuông có chu vi là {a * 4}cm. Một cạnh dài bao nhiêu cm?", a, "Mức 3", f"Hình vuông có 4 cạnh bằng nhau, nên 1 cạnh = Chu vi : 4 = {a*4} : 4 = {a} cm.", "Chu vi hình vuông bằng một cạnh nhân với 4. Muốn tìm một cạnh, ta làm phép toán ngược lại nhé!")

# 5. Tư duy
for _ in range(15):
    days = random.randint(1, 3) * 7
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Hôm nay Thứ Hai, {days} ngày nữa là Thứ mấy? (Ghi: Thu Hai, Thu Ba...)", "Thu Hai", "Mức 1", f"Cứ sau 7 ngày (1 tuần) thì thứ sẽ lặp lại y hệt. {days} ngày là tròn tuần, nên vẫn là Thứ Hai.")
for _ in range(10):
    a, b, years = random.randint(8, 12), random.randint(4, 7), random.randint(3, 5)
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Hiện anh {a} tuổi, em {b} tuổi. {years} năm nữa tổng số tuổi là bao nhiêu?", (a + years) + (b + years), "Mức 2", f"{years} năm nữa, anh tăng {years} tuổi, em cũng tăng {years} tuổi. Tổng = {a+years} + {b+years} = {a+years+b+years}.", "Chú ý: Mỗi năm qua đi, ai cũng tăng thêm 1 tuổi nhé!")
for _ in range(5):
    a, b = random.randint(2, 5), random.randint(3, 6)
    add_q("Toán Tư Duy (Nền tảng NTT)", f"Đàn gà có {a * 10} con. Bán một nửa, mua thêm {b} con. Hiện có bao nhiêu con?", (a * 10 // 2) + b, "Mức 3", f"Bán 1 nửa còn: {a*10} : 2 = {a*10//2}. Mua thêm {b} con: {a*10//2} + {b} = {(a*10//2)+b}.", "Bước 1: Tính số gà còn lại sau khi bán một nửa. Bước 2: Tính số gà sau khi mua thêm.")

with open("data_toan_lop_2.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)