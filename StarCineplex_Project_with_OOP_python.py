#_Coder : anmamun0 | 27 October 2024 ||  14:19:13
# بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ _File: Mid_Exam.py 
#  starCineplex
class StarCineplex:
    def __init__(self) -> None:
        self.hall_list = {}

    def entry_hall(self,hall):
        self.hall_list[hall.hall_no] = hall 

class Hall:
    def __init__(self,hall_no,row,col) -> None:
        self.__seats = {}
        self._show_list = []
        self.row = row
        self.col = col 
        self.hall_no = hall_no

    def entry_show(self,id,movie_name,time):
        info = (id,movie_name,time)
        self._show_list.append(info)
        self.__seats[id] = [[0]*self.col for _ in range(self.row)]
        
    def book_seats(self,movie_id,row,col):
        if movie_id in self.__seats:
            if self.__seats[movie_id][row][col] == 1:
                return False
            self.__seats[movie_id][row][col] = 1
            return True
        return False
    
    def view_show_list(self):
        for movie in self._show_list:
            movie_info = f"{movie[1]}({movie[0]})"
            print(f"MOVIE NAME: {movie_info.ljust(25,'-')} Hall_ID:{self.hall_no} TIME:{movie[2]}")
   
    def view_abailable_seats(self,movie_id): 
        if movie_id in self.__seats: 
            print(f"\nMovie Id : {movie_id} | Holl ID: {self.hall_no}")
            for c in self.__seats[movie_id]:
                print(c) 
            return True
        else :
            return False

class Customer:
    def __init__(self) -> None:
        pass
    def option1(self,host):
        for key ,val in host.hall_list.items():
            val.view_show_list()
    def option2(self,host,movie_id):
        cnt = 0
        for key,val in host.hall_list.items():
            chack = val.view_abailable_seats(movie_id)
            if chack == True:
                cnt += 1
        if cnt == 0:
            print(f"Movie Id {movie_id} Not available of any Hall! Please Watch another Moview")
        print()
    def option3(self,host,hall_id,row,clm):
        if hall_id in host.hall_list:
            room = host.hall_list[hall_id]
            if len(room._show_list) == 0 :
                print(f"No show in this Hall({hall_id})") 
                return 
            if row<0 or row>room.row or clm<0 or clm>room.col:
                print("The seat is invalid! Please Choice valid seat")
                return 
            movie_id = room._show_list[0][0]
            conformation = room.book_seats(movie_id,row,clm)
            if conformation == False:
                print(f"Already Fill your seat, Please choise other seat")
            else :
                print(f"Booked seat:[{row}][{clm}] | Hall No : {hall_id}, Enjoy!")
        else :
            print(f"That Hall {hall_id} not exist our Cenapleax! Try again!")
        print()
        
if __name__ == "__main__":
    print("\n",'-'*10,"Welcome to visit our StarCineplex",'-'*10)

    fly = StarCineplex()  
    fly.entry_hall(Hall(101,4,8))
    fly.entry_hall(Hall(102,5,5))
    fly.entry_hall(Hall(103,7,7))
    fly.entry_hall(Hall(205,4,7))

    fly.hall_list[101].entry_show(1005,'Avengar','2024-10-30: 2:30 PM')
    fly.hall_list[101].entry_show(1006,'Black Panther','2024-10-30: 4:30 PM')
    fly.hall_list[205].entry_show(1005,'Avengar','2024-10-30: 2:30 PM')
    fly.hall_list[102].entry_show(1007,'Infinity War','2024-10-30: 2:30 PM')
    
    while True:
        print('1. VIEW ALL SHOW TODAY')
        print('2. VIEW AVAILABLE SEATS')
        print('3. BOOK TICKET')
        print('4. EXIT')
        n = int(input("ENTER OPTION :>> "))
        guest = Customer()
        if n == 1:
            guest.option1(fly)
            print()
        if n == 2:
            movie_id = int(input("ENTER MOVIE ID: "))
            guest.option2(fly,movie_id)
        if n == 3:
            id = int(input("Enter Hall ID: "))
            row = int(input("Enter Row:"))
            clm = int(input("Enter Column:"))
            guest.option3(fly,id,row,clm)
            print()
        elif n == 4:
            break
