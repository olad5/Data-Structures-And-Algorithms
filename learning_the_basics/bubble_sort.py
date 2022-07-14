
def bubble_list(my_list):
    # moving backward through the list
    for i in range(len(my_list) - 1, 0, -1 ):
        # moving forward through the list
        for j in range(i):
            if my_list[j] > my_list[j+1] :
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


if __name__ == "__main__":
    print(bubble_list([4,2,6,5,1,3]))
