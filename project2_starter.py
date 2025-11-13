"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [William Webster]
Date: [11/13/2025]

AI Usage: AI helped with inheritance structure and method overriding concepts (Free Use)
"""

import random

# ============================================================================ 
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# (kept here for convenience; you wouldn't change this in the repo)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================ 
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic, weapon=None):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        # Composition: a Character can have a Weapon (or None)
        self.weapon = weapon
    
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        Damage is based on strength and weapon bonus (if any).
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = self.strength + weapon_bonus
        print(f"{self.name} deals {damage} physical damage to {target.name}.")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health will not go below 0.
        """
        old_health = self.health
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage (HP: {old_health} -> {self.health}).")
    
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"Name: {self.name}")
        print(f"  Health:   {self.health}")
        print(f"  Strength: {self.strength}")
        print(f"  Magic:    {self.magic}")
        if self.weapon:
            print(f"  Weapon:   {self.weapon.name} (+{self.weapon.damage_bonus} dmg)")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic, weapon=None):
        """
        Initialize a player character.
        Calls parent constructor and adds player attributes.
        """
        super().__init__(name, health, strength, magic, weapon)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
    
    def display_stats(self):
        """
        Override parent's display_stats to show additional player info.
        """
        super().display_stats()
        print(f"  Class:    {self.character_class}")
        print(f"  Level:    {self.level}")
        print(f"  XP:       {self.experience}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a warrior with appropriate stats.
        Suggested stats: health=120, strength=15, magic=5
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5, weapon=weapon)
    
    def attack(self, target):
        """
        Warriors do extra physical damage (strength + fixed bonus).
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        bonus = 5
        damage = self.strength + bonus + weapon_bonus
        print(f"{self.name} (Warrior) performs a heavy strike for {damage} damage!")
        target.take_damage(damage)
    
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = (self.strength * 2) + 10 + weapon_bonus
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a mage with appropriate stats.
        Suggested stats: health=80, strength=8, magic=20
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20, weapon=weapon)
    
    def attack(self, target):
        """
        Mages use magic for damage instead of strength.
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = self.magic + weapon_bonus
        print(f"{self.name} (Mage) casts a spell dealing {damage} magic damage to {target.name}.")
        target.take_damage(damage)
    
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = (self.magic * 2) + 8 + weapon_bonus
        print(f"{self.name} hurls a FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a rogue with appropriate stats.
        Suggested stats: health=90, strength=12, magic=10
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10, weapon=weapon)
    
    def attack(self, target):
        """
        Rogues have a chance for extra damage (critical hit).
        Use random.randint(1,10); crit if result <= 3 (30% chance).
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        roll = random.randint(1, 10)
        if roll <= 3:  # critical hit
            damage = (self.strength * 2) + weapon_bonus
            print(f"{self.name} (Rogue) lands a CRITICAL HIT! {damage} damage.")
        else:
            damage = self.strength + weapon_bonus
            print(f"{self.name} (Rogue) attacks for {damage} damage.")
        target.take_damage(damage)
    
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        weapon_bonus = self.weapon.damage_bonus if self.weapon else 0
        damage = (self.strength * 2) + 10 + weapon_bonus
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print(f"Weapon: {self.name} (+{self.damage_bonus} damage)")

# ============================================================================ 
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create weapons (composition)
    sword = Weapon("Iron Sword", 5)
    staff = Weapon("Oak Staff", 7)
    dagger = Weapon("Steel Dagger", 4)
    
    # Create one of each character type
    warrior = Warrior("Sir Galahad", weapon=sword)
    mage = Mage("Merlin", weapon=staff)
    rogue = Rogue("Robin Hood", weapon=dagger)
    
    # Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    rogue.display_stats()
    
    # Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        # Reset dummy health for the next attacker
        dummy_target.health = 100
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test the battle system (polymorphic behavior inside SimpleBattle)
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
