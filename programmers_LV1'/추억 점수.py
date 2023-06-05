def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = sum(yearning[name.index(person)] for person in i if person in name)
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"], ["kein", "deny", "may"], ["kon", "coni"]]))