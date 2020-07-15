def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool!")

def swing(*kids):
    for kid in kids:
        print(f"{kid} is playing swing!")


def slide(*kids):
    for kid in kids:
        print(f"{kid} is playing slide!")


def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} is hidding!")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")