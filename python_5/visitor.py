# Pattern visitor: add functionality to class hierarchy

class Character:
    def __init__(self, favoriteWeapon):
        self.__fv = favoriteWeapon;
    def favWeapon(self):
        return self.__fv;
    def visit(self, visitor):
        visitor.accept(self);

class Elf(Character):
    def __init__(self):
        super().__init__("bow");
        
class Orc(Character):
    def __init__(self):
        super().__init__("axe");

class Human(Character):
    def __init__(self):
        super().__init__("sword");

# What pattern do you smell here? (C******t)
class Lord(Character):
    def __init__(self, *vassals):
        super().__init__("money");
        self.__vassals = vassals;
    def vassals(self):
        return self.__vassals;


# Want to add message, but can't touch classes

class CharacterVisitor:
    def accept(self, char):
        # no overload by param type --> dispatch by hands
        # other solution -- multemethods (extra library is required)
        if isinstance(char, Elf):
            self.acceptElf(char);
        elif isinstance(char, Human):
            self.acceptHuman(char);
        elif isinstance(char, Orc):
            self.acceptOrc(char);
        elif isinstance(char, Lord):
            self.acceptLord(char);
        else:
            raise ValueError("Unknown character");

class MessagingVisitor(CharacterVisitor):
    def __init__(self):
        self.humanNm = 0;

    def acceptElf(self, elf):
        print("Elf: My {0} is ready!".format(elf.favWeapon()));
    
    def acceptHuman(self, human):
        if self.humanNm == 0:
            print("Human: I'm the only human!");
        else:
            print("Human: I will never walk alone");
        self.humanNm += 1;

    def acceptOrc(self, orc):
        print("Orc: Groughhh");

    def acceptLord(self, lord):
        # treat lord as a separate person
        print("Lord: I'm lord. Get off my way");

class HiringCostCounter(CharacterVisitor):
    def __init__(self):
        self.__totalCost = 0;

    def acceptElf(self, elf):
        self.__totalCost += 15;
    
    def acceptHuman(self, human):
        self.__totalCost += 10;

    def acceptOrc(self, orc):
        self.__totalCost += 30;

    def acceptLord(self, lord):
        # Lord is not a fighter, we can entice his army.
        for v in lord.vassals():
            v.visit(self);

    def totalCost(self):
        return self.__totalCost;

if __name__ == "__main__":
    msgVisitor = MessagingVisitor();
    hiringCounter = HiringCostCounter();

    for ch in [Elf(), Human(), Lord(Elf(), Elf(), Orc()), Orc(), Human()]:
        ch.visit(msgVisitor);
        ch.visit(hiringCounter);

    print("Total cost:", hiringCounter.totalCost());

# NB: visitor is not about traversal.
#     It's about adding actions to every item in hierachy.
#     Visitor can itself define traversal order or ignore it (lord example)
# Drawback:
#     New character --> need to modify all visitors.
        
