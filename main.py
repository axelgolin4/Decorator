from time import sleep

import portalWeapon
from armourDecorator import ArmourDecorator
from birdman import Birdman
from helmetDecorator import HelmetDecorator
from laserWeapon import LaserWeapon
from morty import Morty
from mrpoopybutthole import MrPoopyButtHole
from portalWeapon import PortalWeapon
from rick import Rick

print("ESCOGE A TU PERSONAJE")
print("1. Rick")
print("2. Morty")
print("3. Mr. PoopyButtHole")
print("4. Birdman")


#CHARACTERS
def character(option):
    characters = {
        1: "Escogiste a Rick \n",
        2: "Escogiste a Morty \n",
        3: "Escogiste a Mr. PoopyButtHole \n",
        4: "Escogiste a Birdman \n"
    }
    return characters.get(option)

# DECORATORS

def decorators_list():
    print("ESCOGE TU COMPLEMENTO")
    print("1. Casco ")
    print("2. Armadura ")
    print("3. Pistola de Portales ")
    print("4. Pistola Laser ")


def decorator(option_decorator):
    decorators = {
        1: "Escogiste Casco \n",
        2: "Escogiste Armadura \n",
        3: "Escogiste Pistola de Portales \n",
        4: "Escogiste Pistola Laser \n"
    }
    return decorators.get(option_decorator)


# OPTIONS
character_option = int(input("Ingresa Opcion: "))
print(character(character_option))
sleep(2)


# SWITCH
# RICK
if character_option==1:
    rick = Rick()
    print(decorators_list())
    decorator_option = int(input("Ingrese Opcion: "))
    print(decorator(decorator_option))
    sleep(2)
    # PRIMER COMLEMENTO
    if decorator_option==1:
        enemywithhelmet = HelmetDecorator(rick)
        computedDamaged = enemywithhelmet.take_damage()
        computedVelocity = enemywithhelmet.get_velocity()
        computedDefence = enemywithhelmet.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))
        print("Defensa: " + str(computedDefence))
        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            print("YA ESCOGISTE CASCO!")
        elif decorator_option == 2:
            enemywithhelmetandarmour = ArmourDecorator(enemywithhelmet)
            computedDamaged = enemywithhelmetandarmour.take_damage()
            computedVelocity = enemywithhelmetandarmour.get_velocity()
            computedDefence = enemywithhelmetandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            enemywithhelmetandportalweapon = PortalWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandportalweapon.take_damage()
            computedVelocity = enemywithhelmetandportalweapon.get_velocity()
            computedDefence = enemywithhelmetandportalweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 4:
            enemywithhelmetandlaserweapon = LaserWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandlaserweapon.take_damage()
            computedVelocity = enemywithhelmetandlaserweapon.get_velocity()
            computedDefence = enemywithhelmetandlaserweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))


    elif decorator_option==2:
        enemywitharmour = ArmourDecorator(rick)
        computedDamaged = enemywitharmour.take_damage()
        computedVelocity = enemywitharmour.get_velocity()
        computedDefence = enemywitharmour.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))
        print("Defensa: " + str(computedDefence))

        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            enemywitharmourandhelmet = HelmetDecorator(enemywitharmour)
            computedDamaged = enemywitharmourandhelmet.take_damage()
            computedVelocity = enemywitharmourandhelmet.get_velocity()
            computedDefence = enemywitharmourandhelmet.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 2:
            print("Ya Tienes Armadura!")
        elif decorator_option == 3:
            enemywitharmourandportalweapon = PortalWeapon(enemywitharmour)
            computedDamaged = enemywitharmourandportalweapon.take_damage()
            computedVelocity = enemywitharmourandportalweapon.get_velocity()
            computedDefence = enemywitharmourandportalweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 4:
            enemywithamourandlaserweapon = LaserWeapon(enemywitharmour)
            computedDamaged = enemywithamourandlaserweapon.take_damage()
            computedVelocity = enemywithamourandlaserweapon.get_velocity()
            computedDefence = enemywithamourandlaserweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))

    elif decorator_option==3:
        enemywithportalgun = PortalWeapon(rick)
        computedDamaged = enemywithportalgun.take_damage()
        computedVelocity = enemywithportalgun.get_velocity()
        computedDefence = enemywithportalgun.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))

        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            enemywithportalgunandhelmet = HelmetDecorator(enemywithportalgun)
            computedDamaged = enemywithportalgunandhelmet.take_damage()
            computedVelocity = enemywithportalgunandhelmet.get_velocity()
            computedDefence = enemywithportalgunandhelmet.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 2:
            enemywithportalgunandarmour = ArmourDecorator(enemywithportalgun)
            computedDamaged = enemywithportalgunandarmour.take_damage()
            computedVelocity = enemywithportalgunandarmour.get_velocity()
            computedDefence = enemywithportalgunandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            print("YA TIENE UNA PISTOLA DE PORTALES!")
        elif decorator_option == 4:
            print("YA TIENES UN ARMA")

    elif decorator_option==4:
        enemywithlasergun = LaserWeapon(rick)
        computedDamaged = enemywithlasergun.take_damage()
        computedVelocity = enemywithlasergun.get_velocity()
        computedDefence = enemywithlasergun.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))

        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            enemywithlasergunandhelmet = HelmetDecorator(enemywithlasergun)
            computedDamaged = enemywithlasergunandhelmet.take_damage()
            computedVelocity = enemywithlasergunandhelmet.get_velocity()
            computedDefence = enemywithlasergunandhelmet.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 2:
            enemywithlasergunandarmour = ArmourDecorator(enemywithlasergun)
            computedDamaged = enemywithlasergunandarmour.take_damage()
            computedVelocity = enemywithlasergunandarmour.get_velocity()
            computedDefence = enemywithlasergunandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            print("YA TIENE UNA PISTOLA DE PORTALES!")
        elif decorator_option == 4:
            print("YA TIENES UN ARMA")
