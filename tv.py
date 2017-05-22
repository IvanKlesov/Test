class Television(object):
    def __init__(self, model, channel = 1, volume = 5):
        self.model = model
        self.channel = channel
        self.volume = volume
    def chan(self):
        i = 0
        self.channel = None
        while i != 1:
            self.channel = int(input("Введите номер канала: "))
            if self.channel > 0 and self.channel < 20:
                print ("Вы включили ", self.channel ," канал.")
                i = 1
            else:
                print ("Такого канала не существует. Попробуйте еще раз.")
    def vol1(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print ("Громкость - ", self.volume)
    def vol2(self):
        self.volume += 1
        if self.volume > 10:
            self.volume = 10
        print ("Громкость - ", self.volume)

def main():
    tv_model = input("Введите модель вашего телевизора: ")
    tv = Television(tv_model)
    choice = None
    while choice != "Exit":
        print("""
        Телевизор
        Exit - Выйти
        Channel - Переключить канал
        Volume+ - Повысить громкость
        Volume- - Понизить громкость
        """)
        choice = input("Что вы хотите сделать?")
        if choice == "Exit":
            print ("Выключение.")
        elif choice == "Channel":
            tv.chan()
        elif choice == "Volume+":
            tv.vol2()
        elif choice == "Volume-":
            tv.vol1()
        else:
            print ("Извините, такой функции нет.")

main()            
            
