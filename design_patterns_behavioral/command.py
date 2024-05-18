"""
Účelem vzoru chování Command je oddělit objekty, které odesílají požadavky, od objektů, které přijímají jejich výsledky.
Umožňuje to zavedením objektu představujícího příkaz, který takový proces provádí.
Volitelně může být příkaz také schopen vrátit zpět výsledek takového procesu.

Zabalením provádění procesu do samostatného objektu zachováme pravidla SOLID odstraněním potenciální silné vazby
mezi odesílatelem a příjemcem výsledku požadavku.

Design a příklad
Hlavním prvkem, který musíme vytvořit, je společný objekt představující provádění procesu.
Volitelně může být možné zrušit provedení příkazu.

Objekty potřebné k provedení příkazu nejčastěji získává v konstruktoru implementace.

1. Command Interface: Deklaruje rozhraní pro provedení operace.
2. Concrete Command: Implementuje rozhraní příkazu a definuje vazbu mezi přijímačem a akcí.
3. Receiver: Příkaz, který je určen k provedení příkazu: Příkaz: Ví, jak provést operace spojené s provedením požadavku.
4. Invoker: Vyvolávač: Vyvolává příkaz: Žádá příkaz o provedení požadavku.
5. Client: Vyplní příkaz k provedení příkazu: Vytvoří objekt ConcreteCommand a nastaví jeho příjemce.
"""