# MORTY
elif character_option==2:
    morty = Morty()
    print(decorators_list())
    decorator_option = int(input("Ingrese Opcion: "))
    print(decorator(decorator_option))
    sleep(2)
    # PRIMER COMLEMENTO
    if decorator_option == 1:
        enemywithhelmet = HelmetDecorator(morty)
        computedDamaged = enemywithhelmet.take_damage()
        computedVelocity = enemywithhelmet.get_velocity()
        computedDefence = enemywithhelmet.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))
        print("Defensa: " + str(computedDefence))
        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            print("YA ESCOGISTE CASCO!")
        elif decorator_option == 2:
            enemywithhelmetandarmour = ArmourDecorator(enemywithhelmet)
            computedDamaged = enemywithhelmetandarmour.take_damage()
            computedVelocity = enemywithhelmetandarmour.get_velocity()
            computedDefence = enemywithhelmetandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            enemywithhelmetandportalweapon = PortalWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandportalweapon.take_damage()
            computedVelocity = enemywithhelmetandportalweapon.get_velocity()
            computedDefence = enemywithhelmetandportalweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 4:
            enemywithhelmetandlaserweapon = LaserWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandlaserweapon.take_damage()
            computedVelocity = enemywithhelmetandlaserweapon.get_velocity()
            computedDefence = enemywithhelmetandlaserweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))


        elif decorator_option == 2:
            enemywitharmour = ArmourDecorator(morty)
            computedDamaged = enemywitharmour.take_damage()
            computedVelocity = enemywitharmour.get_velocity()
            computedDefence = enemywitharmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywitharmourandhelmet = HelmetDecorator(enemywitharmour)
                computedDamaged = enemywitharmourandhelmet.take_damage()
                computedVelocity = enemywitharmourandhelmet.get_velocity()
                computedDefence = enemywitharmourandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                print("Ya Tienes Armadura!")
            elif decorator_option == 3:
                enemywitharmourandportalweapon = PortalWeapon(enemywitharmour)
                computedDamaged = enemywitharmourandportalweapon.take_damage()
                computedVelocity = enemywitharmourandportalweapon.get_velocity()
                computedDefence = enemywitharmourandportalweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 4:
                enemywithamourandlaserweapon = LaserWeapon(enemywitharmour)
                computedDamaged = enemywithamourandlaserweapon.take_damage()
                computedVelocity = enemywithamourandlaserweapon.get_velocity()
                computedDefence = enemywithamourandlaserweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))

        elif decorator_option == 3:
            enemywithportalgun = PortalWeapon(morty)
            computedDamaged = enemywithportalgun.take_damage()
            computedVelocity = enemywithportalgun.get_velocity()
            computedDefence = enemywithportalgun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithportalgunandhelmet = HelmetDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandhelmet.take_damage()
                computedVelocity = enemywithportalgunandhelmet.get_velocity()
                computedDefence = enemywithportalgunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithportalgunandarmour = ArmourDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandarmour.take_damage()
                computedVelocity = enemywithportalgunandarmour.get_velocity()
                computedDefence = enemywithportalgunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")

        elif decorator_option == 4:
            enemywithlasergun = LaserWeapon(morty)
            computedDamaged = enemywithlasergun.take_damage()
            computedVelocity = enemywithlasergun.get_velocity()
            computedDefence = enemywithlasergun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithlasergunandhelmet = HelmetDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandhelmet.take_damage()
                computedVelocity = enemywithlasergunandhelmet.get_velocity()
                computedDefence = enemywithlasergunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithlasergunandarmour = ArmourDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandarmour.take_damage()
                computedVelocity = enemywithlasergunandarmour.get_velocity()
                computedDefence = enemywithlasergunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")
