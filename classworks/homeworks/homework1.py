class Football:
    def __init__(self, name, pac, sho, pas, dri, defe, phy):
        self.name = name
        self.pac = pac
        self.sho = sho
        self.pas = pas
        self.dri = dri
        self.defe = defe
        self.phy = phy

    def ron_trophy(self):
        return f'{self.name} has 34 trophy'

    def messi_trophy(self):
        return f'{self.name} has 46 trophy'

    def neymar_trophy(self):
        return f'{self.name} has 30 trophy'

    def ronaldo_stats(self):
        return f'{self.name} has {self.pac} pac, {self.sho} sho, {self.pas} pas, {self.dri} dri, {self.defe} defe, {self.phy} phy'
    def messi_stats(self):
        return f'{self.name} has {self.pac} pac, {self.sho} sho, {self.pas} pas, {self.dri} dri, {self.defe} defe, {self.phy} phy'
    def neymar_stats(self):
        return f'{self.name} has {self.pac} pac, {self.sho} sho, {self.pas} pas, {self.dri} dri, {self.defe} defe, {self.phy} phy'

ronaldo = Football('Ronaldo', 96, 95, 87, 95, 53, 86)
messi = Football('Messi', 93, 89, 86, 97, 24, 58)
neymar = Football('Neymar', 90, 80, 85, 98, 30, 58)

print(ronaldo.ron_trophy())
print(messi.messi_trophy())
print(neymar.neymar_trophy())
print(ronaldo.ronaldo_stats())
print(messi.messi_stats())
print(neymar.neymar_stats())