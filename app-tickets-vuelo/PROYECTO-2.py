from tkinter import *
import random
global datos
global reserva
datos=[]

class informaciones():
    nombre="";apellido="";DNI="";destino="";avion="";
    dia="";mes="";sexo="";hora="";clase="";puerta="";
    reservex="";asiento=""
#-----Funciones---------------

def window_new_register():            	           
    def regresar1():
        ventana1.state(newstate = "withdraw")
        ventana.state(newstate = "normal")
    
    def ventana_ticket(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
        def regresar_menu():
            ticket.state(newstate = "withdraw")
            ventana.state(newstate = "normal")
            
        ventana1.state(newstate="withdraw")
        ticket=Toplevel()
        ticket.title("Ticekt Creado")
        ticket.resizable(0,0)   
        logo_ticket=PhotoImage(file="ticket_diseño.PNG")
        tick=Label(ticket,image=logo_ticket).pack()
        
        
        Nombre_Label = Label(ticket,text=a).place(x=40, y=127)
        Apellido_Label=Label(ticket,text=b).place(x=102,y=127)
        DNI_Label=Label(ticket,text=c).place(x=40,y=166)
        Sexo_Label=Label(ticket,text=i).place(x=102,y=166)
        
        Origen_Label=Label(ticket,text=j).place(x=40,y=205)
        Destino_Label=Label(ticket,text=d).place(x=102,y=205)
        
        Dia_Label=Label(ticket,text=f).place(x=41,y=243)
        Mes_LAbel=Label(ticket,text=g).place(x=65,y=243)
        hora=Label(ticket,text=n).place(x=130,y=243)
        
        Avion_label=Label(ticket,text=e).place(x=518,y=67)                
        Clase_Label=Label(ticket,text=h).place(x=587,y=67)
                

        Puerta_LAvel=Label(ticket,text=k).place(x=518,y=181)
        Reserva_Label=Label(ticket,text=l).place(x=518,y=222)
        
        Asiento_label=Label(ticket,text=m).place(x=518,y=104)
        
        embarque_label=Label(ticket,text="12:00 pm" if n=="1:00 pm" else "7:00 pm").place(x=518,y=140)
        
        #---Boton regresar al menu
        listo=Button(ticket,text="LISTO",command=regresar_menu)
        listo.config(font=("Century Gothic",10),height=1, width=6,cursor="hand2")
        listo.place(x=405,y=249)     
        ticket.mainloop()
   
    ventana.state(newstate = "withdraw")
    ventana1=Toplevel()
    ventana1.title("Nuevo Registro")
    ventana1.resizable(0,0)   
    i=informaciones()
    #-------DEfinir la imagen de fondo
    logo_registro=PhotoImage(file="new_register1.png")
    logito=Label(ventana1,image=logo_registro).pack()
        
     #-------Texto Nombre
    i.nombre=StringVar()
    txtNombre=Entry(ventana1,textvariable=i.nombre).place(x=152.85,y=297.14)
    
    #-------Texto Apellido
    i.apellido=StringVar()
    txtApellido=Entry(ventana1,textvariable=i.apellido).place(x=152.85,y=338.94)
    #--------Texto DNI
    i.DNI=StringVar()
    txtDNI=Entry(ventana1,textvariable=i.DNI).place(x=152.85,y=432.14)
    #-------Texto Destino
    i.destino=StringVar()
    txtDestino=Entry(ventana1,textvariable=str(i.destino)).place(x=152.85,y=482.82)

    #--------Boton avion
    
#------------------------------------------------------------            
    
    def aceptar_clase1():
        i.clase=StringVar()    
        avion_elegido=Label(ventana1,text="Boeing-777",bg='#01aed8')
        avion_elegido.config(font=("Century Gothic",12),height=1, width=10)
        avion_elegido.place(x=240,y=256.99)
        op_clases=["Premium","Ejecutivo","Primera","Economica"]
        elegir_clase=OptionMenu(ventana1, i.clase, *op_clases)
        elegir_clase.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
        elegir_clase.place(x=94.9,y=636.3)
        columna=random.randint(0,9)
        fila=random.randint(0,55)
        i.asiento=f"Fila: {fila} / Columna: {columna}"
        i.avion="Boeing-777"
    def aceptar_clase2():                
        i.clase=StringVar()
        avion_elegido=Label(ventana1,text="Airbus-a350",bg='#01aed8')
        avion_elegido.config(font=("Century Gothic",12),height=1, width=10)
        avion_elegido.place(x=240,y=256.99)
        op_clases=["Premium","Economica"]
        elegir_clase=OptionMenu(ventana1, i.clase, *op_clases)
        elegir_clase.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
        elegir_clase.place(x=94.9,y=636.3)
        columna=random.randint(0,6)
        fila=random.randint(0,26)
        i.asiento=f"Fila: {fila} / Columna: {columna}"
        i.avion="Airbus-a350"       
            
    #Boton boeing
    avion1=Button(ventana1,text="Boeing-777",command=aceptar_clase1)
    avion1.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
    avion1.place(x=68,y=205)
    
    avion2=Button(ventana1,text="Airbus-a350",command=aceptar_clase2)
    avion2.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
    avion2.place(x=235,y=205)
    #--------Boton dia
    i.dia=StringVar()
    op_dias=[str(i) for i in range(1,31)]
    elegir_dia=OptionMenu(ventana1, i.dia, *op_dias)
    elegir_dia.config(font=("Century Gothic",10),height=1, width=3,cursor="hand2")
    elegir_dia.place(x=68.7,y=533.41)
    #-------Boton mes
    i.mes=StringVar()
    op_meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    elegir_mes=OptionMenu(ventana1, i.mes, *op_meses)
    elegir_mes.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
    elegir_mes.place(x=195,y=533.41)
    #-------Boton hora
    i.hora=StringVar()
    op_hora=["1:00 pm","8:00 pm"]
    elegir_hora=OptionMenu(ventana1, i.hora, *op_hora)
    elegir_hora.config(font=("Century Gothic",10),height=1, width=5,cursor="hand2")
    elegir_hora.place(x=81.18,y=583.99)
    #-------Boton sexo
    i.sexo=StringVar()
    op_sexo=["Masculino","Femenino"]
    elegir_sexo=OptionMenu(ventana1,i.sexo, *op_sexo)
    elegir_sexo.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
    elegir_sexo.place(x=152.85,y=384.74)

    

    i.origen="Lima"
    
    i.puerta="P"+str(random.randint(1,10))
    
    reservita=random.randint(10,900)
    i.reservex=reservita #Recoerdad cambiarlo
        
    
            
    
    #-------Boton Regresar
    abrirVentana1 = Button(ventana1,text="Regresar",cursor="hand2",bg='#849db0',fg='Black', command=regresar1)
    abrirVentana1.config(font=("Century Gothic",10))
    abrirVentana1.place(x=12,y=25)
    def ventana_error():
        def regresar_registro():
            error.state(newstate = "withdraw")
            ventana1.state(newstate = "normal")
        ventana1.state(newstate="withdraw")
        #s.------------
        error=Toplevel()
        
        error.title("Error")
        error.resizable(0,0)
        logo_error=PhotoImage(file="mensaje_error.PNG")
        pegar=Label(error,image=logo_error).pack()
        datos.pop()
        
        #-------Botoon regresar al registro
        ok=Button(error,text="OK",bg='White',command=regresar_registro)
        ok.config(font=("Century Gothic",8),height=1, width=3,cursor="hand2")
        ok.place(x=213,y=250)
        error.mainloop()
        
    
    
    def validar_txt(palabra):
        return False if palabra=="" else True
    def validar_DNI(DNI):
        if DNI=="": return False
        new=""
        for i in DNI:            
            if i in "1234567890": new+=i
            else: return False
        return True if len(new)==8 else False
    def ir_o_noir(nombre,apellido,Dni,Destino):
        if validar_txt(nombre) and validar_txt(apellido) and validar_txt(Destino) and validar_DNI(Dni)==True:
            ventana_ticket(i.nombre.get(),i.apellido.get(),i.DNI.get(),
                           i.destino.get(),i.avion,i.dia.get(),
                           i.mes.get(),i.clase.get(),i.sexo.get(),i.origen,
                           i.puerta,i.reservex,i.asiento,i.hora.get())
            
        else:
            ventana_error()
    
    #-------Boton Guardar    
    guardar=Button(ventana1,text="GUARDAR",bg='#849db0', command=lambda:[datos.append(i),ir_o_noir(i.nombre.get(),i.apellido.get(),
                                                                                                                                  i.DNI.get(),i.destino.get())])
    guardar.config(font=("Century Gothic",10),height=1, width=9,cursor="hand2")
    guardar.place(x=302,y=643.99)
    ventana1.mainloop()
    
    
    
    
    
    
def window_search_register():    
    def regresar():
        ventana2.state(newstate = "withdraw")
        ventana.state(newstate = "normal")

    
    def ventana_buscado():
    
        def volver():
            buscado.state(newstate = "withdraw")
            ventana.state(newstate = "normal")
        ventana2.state(newstate="withdraw")
        buscado=Toplevel()
        buscado.title("TIcket Buscado")
        buscado.resizable(0,0)
        logo_busqueda=PhotoImage(file="registro_encontrado.png")
        poner_logo=Label(buscado,image=logo_busqueda).pack()
        #Boton regresar
        again=Button(buscado,text="Regresar",command=volver)
        again.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
        again.place(x=12,y=25)
        
        
        
        for i in datos:
            if i.reservex==int(reserva.get()):
               #Hora (x=259,y=366)
                a=Label(buscado,text=str(i.nombre.get()))
                a.config(font=("Century Gothic",10),height=1)
                a.place(x=101,y=187)
                
                b=Label(buscado,text=str(i.apellido.get()))        
                b.config(font=("Century Gothic",10),height=1)
                b.place(x=282,y=190)
                
                c=Label(buscado,text=str(i.DNI.get()))
                c.config(font=("Century Gothic",10),height=1)
                c.place(x=251,y=242)
                
                d=Label(buscado,text=str(i.destino.get()))
                d.config(font=("Century Gothic",10),height=1)
                d.place(x=100,y=303)
                
                e=Label(buscado,text=str(i.avion))
                e.config(font=("Century Gothic",10),height=1)
                e.place(x=272,y=440)
                
                f=Label(buscado,text=str(i.dia.get()))
                f.config(font=("Century Gothic",10),height=1)
                f.place(x=251,y=300)
                
                g=Label(buscado,text=str(i.mes.get()))
                g.config(font=("Century Gothic",10),height=1)
                g.place(x=71,y=366)
                
                h=Label(buscado,text=str(i.clase.get()))
                h.config(font=("Century Gothic",10),height=1)
                h.place(x=83,y=441)
                
                pt=Label(buscado,text=str(i.sexo.get()))
                pt.config(font=("Century Gothic",10),height=1)
                pt.place(x=79,y=246)
                
                j=Label(buscado,text="Lima")
                j.config(font=("Century Gothic",10),height=1)
                j.place(x=117,y=510)
                
                mm=Label(buscado,text=reserva.get())
                mm.config(font=("Century Gothic",10),height=1)
                mm.place(x=235,y=606)
                
                GG=Label(buscado,text=i.asiento)
                GG.config(font=("Century Gothic",10),height=1)
                GG.place(x=119,y=558)
                
                puerta=Label(buscado,text=i.puerta)
                puerta.config(font=("Century Gothic",10),height=1)
                puerta.place(x=303,y=651)
                
                embarque=Label(buscado,text="12:00 pm" if i.hora.get()=="1:00 pm" else "7:00 pm")
                embarque.config(font=("Century Gothic",10),height=1)
                embarque.place(x=229,y=651)
                
                hua=Label(buscado,text=i.hora.get())
                hua.config(font=("Century Gothic",10),height=1)
                hua.place(x=259,y=364)
#---.-------.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.                                                        
        buscado.mainloop()
        
        
    ventana2=Toplevel()
    ventana2.title("Buscar Registro")
    logo_buscar=PhotoImage(file="GG.png")
    buscarr=Label(ventana2,image=logo_buscar).pack()
    ventana2.resizable(0,0)
    ventana2.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
    #---CUadro para escribir el codigo de reserva    
    reserva=StringVar()
    reservita=Entry(ventana2,textvariable=str(reserva)).place(x=100,y=300)
            
    #------Boton Regresar
    back= Button(ventana2,text="Regresar", command=regresar)    
    back.config(font=("Century Gothic",10),height=1, width=9,cursor="hand2")
    back.place(x=12,y=25)
    
    #------Boton Buscar
    
    buscar= Button(ventana2,text="Buscar", command=ventana_buscado)
    buscar.config(font=("Century Gothic",10),height=1, width=7,cursor="hand2")
    buscar.place(x=150,y=350)
    ventana2.mainloop()
    
    

def window_view_register():
    def regresar():
        ventana3.state(newstate = "withdraw")
        ventana.state(newstate = "normal")
    
#---------- s ----------------- s ........... .
    def imprimir_texto():
        date=""
        cont=0        
        for i in datos:
            cont+=1
            a=str(i.nombre.get())
            b=str(i.apellido.get())
            c=str(i.DNI.get())
            d=str(i.destino.get())
            e=str(i.avion)
            f=str(i.mes.get())
            h=str(i.clase.get())
            v=str(i.sexo.get())
            day=str(i.dia.get())
            j="Lima"
            mm=str(i.reservex)
            
            GG=i.asiento
            puerta=i.puerta
            embarque="12:00 pm" if i.hora.get()=="1:00 pm" else "7:00 pm"
            valor=f"""              🛩️REGISTRO {cont} 🛩️\n\n   Nombre: {a}\n   Apellido: {b}\n   DNI: {c}\n   Destino: {d}\n   Avión: {e}\n   Día: {day}\n   Mes: {f}\n   Año: 2020\n   Clase: {h}\n   Sexo: {v}\n   Origen: {j}\n   Puerta: {puerta}\n   Reserva: {mm}\n   Hora: {i.hora.get()}\n   Embarque: {embarque}\n   Asiento: {GG}\n\n"""
            date+=valor
        return date
     #---------------------------------------------------       
    ventana3=Toplevel()
    ventana3.geometry("398x698")
    ventana3.title("Mostrar Registro")
    ventana3.configure(background='#01aed8')
    ventana3.resizable(0,0)
    
    ventana3.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
    #Scroolbar
    Sbar=Scrollbar(ventana3)
    Sbar.pack(side=RIGHT,fill="y")
    #-------------------------------
    texto=Text(ventana3,yscrollcommand=Sbar.set)
    texto.pack(expand=1,fill="x")
    
    #--------------------------------
    texto.insert(END,imprimir_texto())
    #--------------------------------
    Sbar.config(command=texto.yview)
    
    #-------Boton Regresar
    menu_principal= Button(ventana3,text="Regresar", command=regresar)    
    menu_principal.config(font=("Century Gothic",10),height=1, width=10,cursor="hand2")
    menu_principal.place(x=12,y=25)
    ventana3.mainloop()


#------INICIO------
ventana=Tk()
ventana.state(newstate = "normal")
ventana.title("UTEC-AIRLINES")
ventana.resizable(0,0)

fondo=PhotoImage(file="logo_UTEC.png")
lblImagen=Label(ventana, image=fondo).pack()

imaBoton=PhotoImage(file="nuevo_registro.png")
bton_new_register=Button(ventana,image=imaBoton,command=window_new_register,cursor="hand2").place(x=40,y=520)

imaBoton_2=PhotoImage(file="buscar_registro.png")
bton_search_register=Button(ventana,image=imaBoton_2,command=window_search_register,cursor="hand2").place(x=164,y=520)

imaBoton_3=PhotoImage(file="mostrar_registros.png")
bton_view_register=Button(ventana,image=imaBoton_3,command=window_view_register,cursor="hand2").place(x=288,y=520)

ventana.mainloop()
#----------------------------------




