def leap_year():
    year_input=input("Ingrese un año: ")
    year_input=int(year_input)
    if year_input % 4 == 0 and  not year_input %100 ==0 or year_input % 400 == 0:
        print(f"El año {year_input} es bisiesto")
    else:
        print(f"El año {year_input} no es bisiesto")
