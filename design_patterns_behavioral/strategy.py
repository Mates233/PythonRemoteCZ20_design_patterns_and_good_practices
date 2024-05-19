"""
Strategie je návrhový vzor, který vám řekne o různých způsobech provádění stejné činnosti.
Tuto akci chceme vybrat v runtime. Protože máme různé způsoby provádění určité operace,
můžeme mluvit o skupině algoritmů, které chceme používat zaměnitelně (v závislosti na konfiguraci aplikace nebo volbě uživatele).

Design
Abychom mohli použít vzor Strategy, musíme definovat následující:

společné rozhraní pro skupinu algoritmů provádějících určitou operaci
několik implementací výše uvedeného rozhraní, tj. skupina společných algoritmů
třída, která zvolí vhodnou strategii na základě kontextu (tj. konfigurace nebo jiných externích faktorů)


Příklad se skládá z následujících částí:

rozhraní SpacesModificationStrategy, které je společnou součástí skupiny algoritmů,
 které umožňují upravovat mezery ve vstupním textu.
tři implementace rozhraní SpacesModificationStrategy:
DoubleSpacesStrategy - nahradí každou mezeru dvěma
RemoveSpacesStrategy - odstraní všechny mezery
ReplaceWithUnderscoreStrategy - nahradí všechny mezeru znakem _
SpacesModificationStrategyProvider - umožňuje vám vybrat správnou strategii podle typu
ukázkové použití vzoru
"""

class SpacesModificationStrategy:
    def modify(self, inp):
        pass


class DoubleSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '  ')


class RemoveSpacesStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '')


class ReplaceWithUnderscoreStrategy(SpacesModificationStrategy):
    def modify(self, inp):
        return inp.replace(' ', '_')


class SpaceModificationStrategyProvider:
    def get(self, strategy_type):
        if strategy_type == 'DOUBLE':
            return DoubleSpacesStrategy()
        elif strategy_type == 'REMOVE':
            return RemoveSpacesStrategy()
        elif strategy_type == 'REPLACE':
            return ReplaceWithUnderscoreStrategy()


def main():
    strategy_type = input("Choose a strategy [DOUBLE|REMOVE|REPLACE]: ")
    inp = "hello from SDA knowledge base!"

    strategy = SpaceModificationStrategyProvider().get(strategy_type)
    output = strategy.modify(inp)

    print(output)


if __name__ == '__main__':
    main()
