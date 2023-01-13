def main():
    option_selector = input("Hi, Welcome to Binary Networks©®™\nIf you have an account, Go for login else create\n").lower()
    if "create" in option_selector:
        import part1
    elif "login" in option_selector:
        import part2
    else:
        print("Invalid Selection")
        main()

main()
