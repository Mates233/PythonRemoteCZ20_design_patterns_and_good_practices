## Sumár
Tento repozitář je součástí kurzu pythonu, který pořádá SDA.

Modul, kterého se toto úložiště týká, je Good Practices and Design Patterns v Pythonu.

Související materiály lze nalézt v platformě Journey, konkrétně prezentaci, kterou procházíme během hodiny, 
doprovodné poznámky k probírané látce a další cvičení pro ty, kteří hledají další výzvu.

**Na první přednášce (12.5.2024) jsme se zabývali**
- pokyny pro styl kódování
- osvědčené postupy kódování odvozené ze Zen of Python
- formátování kódu, analýza kódu pomocí programu Pylint 
- zásady SOLID

**Další zdroje:**
- Zásady Zen of Python: https://cs.wikipedia.org/wiki/Filozofie_Pythonu
- Pylint návod k použití pluginu: https://github.com/leinardi/pylint-pycharm/blob/master/README.md
- Průvodce Pylint pro použití jako externí nástroj: https://kirankoduru.github.io/python/pylint-with-pycharm.html#1-locate-your-pylint-installation
- Black setup: https://github.com/psf/black
- Ako na pre-commit hook s Flake8 & Black - vřele doporučujem používat na větších projektech, 
jako je závěrečný projekt tohoto kurzu: https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
- Skvělý článek o atributech tříd : https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide


**Vytvárecí návrhové vzory**
- Singleton
- Builder
- Factory Method
- Abstract Factory
- Prototype

Na druhe přednášce (18.5.2024) jsme se zabývali:

**Strukturální návrhové vzory**
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

Na třetí přednášce (19.5.2024) jsme se zabývali:

**Návrhové vzory chování**
- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

Další zdroje:
- Decorator vs Decorator pattern: https://betterprogramming.pub/decorator-pattern-and-python-decorators-b0b573f4c1ce
- Free alternativa k GitHub Copilot pluginu: https://plugins.jetbrains.com/plugin/20540-codeium-ai-autocomplete-and-chat-for-python-js-java-go--

### Úkoly:
Úkoly 1,2,3,4 by měly být plně vyřešeny, v úkolu 5 zbývá dokončit metodu update.

Bonusový úkol je trochu náročnější pro ty, kteří chtějí vyzkoušet něco navíc, je zo série 100 days of code,
kde sou i další zajímavé úkoly. Vybral jsem úkol Coffee Machine, který se týka OOP a dá se řešit pomocí návrhového
vzoru State.
https://github.com/LeeRenJie/100-days-of-code-in-python/blob/main/Day016-OOP-Coffee_Machine.py
