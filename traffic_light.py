from random import choice

traffic_light={"červená" :"Zůstaň stát!" , "žlutá" :"Připrav se!" , "zelená" : "Jeď"}
random_warning_list = ["Tato barva není na semaforu.", "Asi porucha", "Vyber správnou barvu!",
                       "Červená, žlutá, nebo zelená", "Ty jsi případ!", "Lorem ipsum dolor"]

def last_warning_message(msg_text):
    return msg_text


def random_message(last_warning_text):
    temp_warning_list = random_warning_list.copy()
    if last_warning_text in temp_warning_list:
        temp_warning_list.remove(last_warning_text)
    message = choice(temp_warning_list)
    return message

def main():
    repeat_cycle = True
    last_warning_msg=""
    while repeat_cycle :
        repeat_cycle = False
        print(f"Poslední náhodný vzkaz: {last_warning_msg}")

        color_of_light = input("Zadej barvu světla na semaforu: ")
        what_to_do = traffic_light.get(color_of_light)
        if what_to_do == None:
            random_warning = random_message(last_warning_msg)
            last_warning_msg = random_warning
            print (random_warning)
        else:
            last_warning_msg = ""
            print (what_to_do)

        once_again = input("Opakovat cyklus ? (Ano/Ne) ")
        once_again = once_again.lower()
        if once_again == "ano" :
            repeat_cycle = True

    print("Program bude ukončen.")

if __name__ == "__main__":
    main()