# MrPoopyButtHole
if character_option==3:
    mrpoopybutthole = MrPoopyButtHole()
    print(decorators_list())
    decorator_option = int(input("Ingrese Opcion: "))
    print(decorator(decorator_option))
    sleep(2)
    # PRIMER COMLEMENTO
    if decorator_option == 1:
        enemywithhelmet = HelmetDecorator(mrpoopybutthole)
        computedDamaged = enemywithhelmet.take_damage()
        computedVelocity = enemywithhelmet.get_velocity()
        computedDefence = enemywithhelmet.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))
        print("Defensa: " + str(computedDefence))
        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            print("YA ESCOGISTE CASCO!")
        elif decorator_option == 2:
            enemywithhelmetandarmour = ArmourDecorator(enemywithhelmet)
            computedDamaged = enemywithhelmetandarmour.take_damage()
            computedVelocity = enemywithhelmetandarmour.get_velocity()
            computedDefence = enemywithhelmetandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            enemywithhelmetandportalweapon = PortalWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandportalweapon.take_damage()
            computedVelocity = enemywithhelmetandportalweapon.get_velocity()
            computedDefence = enemywithhelmetandportalweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 4:
            enemywithhelmetandlaserweapon = LaserWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandlaserweapon.take_damage()
            computedVelocity = enemywithhelmetandlaserweapon.get_velocity()
            computedDefence = enemywithhelmetandlaserweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))


        elif decorator_option == 2:
            enemywitharmour = ArmourDecorator(mrpoopybutthole)
            computedDamaged = enemywitharmour.take_damage()
            computedVelocity = enemywitharmour.get_velocity()
            computedDefence = enemywitharmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywitharmourandhelmet = HelmetDecorator(enemywitharmour)
                computedDamaged = enemywitharmourandhelmet.take_damage()
                computedVelocity = enemywitharmourandhelmet.get_velocity()
                computedDefence = enemywitharmourandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                print("Ya Tienes Armadura!")
            elif decorator_option == 3:
                enemywitharmourandportalweapon = PortalWeapon(enemywitharmour)
                computedDamaged = enemywitharmourandportalweapon.take_damage()
                computedVelocity = enemywitharmourandportalweapon.get_velocity()
                computedDefence = enemywitharmourandportalweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 4:
                enemywithamourandlaserweapon = LaserWeapon(enemywitharmour)
                computedDamaged = enemywithamourandlaserweapon.take_damage()
                computedVelocity = enemywithamourandlaserweapon.get_velocity()
                computedDefence = enemywithamourandlaserweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))

        elif decorator_option == 3:
            enemywithportalgun = PortalWeapon(mrpoopybutthole)
            computedDamaged = enemywithportalgun.take_damage()
            computedVelocity = enemywithportalgun.get_velocity()
            computedDefence = enemywithportalgun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithportalgunandhelmet = HelmetDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandhelmet.take_damage()
                computedVelocity = enemywithportalgunandhelmet.get_velocity()
                computedDefence = enemywithportalgunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithportalgunandarmour = ArmourDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandarmour.take_damage()
                computedVelocity = enemywithportalgunandarmour.get_velocity()
                computedDefence = enemywithportalgunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")

        elif decorator_option == 4:
            enemywithlasergun = LaserWeapon(mrpoopybutthole)
            computedDamaged = enemywithlasergun.take_damage()
            computedVelocity = enemywithlasergun.get_velocity()
            computedDefence = enemywithlasergun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithlasergunandhelmet = HelmetDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandhelmet.take_damage()
                computedVelocity = enemywithlasergunandhelmet.get_velocity()
                computedDefence = enemywithlasergunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithlasergunandarmour = ArmourDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandarmour.take_damage()
                computedVelocity = enemywithlasergunandarmour.get_velocity()
                computedDefence = enemywithlasergunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")
