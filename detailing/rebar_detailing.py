def select_bar_diameter(Ast):

    bars = [12,16,20,25]

    for dia in bars:

        area = 3.14*(dia**2)/4

        n = math.ceil(Ast/area)

        if n <= 6:
            return dia,n
