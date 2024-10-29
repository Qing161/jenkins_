class Person:
    def __init__(self, ID=0, name='', gender=0, birth_day=0, work_day=0, phone_number=0,
                 education_background='', address='', job=''):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.birth_day = birth_day
        self.work_day = work_day
        self.phone_number = phone_number
        self.education_background = education_background
        self.address = address
        self.job = job

def print_people(people):
    print("\033[0;36m")
    print("ID    Name   Gender  Birth Day\tWork Day  Phone Number\tEducation Background\tAddress\tJob")
    print("\033[0m")
    for p in people:
        print(f"{p.ID:<5}{p.name:<8}{p.gender:<8}{p.birth_day:<11}{p.work_day:<10}{p.phone_number:<16}{p.education_background:<20}{p.address:<10}{p.job}")

def create_people(n):
    people = []
    for i in range(n):
        print(f"\033[0;33m第{i+1}个人的数据:\033[0m")
        ID = int(input("-ID: "))
        name = input("-姓名: ")
        gender = int(input("-性别: "))
        birth_day = int(input("-生日: "))
        work_day = int(input("-工作日: "))
        phone_number = int(input("-电话号码: "))
        education_background = input("-教育经历: ")
        address = input("-地址: ")
        job = input("-职业: ")
        people.append(Person(ID, name, gender, birth_day, work_day, phone_number, education_background, address, job))
    return people

def delete_person(people, n, d):
    index_to_delete = next((i for i, p in enumerate(people) if p.ID == d), None)
    if index_to_delete is not None:
        del people[index_to_delete]
        return True
    return False

def sort_by_name(people):
    people.sort(key=lambda p: p.name)

def search_person(people, id):
    found = [p for p in people if p.ID == id]
    if found:
        print_people(found)
    else:
        print("没有此ID!")

def sort_by_gender(people):
    people.sort(key=lambda p: p.gender)

def sort_by_id(people):
    people.sort(key=lambda p: p.ID)

def sort_by_birth_day(people):
    people.sort(key=lambda p: p.birth_day)

def update_person(people, id):
    for p in people:
        if p.ID == id:
            while True:
                print("1.ID 2.名字 3.性别 4.生日 5.工作日 6.电话号码 7.教育经历 8.地址 9.职业 0.修改完成")
                key = int(input("*修改哪些数据: "))
                if key == 1:
                    p.ID = int(input("-输入新ID: "))
                elif key == 2:
                    p.name = input("-输入新名字: ")
                elif key == 3:
                    p.gender = int(input("-输入新性别: "))
                elif key == 4:
                    p.birth_day = int(input("-输入新生日: "))
                elif key == 5:
                    p.work_day = int(input("-输入新工作日: "))
                elif key == 6:
                    p.phone_number = int(input("-输入新电话号码: "))
                elif key == 7:
                    p.education_background = input("-输入新教育经历: ")
                elif key == 8:
                    p.address = input("-输入新地址: ")
                elif key == 9:
                    p.job = input("-输入新职业: ")
                elif key == 0:
                    return
                else:
                    print("-重新输入")

def add_person(people):
    ID = int(input("-ID: "))
    name = input("-姓名: ")
    gender = int(input("-性别: "))
    birth_day = int(input("-生日: "))
    work_day = int(input("-工作日: "))
    phone_number = int(input("-电话号码: "))
    education_background = input("-教育经历: ")
    address = input("-地址: ")
    job = input("-职业: ")
    people.append(Person(ID, name, gender, birth_day, work_day, phone_number, education_background, address, job))

def write_to_file(people, filename="output.txt"):
    with open(filename, "w") as file:
        file.write("ID\tName\tGender\tBirth Day\tWork Day\tPhone Number\tEducation Background\tAddress\tJob\n")
        for p in people:
            file.write(f"{p.ID}\t{p.name}\t{p.gender}\t{p.birth_day}\t{p.work_day}\t{p.phone_number}\t{p.education_background}\t{p.address}\t{p.job}\n")

def find_by_job(people):
    job = input("要查找的职业: ")
    matching_people = [p for p in people if p.job == job]
    if matching_people:
        print("\033[0;36m")
        print("ID    Name   Gender  Birth Day\tWork Day  Phone Number\tEducation Background\tAddress\tJob")
        print("\033[0m")
        print_people(matching_people)
    else:
        print("没有找到匹配的职业!")

def main():
    n = int(input("职工数量："))
    people = create_people(n)
    print("\033[0;32m")
    print("************************菜单**************************")
    print("\033[0m")
    print("1. 输出所有数据")
    print("2. 查找ID")
    print("3. 查找职业")
    print("4. 按照ID排序")
    print("5. 按照名字排序")
    print("6. 按照生日排序")
    print("7. 男女分开")
    print("8. 修改数据")
    print("9. 添加数据")
    print("10. 输出在文件中")
    print("11. 删除数据")
    print("12. 退出程序")
    print("\033[0;32m")
    print("******************************************************")
    print("\033[0m")

    while True:

        key = int(input("\033[0;33m@输入操作：\033[0m"))
        if key == 1:
            print_people(people)
        elif key == 2:
            id = int(input("查找的人的ID: "))
            search_person(people, id)
        elif key == 3:
            find_by_job(people)
        elif key == 4:
            sort_by_id(people)
            print("排序后:")
            print_people(people)
        elif key == 5:
            sort_by_name(people)
            print("排序后:")
            print_people(people)
        elif key == 6:
            sort_by_birth_day(people)
            print("排序后:")
            print_people(people)
        elif key == 7:
            sort_by_gender(people)
            print("排序后:")
            print_people(people)
        elif key == 8:
            id = int(input("修改谁的数据: "))
            update_person(people, id)
        elif key == 9:
            add_person(people)
        elif key == 10:
            write_to_file(people)
        elif key == 11:
            id = int(input("删除的人的ID: "))
            if delete_person(people, len(people), id):
                print("成功删除!")
            else:
                print("删除失败")
        elif key == 12:
            break
        else:
            print("重新输入!")

if __name__ == "__main__":
    main()