# Birdman
if character_option==4:
    birdman = Birdman()
    print(decorators_list())
    decorator_option = int(input("Ingrese Opcion: "))
    print(decorator(decorator_option))
    sleep(2)
    # PRIMER COMLEMENTO
    if decorator_option == 1:
        enemywithhelmet = HelmetDecorator(birdman)
        computedDamaged = enemywithhelmet.take_damage()
        computedVelocity = enemywithhelmet.get_velocity()
        computedDefence = enemywithhelmet.get_def()
        print("Ataque: " + str(computedDamaged))
        print("Velocidad: " + str(computedVelocity))
        print("Defensa: " + str(computedDefence))
        # SEGUNDO COMPLEMENTO
        print('\n')
        print("ESCOGE TU SEGUNDO COMPLEMENTO")
        print(decorators_list())
        decorator_option = int(input("Ingrese Opcion: "))
        print(decorator(decorator_option))
        if decorator_option == 1:
            print("YA ESCOGISTE CASCO!")
        elif decorator_option == 2:
            enemywithhelmetandarmour = ArmourDecorator(enemywithhelmet)
            computedDamaged = enemywithhelmetandarmour.take_damage()
            computedVelocity = enemywithhelmetandarmour.get_velocity()
            computedDefence = enemywithhelmetandarmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 3:
            enemywithhelmetandportalweapon = PortalWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandportalweapon.take_damage()
            computedVelocity = enemywithhelmetandportalweapon.get_velocity()
            computedDefence = enemywithhelmetandportalweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))
        elif decorator_option == 4:
            enemywithhelmetandlaserweapon = LaserWeapon(enemywithhelmet)
            computedDamaged = enemywithhelmetandlaserweapon.take_damage()
            computedVelocity = enemywithhelmetandlaserweapon.get_velocity()
            computedDefence = enemywithhelmetandlaserweapon.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))


        elif decorator_option == 2:
            enemywitharmour = ArmourDecorator(birdman)
            computedDamaged = enemywitharmour.take_damage()
            computedVelocity = enemywitharmour.get_velocity()
            computedDefence = enemywitharmour.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))
            print("Defensa: " + str(computedDefence))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywitharmourandhelmet = HelmetDecorator(enemywitharmour)
                computedDamaged = enemywitharmourandhelmet.take_damage()
                computedVelocity = enemywitharmourandhelmet.get_velocity()
                computedDefence = enemywitharmourandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                print("Ya Tienes Armadura!")
            elif decorator_option == 3:
                enemywitharmourandportalweapon = PortalWeapon(enemywitharmour)
                computedDamaged = enemywitharmourandportalweapon.take_damage()
                computedVelocity = enemywitharmourandportalweapon.get_velocity()
                computedDefence = enemywitharmourandportalweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 4:
                enemywithamourandlaserweapon = LaserWeapon(enemywitharmour)
                computedDamaged = enemywithamourandlaserweapon.take_damage()
                computedVelocity = enemywithamourandlaserweapon.get_velocity()
                computedDefence = enemywithamourandlaserweapon.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))

        elif decorator_option == 3:
            enemywithportalgun = PortalWeapon(birdman)
            computedDamaged = enemywithportalgun.take_damage()
            computedVelocity = enemywithportalgun.get_velocity()
            computedDefence = enemywithportalgun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithportalgunandhelmet = HelmetDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandhelmet.take_damage()
                computedVelocity = enemywithportalgunandhelmet.get_velocity()
                computedDefence = enemywithportalgunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithportalgunandarmour = ArmourDecorator(enemywithportalgun)
                computedDamaged = enemywithportalgunandarmour.take_damage()
                computedVelocity = enemywithportalgunandarmour.get_velocity()
                computedDefence = enemywithportalgunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")

        elif decorator_option == 4:
            enemywithlasergun = LaserWeapon(birdman)
            computedDamaged = enemywithlasergun.take_damage()
            computedVelocity = enemywithlasergun.get_velocity()
            computedDefence = enemywithlasergun.get_def()
            print("Ataque: " + str(computedDamaged))
            print("Velocidad: " + str(computedVelocity))

            # SEGUNDO COMPLEMENTO
            print('\n')
            print("ESCOGE TU SEGUNDO COMPLEMENTO")
            print(decorators_list())
            decorator_option = int(input("Ingrese Opcion: "))
            print(decorator(decorator_option))
            if decorator_option == 1:
                enemywithlasergunandhelmet = HelmetDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandhelmet.take_damage()
                computedVelocity = enemywithlasergunandhelmet.get_velocity()
                computedDefence = enemywithlasergunandhelmet.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 2:
                enemywithlasergunandarmour = ArmourDecorator(enemywithlasergun)
                computedDamaged = enemywithlasergunandarmour.take_damage()
                computedVelocity = enemywithlasergunandarmour.get_velocity()
                computedDefence = enemywithlasergunandarmour.get_def()
                print("Ataque: " + str(computedDamaged))
                print("Velocidad: " + str(computedVelocity))
                print("Defensa: " + str(computedDefence))
            elif decorator_option == 3:
                print("YA TIENE UNA PISTOLA DE PORTALES!")
            elif decorator_option == 4:
                print("YA TIENES UN ARMA")











        # print(f"Rick Tiene:, \n Vida: {life}, \n Defensa: {defence}, \n Velocidad: {velocity}, \n Ataque: {computedDamaged} \n")









