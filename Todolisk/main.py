from todo_manager import *

# แสดงเมนู
def show_menu():
    print("\n---- To-Do List ----")
    print("1. แสดงรายการ")
    print("2. เพิ่มรายการ")
    print("3. ลบรายการ")
    print("4. ออกจากโปรแกรม")
    print("--------------------")

# เมนูหลัก
def main():
    todos = read_todos()
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-4): ")
        if choice == '1':
            show_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            delete_todo(todos)
        elif choice == '4':
            print("ออกจากโปรแกรมแล้ว ขอบคุณที่ใช้งานค่ะ!")
            break
        else:
            print("กรุณาเลือกหมายเลข 1-4 เท่านั้น")

if __name__ == "__main__":
    main()
