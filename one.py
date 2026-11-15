import numpy as np
def get_marks():
    raw = input("Enter marks: ").split()
    marks = []

    for item in raw:
        try:
            num = float(item)
        except ValueError:
            print(f"invalid marks '{item}'. Enter numbers only.")
            return None

        if num <0 or num >100:
            print("Marks must be between 0 and 100.")
            return None

        marks.append(int(num) if num.is_integer() else num)

    return marks

def analyse_marks(marks):
    arr = np.array(marks)
    total = len(arr)

    mean = np.mean(arr)
    median = np.median(arr)
    highest = np.max(arr)
    lowest = np.min(arr)
    std_dev = np.std(arr)

    passed = np.sum(arr >=40)
    failed = total - passed
    pass_pct = (passed/total)* 100
    above_avg = np.sum(arr > mean)

    print(f"Mean: {mean:.2f} | Median: {median:.2f}")
    print(f"Max: {highest} | Min: {lowest} | std Dev: {std_dev:.2f}")
    print(f"Passed: {passed} of {total} | Failed: {failed} | Pass percentage: {pass_pct:.2f}%")
    print(f"Above average: {above_avg} students")

marks = get_marks()
if marks:
    analyse_marks(marks)