# def choose_character():
#     opcion_personaje = input("Ingrese Opcion:")
#     if opcion_personaje == 1:
#         rick = Rick()
#         print("ESCOGISTE A RICK!")
#         def choose_defence(opcion_defensa):
#             print("ESCOGE TU ARMADURA")
#             print("1. Casco")
#             print("2. Armadura")
#             print("3. Casco y Armadura")
#
#             if opcion_defensa == 1:
#                 enemywithhelmet = HelmetDecorator(rick)
#                 computedDamaged = enemywithhelmet.take_damage()
#                 velocity = enemywithhelmet.get_velocity()
#                 defence = enemywithhelmet.get_def()
#                 life = rick.get_hp()
#                 print(f"Rick Tiene:, \n Vida: {life}, \n Defensa: {defence}, \n Velocidad: {velocity}, \n Ataque: {computedDamaged} \n")



#     elif operador == 'resta':
#         return a - b
#     elif operador == 'multiplica':
#         return a * b
#     elif operador == 'divide':
#         return a / b
#     else:
#         return None
#
# rick = Rick()
# enemywithhelmet = HelmetDecorator(rick)
# enemywitharmourandhelmet = ArmourDecorator(enemywithhelmet)
# computedDamaged = enemywitharmourandhelmet.take_damage()
#
#
# enemywithhelmetandportalweapon = PortalWeapon(enemywithhelmet)
# velocity = enemywithhelmetandportalweapon.get_velocity()
#
# print (velocity)
# print(computedDamaged)


# choose_character()