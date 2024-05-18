"""
Composite je návrhový vzor, který lze použít, pokud jsme schopni reprezentovat objekty jako stromy.
Takový strom se skládá z uzlů, které jsou z pohledu uživatele samostatnými objekty.

Abychom mohli použít kompozit, potřebujeme následující prvky:

běžné rozhraní nebo základní třída pro objekty ve stromu se často nazývá component (komponenta).
třída představující jeden objekt na větvi (což je component). Takový objekt,
který neobsahuje žádné potomky, často nazývané list (leaf)
složená třída, která je také component, obsahující množinu listů (leafs).
"""


