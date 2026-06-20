print("===================================")
print("      SMART DATA ANALYZER TOOL     ")
print("===================================")

data = []

print("Enter numbers (type 'stop' to finish):")

n = input()

while n != "stop":
    data.append(int(n))
    n = input()
def analyze(data):

    if len(data) == 0:
        print("No data entered")
        return

    total = 0
    even_sum = 0
    odd_sum = 0
    even_count = 0
    odd_count = 0

    for x in data:
        total += x

        if x % 2 == 0:
            even_sum += x
            even_count += 1
        else:
            odd_sum += x
            odd_count += 1

    print("\n📊 REPORT")
    print("Total:", total)
    print("Count:", len(data))
    print("Average:", total / len(data))
    print("Max:", max(data))
    print("Min:", min(data))
    print("Even count:", even_count)
    print("Odd count:", odd_count)
analyze(data)

print("===================================")
print("        ANALYSIS COMPLETE          ")
print("===================================")