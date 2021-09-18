#hackerrank2.py
if __name__ == '__main__':
    n = int(input())
    sonuc=0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        sonuc += i
    average = sonuc / len(student_marks[query_name])
    print("%.2f" %average)