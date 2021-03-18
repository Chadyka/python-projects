def xor(inp_1, inp_2):
    if bool(inp_1) != bool(inp_2):
        return True
    else:
        return False


def main():
    inp_1 = int(input("1st input of XOR: "))
    inp_2 = int(input("2nd input of XOR: "))
    print("XOR returned", xor(inp_1, inp_2))


if __name__ == "__main__":
    main()
