class Foo: # the simplest definition
    pass

class GreenTea:
    def __init__(self, name): # self must go first
        self._name = name;    # _name is intended to be "private"
    def get_name(my_class):   # "my_class" is OK, "self" is a convention
        return "delicious greeny " + my_class._name;


class Teapot:
    ''' Fancy teapots '''

    essential = False; # static attribute

    def __init__(self, tea):
        self.__temperature = 20; # name is intended to be "unaccessable"
        self._tea = tea; # composition of objects
        self._cups = 5;

    def heat_up(self, delta = 10):
        if delta < 0:
            raise ValueError;
        self.__temperature += delta; # attributes must be accessed via self

    def serve(self, cups):
        self.heat_up(); # side effect
        if self._cups < cups:
            return "Someone drinks to match";
        else:
            self._cups -= cups;
            return "Your tea, please";

    def __str__(self): # conversion to string
        return "Teapot with {} ({}C) and {} cups".format(
            self._tea.get_name(), self.__temperature, self._cups);

    def is_essential():
        return Teapot.essential;

if __name__ == "__main__":
    fav_tea = GreenTea("Gunpowder");

    teapot1 = Teapot(fav_tea);
    teapot2 = Teapot(GreenTea("Noname"));
    teapot3 = teapot1; # aliasing vs copying

    teapot1.heat_up();
    print("Serve Teapot 3:" + teapot3.serve(3));
    print("Status:");
    print(("\t{}\n" * 3).format(teapot1, str(teapot3), teapot2));
    # NB:
    #    teapot 3 is alias for teapot 1
    #    teapots has different value

    print("-" * 10);
    print("_cups access: ", teapot3._cups); # UNACCEPTABLE! (c)
    # teapot3.__temperature; -- Error: name mangling

    # UNACCEPTABLE!
    print("__temperatue: ", teapot3._Teapot__temperature); # name unmangling

    teapot3.color = "silver"; # ad hoc attribute addition
    print("Color: ", teapot3.color);
    # teapot2.color -- Error: attr addition is "object-wide"

    # Welcome exceptions
    try:
        teapot2.heat_up(-10);
    except ValueError as error:
        print("Expected ValueError was thrown");
    else:
        print("Error: no error");

    # Lemongrab hates me even more
    print("Alternative Call Format: tempr before --", \
              teapot2._Teapot__temperature, end="; ");
    Teapot.heat_up(teapot2, 10);
    print("tempr before --", teapot2._Teapot__temperature);

    # teapot2.heat_up(teapot3); -- Error: self is substituted implicitly

    teapot3.get_tempr = lambda self: self.__temperature;
    # teapot3.get_tempr(); # error: param must be specified
    # teapot2.get_tempr(teapot2); # error: no member get_tempr in Teapot
    # teapot3.get_tempr(teapot3); # error: name mangling


    def get_cups(self):
        return self._cups;

    Teapot.get_available_cups = get_cups;
    print("T1 cups -- {}; T2 cups -- {}".format(\
            Teapot.get_available_cups(teapot1),\
            Teapot.get_available_cups(teapot2)));

    # static stuff
    print("Static essential:", teapot1.essential, Teapot.is_essential());
    # teapot1.is_essential() # error
    Teapot.essential = True;
    print("Static essential changed:", teapot1.essential, teapot2.essential);
    teapot1.essential = False; # actually local attr defn
    print("Static essential ?!:", teapot1.essential, teapot2.essential);

################################################################################

# Case study iterator

class ReversedList:
    def __init__(self, host):
        self.host = host;

    def __iter__(self):
        self.ind = len(self.host);
        return self;

    def __next__(self):
        if self.ind == 0:
            raise StopIteration;
        self.ind -= 1;
        return self.host[self.ind];

if __name__ == "__main__":
    print("-" * 3 + "ReversedList" + "-" * 3);
    rev_list = ReversedList(list(range(10)));
    res = [print(el, end="") for el in rev_list]; # welcome list comprehension
    print();
    print(res); # print return "nothing" --> None
