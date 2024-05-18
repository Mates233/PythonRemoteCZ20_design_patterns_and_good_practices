"""
„Řetěz odpovědnosti“ je vzor, který popisuje, jak vytvořit řetězec objektů,
které jsou schopny zpracovat konkrétní požadavek.
Takový požadavek obvykle odešle klient a poté přechází k prvnímu prvku řetězce.
Pokud je první prvek schopen správně zpracovat požadavek, řetězec opustí, což také neznamená žádný "kontakt" se
zbytkem řetězce (často nazývaným "handlery"). Na druhou stranu, pokud prvek řetězce není schopen požadavek zpracovat,
pak – pokud nejde o poslední prvek řetězce – se snaží přesunout odpovědnost za jeho vyřízení na další prvek.
"""


