import os

FILE_NAME = "todo.txt"

# อ่านข้อมูลจากไฟล์
def read_todos():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        todos = [line.strip() for line in file.readlines()]
    return todos

# เขียนข้อมูลลงไฟล์
def write_todos(todos):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for todo in todos:
            file.write(todo + '\n')

# แสดงรายการ To-Do
def show_todos(todos):
    if not todos:
        print("ไม่มีรายการใน To-Do List")
    else:
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")

# เพิ่มรายการ
def add_todo(todos):
    new_todo = input("กรอกรายการใหม่: ")
    todos.append(new_todo)
    write_todos(todos)
    print(f"เพิ่ม '{new_todo}' เรียบร้อยแล้ว")

# ลบรายการ
def delete_todo(todos):
    show_todos(todos)
    try:
        index = int(input("กรอกหมายเลขที่ต้องการลบ: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            write_todos(todos)
            print(f"ลบ '{removed}' เรียบร้อยแล้ว")
        else:
            print("หมายเลขไม่ถูกต้อง")
    except ValueError:
        print("กรุณากรอกตัวเลข")
