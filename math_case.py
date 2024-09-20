data = "delete_variable"


match data:
    case "check_type":
        print(type(data))

    case "delete_variable":
        del data

    case _:
        print(data)


for _ in range(10):
    print(123)