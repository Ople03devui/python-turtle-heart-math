import math
from turtle import*

def heart1(m):
    return 15 * math.sin(m)**3

def heart2(m):
    return 12 * math.cos(m) - 5 * math.cos(2 * m) - 2 * math.cos(3 * m) - math.cos(4 * m)

speed(0.1)  # ตั้งค่าความเร็วเป็น 0 เพื่อให้วาดเร็วที่สุด
bgcolor("white")
penup()  # ยกปากกาขึ้นเพื่อไม่ให้เกิดเส้นก่อนวาด
goto(0, 72)  # เริ่มต้นที่จุดกึ่งกลาง
pendown()  # วางปากกาลงเพื่อเริ่มวาด

for i in range(750):
    x = heart1(i) * 18
    y = heart2(i) * 18
    goto(x, y)
    color("red")  # กำหนดสีเป็นสีแดง

#goto(0, 0) # กลับมาที่จุดเริ่มต้นเมื่อวาดเสร็จ (อาจไม่จำเป็นสำหรับการวาดรูปหัวใจ)
done()