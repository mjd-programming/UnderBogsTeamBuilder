class hero:
    def __init__(self, name, cost, types):
        self.name = name
        self.cost = cost
        self.types = types

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_types(self):
        return self.types

def load_hero_data(f_name):
    hero_list = []
    f = open(f_name, 'r')
    c_line = f.readline()
    while c_line:
        h_args = [x.strip() for x in c_line.split(',')]
        types = [x.strip() for x in h_args[2:]]
        hero_list.append(hero(h_args[0].title(), h_args[1], types))
        c_line = f.readline()
    return hero_list

def get_list_with_types(o_list, types):
    n_list = []
    for h in o_list:
        c_hero = h
        for c_type in c_hero.get_types():
            if c_type in types and not (c_hero in n_list):
                n_list.append(c_hero)
    return n_list

def get_string_list_from_heroes(h_list):
    r_list = []
    for current_hero in h_list:
        r_list.append(current_hero.get_name())
    return r_list