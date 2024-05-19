"""
Předpokládejme:

v terminálu v shellu bash spustíme příkaz ls -ltr | grep -i sda
v konzoli python spustíme příkaz 3 ** 3 + 1
v konzoli jshell spustíme příkaz Math.abs(Math.pow(2, 3)).
Každý z výše uvedených příkladů bere jako vstup nějakou informaci, obvykle ve formě řetězce.
Poté jsou tyto znaky interpretovány určitým dohodnutým způsobem (tj. v závislosti na smlouvě a možnostech technologie)
a poskytují konkrétní výsledek. Toto chování popisuje použití vzoru interpret.

Design
Abychom mohli použít vzor, potřebujeme následující prvky:

společné rozhraní, které má metodu pro interpretaci určitého objektu. Tento objekt často nazýváme kontext ( context)
implementace rozhraní, která mohou interpretovat kontext různými způsoby
"""