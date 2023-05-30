import random
class Casino:
    def __init__(self,numOfReels,win):
        self.reels=[[x for x in range(10)]]*numOfReels
        self.wins=win
    def spin(self):
        destiny=''
        for reel in self.reels:
            destiny+=str(random.choice(reel))
        return destiny

    def simulate(self,spins,pot,bet):
        self.spincount,self.pot,self.bet=spins,pot,bet
        jackpots=0
        startingPot=pot
        totalPaid=0
        winningSpins=0

        for i in range(self.spincount):
            pot+=bet
            current= self.spin()
            hits=[item for item in self.wins.keys() if item in current ]
            if hits:
                multiplier=self.wins[max(hits)]
                payout=(bet*multiplier)
                pot-=payout
                totalPaid+=payout
                winningSpins+=1
                if multiplier==self.wins[max(self.wins.keys())]:
                    jackpots+=1

        profit=pot-startingPot
        if profit>0:
            profit=f"{float(profit):,.2f} Ft"
            return f"{winningSpins}/{spins} nyert. A Sárkány {profit}-ot evett ham ham."

        if profit<0:
            profit = f"-${float(profit):,.2f}"
            return f"{winningSpins} wins/{spins} spins. Profit is zero"
slot=Casino(3,{"777":50,"123":10})

print(slot.simulate(1000,20000,50))

