from random import choice

def random_message():
    random_warning_list=["Tato barva není na semaforu." , "Asi porucha", "Vyber správnou barvu!",
                         "Červená, žlutá, nebo zelená", "Ty jsi případ!" , "Lorem ipsum dolor"]
    message = choice(random_warning_list)
    return message

def return_answer (shining_light):
    traffic_light={"červená" :"Zůstaň stát!" , "žlutá" :"Připrav se!" , "zelená" : "Jeď"}
    what_to_do =  traffic_light.get(shining_light)
    if what_to_do == None:
        random_warning = random_message()
        return random_warning
    else:
        return what_to_do

def main():
    repeat_cycle = True
    while repeat_cycle :
        repeat_cycle = False

        traffic_light = input("Zadej barvu světla na semaforu: ")
        your_behaviour = return_answer(traffic_light)
        print(your_behaviour)
        once_again = input("Opakovat cyklus ? (Ano/Ne) ")
        once_again = once_again.lower()
        if once_again == "ano" :
            repeat_cycle = True

    print("Program bude ukončen.")

if __name__ == "__main__":
    main()
