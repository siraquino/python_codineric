def fixe_whidth_parser(datos):
    lst = [
        "{0:05d}".format(datos[0]),
        datos[1],
        "".join(datos[2].split("/")),
        "".join(datos[3].split(":")),
    ]
    str_lst = "".join(lst)

    return str_lst

#def fixe_whidth_reader(data_in):
#        print(data_in[0:5])
#        print(data_in[5:6])
#        print(data_in[6:8])
#        print(data_in[8:11])
#        print(data_in[11:15])
#        print(data_in[15:17])
#        print(data_in[17:19])
#        print(data_in[19:21])
    
def fixe_whidth_reader(data_in):
    lst_out = [
        int(data_in[0:5]),
        data_in[5:6],
        "/".join([data_in[6:8],data_in[8:11],data_in[11:15]]),
        ":".join([data_in[15:17],data_in[17:19],data_in[19:21]])
    ]
    print(lst_out)        


#id_persona   | tipo   | fecha y hora
#00010e10MAY2019071530

datos = [10,"e","10/MAY/2019","07:15:30"]

str_datos = fixe_whidth_parser(datos)

with open("python_codineric\entr_sal.txt","w") as outf:
    outf.write(str_datos)

with open("python_codineric\entr_sal.txt","r") as inf:
    data_in = inf.read()

fixe_whidth_reader(data_in)
print(data_in)