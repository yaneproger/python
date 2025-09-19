
# reader = open('050925-yandex-task.txt', 'r')
# a, b = [int(n) for n in reader.readline().split(" ")]
# reader.close()

# writer = open('output.txt', 'w')
# writer.write("%d" % (a+b))
# writer.close()


num1, num2 = (open("050925-yandex-task.txt", "r").read()).split()
resu = open("output.txt", "w")
resu.write(str(int(num1) + int(num2)))
