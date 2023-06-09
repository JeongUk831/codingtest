'''
문제 설명
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = ""
    while n > 0:
        n, remainder = divmod(n,3)
        answer += str(remainder)
        
    answer = int(answer, 3)
    return answer

print(solution(45))
print(solution(125))