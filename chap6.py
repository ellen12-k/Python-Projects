# human 클래스를 만들고, 이 클래스를 상속받는 player클래스, npc 클래스, enemy클래스를 만들기
# human 클래스에는 이름, HP, MP 속성과 안녕하세요를 출력하는 meet 메소드가 있어야 하고
# player 클래스에는 AD 속성과 player 객체의 AD값 - enemy 객체의 DP값 만큼 enemy 객체의 HP를 감소시키는 att메소드가 있어야함
# enemy 클래스에는 DP 속성이 있어야함
# 그 다음에는 player, npc, enemy 객체를 자유롭게 1개씩 만들고
# 사용자에게 입력을 받아 1을 입력받으면 player과 npc의 meet 메소드가 실행되고
# 2를 입력받으면 att메소드가 실행되어 enemy 객체의 HP가 감소하도록 만들어주기
# enemy의 HP값이 0이 되면 게임이 종료되어야 함
# att 메소드는 반드시 2번이상 실행되어야 함.(공격력이 너무 높아서 한방에 끝나지 않게 하기)

class human:
    def __init__(self, name, HP, MP):
        self.name = name
        self.HP = HP
        self. MP = MP

    def meet(self):
        print("안녕하세요")

class player(human):
    AD = 30
    def att(self, enemy):
        enemy.HP = enemy.HP - (player.AD - enemy.DP)

class npc(human):
    def meet(self):
        print("안녕하세요")

class enemy(human):
    DP = 10
    HP = 100

while True:
    a = int(input("1또는 2를 입력하세요: "))
    if a == 1:
        player.meet(human)
        npc.meet(human)
        continue

    if a == 2:
        while True:
            player.att(player, enemy)
            print("공격! enemy의 남은 HP는")
            print(enemy.HP)
            if enemy.HP == 0:
                print("게임 종료")
                break
        break







