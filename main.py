from magic_list import MagicList
from person import Person


def run_test():
    a = MagicList()
    print("a = MagicList()")
    a[0] = 5
    a[1] = 6
    print("a[0] = 5")
    print("print(a)")
    print(a)

def run_type_test():
    a = MagicList(cls_type=Person)
    print("a = MagicList(cls_type=Person)")
    #a[0].age = 5
    a[1].age = 6
    print("a[0].age = 5")
    print("print(a)")
    print(a)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #run_test()
    run_type_test()
