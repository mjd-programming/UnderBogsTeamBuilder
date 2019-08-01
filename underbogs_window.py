from tkinter import *
from tkinter import messagebox

import underlords_probability as up
from hero import *


class underlords_team_builder_window():
    def __init__(self):
        self.window = Tk()
        self.window.title('Underlords Team Builder')
        self.window.resizable(False, False)
        self.setup_window(self.window)

    def setup_window(self, window):
        Label(window, text='Unit Tier:').grid(row=0, column=0, sticky=W)
        Label(window, text='Total Units:').grid(row=1, column=0, sticky=W)
        Label(window, text='Total Tier Units:').grid(row=2, column=0, sticky=W)
        Label(window, text='Player Level:').grid(row=3, column=0, sticky=W)
        Label(window, text='Amount:').grid(row=4, column=0, sticky=W)
        Label(window, text='Probability:').grid(row=6, column=0, sticky=W)
        Label(window, text='Average Gold:').grid(row=7, column=0, sticky=W)

        probability_text_variable = StringVar()
        estimated_gold_text_variable = StringVar()
        hero_text_variable = StringVar()

        unit_tier_string_var = StringVar()
        total_units_string_var = StringVar()
        total_tier_units_string_var = StringVar()
        player_level_string_var = StringVar()
        amount_string_var = StringVar()

        Label(window, textvariable=probability_text_variable, width=5).grid(row=6, column=1, sticky=W)
        Label(window, textvariable=estimated_gold_text_variable).grid(row=7, column=1, sticky=W)
        Label(window, textvariable=hero_text_variable, width=69, height=5, wraplength=450).grid(row=0, column=2, rowspan=3, columnspan=6)

        Entry(window, width=3, textvariable=unit_tier_string_var).grid(row=0, column=1)
        Entry(window, width=3, textvariable=total_units_string_var).grid(row=1, column=1)
        Entry(window, width=3, textvariable=total_tier_units_string_var).grid(row=2, column=1)
        Entry(window, width=3, textvariable=player_level_string_var).grid(row=3, column=1)
        Entry(window, width=3, textvariable=amount_string_var).grid(row=4, column=1)

        hero_list = load_hero_data('underlords_heroes.txt')

        type_list = [
            'assassin', 'blood-bound', 'brawny', 'deadeye', 'demon',
            'demon hunter', 'dragon', 'druid', 'elusive', 'heartless',
            'human', 'hunter', 'inventor', 'knight', 'mage',
            'primordial', 'savage', 'scaled', 'scrappy', 'shaman',
            'troll', 'warlock', 'warrior'
        ]

        boolean_list = []
        check_box_list = []

        for i in range(len(type_list)):
            boolean_list.append(BooleanVar())
            check_box_list.append(Checkbutton(window, text=type_list[i], variable=boolean_list[i]))

        for i in range(4):
            for j in range(6):
                if i*6+j < len(check_box_list): check_box_list[i*6 + j].grid(row=4+i, column=2+j, sticky=W)

        def update_hero_query():
            temp_type_list = []
            hero_string = ''
            for i in range(len(boolean_list)):
                if boolean_list[i].get():
                    temp_type_list.append(type_list[i])
            string_list = get_string_list_from_heroes(get_list_with_types(hero_list, temp_type_list))
            for s in string_list:
                hero_string += s
                if s is not string_list[len(string_list)-1]: hero_string += ', '
            hero_text_variable.set(hero_string)

        def process_entries():
            try:
                unit_tier_value = int(unit_tier_string_var.get())
                total_units_value = int(total_units_string_var.get())
                total_tier_units_value = int(total_tier_units_string_var.get())
                player_level_value = int(player_level_string_var.get())
                amount_value = int(amount_string_var.get())
            except ValueError:
                messagebox.showerror('Invalid Entries', 'You must enter valid entries.')
                unit_tier_string_var.set('')
                total_units_string_var.set('')
                total_tier_units_string_var.set('')
                player_level_string_var.set('')
                amount_string_var.set('')
            else:
                prob_string = float(100* up.get_chance_appear_shop(
                    amount_value, player_level_value, unit_tier_value, total_units_value, total_tier_units_value))
                gold_string = up.get_estimated_gold(prob_string)
                if gold_string % 2 != 0: gold_string += 1
                probability_text_variable.set('~{0:.2f}%'.format(prob_string))
                estimated_gold_text_variable.set('~{0:.0f}'.format(gold_string))

        Button(window, text='Update Heroes', width=13, command=update_hero_query).grid(row=7, column=7, padx=2)
        Button(window, text='Process', width=16, command=process_entries).grid(row=5, column=0, columnspan=2, padx=2)

        window.mainloop()