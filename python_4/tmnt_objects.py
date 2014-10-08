# author: Artur Huletsky (hatless.fox@gmail.com)
#
# NB: UI stands for unknown info. You must read about it yourself

#!/usr/bin/env python3

import random;

class Hero(object): # object parent is implicit
    def __init__(self, name, health, damage):
        self.__name = name;
        self.__health = health;
        self.__damage = damage;
    def name(self):
        return self.__name;
    def damage(self): # accessor
        return self.__damage;
    def is_dead(self):
        return self.__health <= 0;
    def say(self, msg):
        print("{0}: {1}".format(self.name(), msg));
    def victory_cry(self):
        pass;
    def battle_cry(self):
        pass;
    def _get_a_hit(self, damage):
        self.__health -= damage;
        self.say("D'oh... {0} to go.".format(self.__health));
    def hit_enemy(self, enemy):
        dmg_loss = random.randint(0, self.__damage // 2 + 1);
        enemy._get_a_hit(self.__damage - dmg_loss);

class NinjaTurtle(Hero): # inherit from Hero
    def __init__(self, name):
        super(NinjaTurtle, self).__init__(name, 10, 4);
    def battle_cry(self):
        # super() == super(NinjaTurtle, self)
        super().say("Kawabanga");
    def victory_cry(self):
        super().say("Let's go 4 pizzza");

class BadBoss(Hero): # inherit form Hero
    def battle_cry(self):
        super().say("Die freaking turtles!");
    def victory_cry(self):
        super().say("I'm not defeated? No way!");

#UI: Inspired by Composite pattern
class TurtlesBand(Hero):
    def __init__(self):
        self.__turtles = [
            NinjaTurtle("Leo"), NinjaTurtle("Mike"),
            NinjaTurtle("Don"), NinjaTurtle("Raph")
        ]

    def name(self): # accessor
        return "Turtles Band";

    def is_dead(self):
        return not self.__turtles;

    def victory_cry(self):
        # UI: welcome list comprehension
        [t.victory_cry() for t in self.__turtles];

    def battle_cry(self):
        [t.battle_cry() for t in self.__turtles]

    def _get_a_hit(self, damage):
        turtles_nm = len(self.__turtles);
        if turtles_nm == 0:
            return;
        victim_i = random.randint(0, turtles_nm);
        if victim_i == turtles_nm:
            super().say("Miss, Ha-ha");
            return;
        victim = self.__turtles[victim_i];
        victim._get_a_hit(damage);
        if victim.is_dead():
            victim.say("I'm dead... Sorry dudes");
            del self.__turtles[victim_i];

    def hit_enemy(self, enemy):
        for t in self.__turtles:
            if enemy.is_dead():
                super().say("We don't hit deads");
                break;
            t.hit_enemy(enemy);

class Battle:
    def __print_sw_intro(): # static method
        print("== A long time ago in a galaxy far far away... ==");
    def __init__(self, f1, f2):
        self.__fighter1 = f1;
        self.__fighter2 = f2;
    def are_fighters_alive(self):
        return not (self.__fighter1.is_dead() \
                 or self.__fighter2.is_dead())

    def battle(self):
        figh1, figh2 = self.__fighter1, self.__fighter2;
        print("== Let the battle begin ==");
        [f.battle_cry() for f in [figh1, figh2]];
        print("== Fight! ==");
        while self.are_fighters_alive():
            figh1.hit_enemy(figh2);
            if figh2.is_dead():
                break;
            figh2.hit_enemy(figh1);

        winner = figh1 if figh2.is_dead() else figh2;
        print("== Winner Interview ==");
        winner.victory_cry();

if __name__ == "__main__":

    Battle._Battle__print_sw_intro(); # name mangling for methods

    boss = BadBoss("Shredder", 50, 11);
    turtles = TurtlesBand();

    arena = Battle(turtles, boss)
    arena.battle()


# NB:
#    call "say" for TurtlesBand (polymorphism)
#    call "damage" for TurtlesBand (error)
#    renaming _get_a_hit to __get_a_hit effect? (name mangling)
