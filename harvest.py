############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for each_melon in melon_types:
        print "{name} pairs with".format(name=each_melon.name)
        for i in range(len(each_melon.pairings)):
            print "- {pairing}".format(pairing=each_melon.pairings[i])


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    #what is the attribute passed to key (code)? each_melon[1:]

    for each_melon in melon_types:
        melon_dict[each_melon.code] = each_melon


    return melon_dict

    # melon_dict[each_melon.code] = each_melon[1:]
        # if each_melon.code in melon_dict:
        #     melon_dict[each_melon.code].append(each_melon[])
        # else:
        #     melon_dict[each_melon.code] = []
        #     melon_dict[each_melon.code].append(sth)

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, rating, color_rating, harvested_where, harvested_by):

        self.melon_type = melon_type
        self.rating = rating
        self.color_rating = color_rating
        self.harvested_where = harvested_where
        self.harvested_by = harvested_by

    def is_sellable(self):
        return (self.rating > 5 and self.color_rating > 5 and self.harvested_where != "Field 3")



def make_melons(melon_types):
    """Returns a list of Melon objects."""




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



