w_lenght_metres = float(input())
h_width_metres = float(input())

h_width_cm = h_width_metres * 100                         #от метри в см
hall = 100                                                #см
number_working_places_width = (h_width_cm - hall) / 70    #брой места на ред

w_lenght_cm = w_lenght_metres * 100                       #от метри в см
number_working_places_lenght = w_lenght_cm / 120          #брой редове

number_possible_working_places = (int(number_working_places_lenght) *\
                                  int(number_working_places_width))
final_number = number_possible_working_places - 3         #вртата и катедрата заемат общо 3 места
print(final_number)