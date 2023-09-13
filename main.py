import library


def main():
    a_random_list = ['Dracula', 1, 5.7, 'Carmilla']

    print(a_random_list)
    print(type(a_random_list[2]))
    a1 = a_random_list.pop()
    print(a1)
    a_random_list.append(11)
    print(a_random_list)

if __name__ == '__main__':
    main()
    library.greet() 

# ['Dracula', 1, 5.7, 'Carmilla']