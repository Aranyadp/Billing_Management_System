from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1555x845")
      self.root.minsize(350,300)
      #self.root.maxsize(1555,830)
      self.root.title("Billing Software")
      bg_colr="#95D989"
      title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_colr,fg="red",font=("times new roman",30,"bold"),pady=5)
      title.pack(fill=X)
      
      
      #===========================		Inner Work		==================================#
      
      #++++++++++++++++		Cosmetics		+++++++++++++++#
      
      self.soap=IntVar()
      self.lotion=IntVar()
      self.cream=IntVar()
      self.powder=IntVar()
      self.hair_g=IntVar()
      self.perfume=IntVar()
      self.body_o=IntVar()
      
      #++++++++++++++++		Cold Drinks		+++++++++++++++#
      
      self.pepsi=IntVar()
      self.sprite=IntVar()
      self.limca=IntVar()
      self.fizz=IntVar()
      self.mazza=IntVar()
      self.fanta=IntVar()
      self.appy=IntVar()
      
     #++++++++++++++++		Grocery		+++++++++++++++#
      
      self.rice=IntVar()
      self.wheat=IntVar()
      self.oil=IntVar()
      self.sugar=IntVar()
      self.tea=IntVar()
      self.salt=IntVar()
      self.spice=IntVar()
      
     #++++++++++++++++		Cloths		+++++++++++++++#
      
      self.shirt=IntVar()
      self.jeans=IntVar()
      self.top=IntVar()
      self.skirt=IntVar()
      self.pants=IntVar()
      self.belt=IntVar()
      self.saree=IntVar()
      
      #++++++++++++++		Customer	  +++++++++++++#
      
      self.cname=StringVar()
      self.cno=StringVar()
      
      self.bno=StringVar()
      x=random.randint(1,1000)
      self.bno.set(str(x))
      
      self.srch=StringVar()
      
      #+++++++++++++++		Goods Price & TAX		++++++++++++++++#

      self.m1=StringVar()
      self.m2=StringVar()
      self.m3=StringVar()
      self.m4=StringVar()
      self.m5=StringVar()
      self.m6=StringVar()
      self.m7=StringVar()
      self.m8=StringVar()
      
      
      #=================================		Customer Detail Frame	  ==================================#
      

      F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("arial",25,"bold"),fg="blue",bg=bg_colr)
      F1.place(x=6,y=81,width=1547)

      Cname_lbl = Label(F1,text="Customer Name :",bg=bg_colr,fg="white",font=("arial",20,"bold"))
      Cname_lbl.grid(row=0,column=0,padx=22,pady=5)
      Cname_txt = Entry(F1,width=20,textvariable=self.cname,font="arial 15")
      Cname_txt.grid(row=0,column=1,pady=5,padx=10)

      Cno_lbl = Label(F1,text="Contact No. :",bg=bg_colr,fg="white",font=("arial",20,"bold"))
      Cno_lbl.grid(row=0,column=3,padx=22,pady=5)
      Cno_txt = Entry(F1,width=15,textvariable=self.cno,font="arial 15")
      Cno_txt.grid(row=0,column=4,pady=5,padx=10)

      Bno_lbl = Label(F1,text="Bill No. :",bg=bg_colr,fg="white",font=("arial",20,"bold"))
      Bno_lbl.grid(row=0,column=5,padx=22,pady=5)
      Bno_txt = Entry(F1,width=12,textvariable=self.srch,font="arial 15")
      Bno_txt.grid(row=0,column=6,pady=5,padx=10)

      Srch_bttn = Button(F1,text="Search",command=self.find_bill,width=10,bd=10,font="arial 20 bold")
      Srch_bttn.grid(row=0,column=7,pady=15,padx=60)
      
      
      #===============================		Items Data		==========================#
	  
	  #++++++++++++++++++++		Cosmatics Products		++++++++++++++++#


      F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetic Items",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F2.place(x=6,y=227,width=305,height=400)

      Soap_lbl = Label(F2,text="Soap :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Soap_lbl.grid(row=0,column=0,padx=14,pady=10,sticky="w")
      Soap_txt = Entry(F2,width=11,textvariable=self.soap,font="arial 15")
      Soap_txt.grid(row=0,column=1,pady=10,padx=5)

      Lotion_lbl = Label(F2,text="Lotions :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Lotion_lbl.grid(row=1,column=0,padx=14,pady=10,sticky="w")
      Lotion_txt = Entry(F2,width=11,textvariable=self.lotion,font="arial 15")
      Lotion_txt.grid(row=1,column=1,pady=10,padx=5)

      Cream_lbl = Label(F2,text="Cream :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Cream_lbl.grid(row=2,column=0,padx=14,pady=10,sticky="w")
      Cream_txt = Entry(F2,width=11,textvariable=self.cream,font="arial 15")
      Cream_txt.grid(row=2,column=1,pady=10,padx=5)

      Powder_lbl = Label(F2,text="Powder :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Powder_lbl.grid(row=3,column=0,padx=14,pady=10,sticky="w")
      Powder_txt = Entry(F2,width=11,textvariable=self.powder,font="arial 15")
      Powder_txt.grid(row=3,column=1,pady=10,padx=5)

      Hair_g_lbl = Label(F2,text="Hair Gel :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Hair_g_lbl.grid(row=4,column=0,padx=14,pady=10,sticky="w")
      Hair_g_txt = Entry(F2,width=11,textvariable=self.hair_g,font="arial 15")
      Hair_g_txt.grid(row=4,column=1,pady=10,padx=5)
      
      Perfume_lbl = Label(F2,text="Perfume :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Perfume_lbl.grid(row=5,column=0,padx=14,pady=10,sticky="w")
      Perfume_txt = Entry(F2,width=11,textvariable=self.perfume,font="arial 15")
      Perfume_txt.grid(row=5,column=1,pady=10,padx=5)
      
      Body_o_lbl = Label(F2,text="Body Oil :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Body_o_lbl.grid(row=6,column=0,padx=14,pady=10,sticky="w")
      Body_o_txt = Entry(F2,width=11,textvariable=self.body_o,font="arial 15")
      Body_o_txt.grid(row=6,column=1,pady=10,padx=5)


      #+++++++++++++++++++++	Cold Drinks		++++++++++++++++++++++#


      F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F3.place(x=314,y=227,width=283,height=400)

      Pepsi_lbl = Label(F3,text="Pepsi :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Pepsi_lbl.grid(row=0,column=0,padx=15,pady=10,sticky="w")
      Pepsi_txt = Entry(F3,width=11,textvariable=self.pepsi,font="arial 15")
      Pepsi_txt.grid(row=0,column=1,pady=10,padx=6)

      Sprite_lbl = Label(F3,text="Sprite :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Sprite_lbl.grid(row=1,column=0,padx=15,pady=10,sticky="w")
      Sprite_txt = Entry(F3,width=11,textvariable=self.sprite,font="arial 15")
      Sprite_txt.grid(row=1,column=1,pady=10,padx=6)

      Limca_lbl = Label(F3,text="Limca :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Limca_lbl.grid(row=2,column=0,padx=15,pady=10,sticky="w")
      Limca_txt = Entry(F3,width=11,textvariable=self.limca,font="arial 15")
      Limca_txt.grid(row=2,column=1,pady=10,padx=6)

      Fizz_lbl = Label(F3,text="Fizz :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Fizz_lbl.grid(row=3,column=0,padx=15,pady=10,sticky="w")
      Fizz_txt = Entry(F3,width=11,textvariable=self.fizz,font="arial 15")
      Fizz_txt.grid(row=3,column=1,pady=10,padx=6)

      Mazza_lbl = Label(F3,text="Mazza :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Mazza_lbl.grid(row=4,column=0,padx=15,pady=10,sticky="w")
      Mazza_txt = Entry(F3,width=11,textvariable=self.mazza,font="arial 15")
      Mazza_txt.grid(row=4,column=1,pady=10,padx=6)
      
      Fanta_lbl = Label(F3,text="Fanta :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Fanta_lbl.grid(row=5,column=0,padx=15,pady=10,sticky="w")
      Fanta_txt = Entry(F3,width=11,textvariable=self.fanta,font="arial 15")
      Fanta_txt.grid(row=5,column=1,pady=10,padx=6)
      
      Appy_lbl = Label(F3,text="Appy :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Appy_lbl.grid(row=6,column=0,padx=15,pady=10,sticky="w")
      Appy_txt = Entry(F3,width=11,textvariable=self.appy,font="arial 15")
      Appy_txt.grid(row=6,column=1,pady=10,padx=6)


      #++++++++++++++++++++		Grocery Items	++++++++++++++++++#


      F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F4.place(x=600,y=227,width=283,height=400)

      Rice_lbl = Label(F4,text="Rice :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Rice_lbl.grid(row=0,column=0,padx=15,pady=10,sticky="w")
      Rice_txt = Entry(F4,width=11,textvariable=self.rice,font="arial 15")
      Rice_txt.grid(row=0,column=1,pady=10,padx=6)

      Wheat_lbl = Label(F4,text="Wheat :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Wheat_lbl.grid(row=1,column=0,padx=15,pady=10,sticky="w")
      Wheat_txt = Entry(F4,width=11,textvariable=self.wheat,font="arial 15")
      Wheat_txt.grid(row=1,column=1,pady=10,padx=6)

      Oil_lbl = Label(F4,text="Oil :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Oil_lbl.grid(row=2,column=0,padx=15,pady=10,sticky="w")
      Oil_txt = Entry(F4,width=11,textvariable=self.oil,font="arial 15")
      Oil_txt.grid(row=2,column=1,pady=10,padx=6)

      Sugar_lbl = Label(F4,text="Sugar :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Sugar_lbl.grid(row=3,column=0,padx=15,pady=10,sticky="w")
      Sugar_txt = Entry(F4,width=11,textvariable=self.sugar,font="arial 15")
      Sugar_txt.grid(row=3,column=1,pady=10,padx=6)

      Tea_lbl = Label(F4,text="Tea :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Tea_lbl.grid(row=4,column=0,padx=15,pady=10,sticky="w")
      Tea_txt = Entry(F4,width=11,textvariable=self.tea,font="arial 15")
      Tea_txt.grid(row=4,column=1,pady=10,padx=6)
      
      Salt_lbl = Label(F4,text="Salt :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Salt_lbl.grid(row=5,column=0,padx=15,pady=10,sticky="w")
      Salt_txt = Entry(F4,width=11,textvariable=self.salt,font="arial 15")
      Salt_txt.grid(row=5,column=1,pady=10,padx=6)
      
      Spice_lbl = Label(F4,text="Spice :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Spice_lbl.grid(row=6,column=0,padx=15,pady=10,sticky="w")
      Spice_txt = Entry(F4,width=11,textvariable=self.spice,font="arial 15")
      Spice_txt.grid(row=6,column=1,pady=10,padx=6)
      
      
      #++++++++++++++++++++		Cloth Items	++++++++++++++++++#


      F5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cloths",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F5.place(x=886,y=227,width=283,height=400)

      Shirt_lbl = Label(F5,text="Shirt :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Shirt_lbl.grid(row=0,column=0,padx=15,pady=10,sticky="w")
      Shirt_txt = Entry(F5,width=11,textvariable=self.shirt,font="arial 15")
      Shirt_txt.grid(row=0,column=1,pady=10,padx=6)

      Jeans_lbl = Label(F5,text="Jeans :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Jeans_lbl.grid(row=1,column=0,padx=15,pady=10,sticky="w")
      Jeans_txt = Entry(F5,width=11,textvariable=self.jeans,font="arial 15")
      Jeans_txt.grid(row=1,column=1,pady=10,padx=6)

      Top_lbl = Label(F5,text="Top :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Top_lbl.grid(row=2,column=0,padx=15,pady=10,sticky="w")
      Top_txt = Entry(F5,width=11,textvariable=self.top,font="arial 15")
      Top_txt.grid(row=2,column=1,pady=10,padx=6)

      Skirt_lbl = Label(F5,text="Skirt :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Skirt_lbl.grid(row=3,column=0,padx=15,pady=10,sticky="w")
      Skirt_txt = Entry(F5,width=11,textvariable=self.skirt,font="arial 15")
      Skirt_txt.grid(row=3,column=1,pady=10,padx=6)

      Pants_lbl = Label(F5,text="Pants :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Pants_lbl.grid(row=4,column=0,padx=15,pady=10,sticky="w")
      Pants_txt = Entry(F5,width=11,textvariable=self.pants,font="arial 15")
      Pants_txt.grid(row=4,column=1,pady=10,padx=6)
      
      Belt_lbl = Label(F5,text="Belt :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Belt_lbl.grid(row=5,column=0,padx=15,pady=10,sticky="w")
      Belt_txt = Entry(F5,width=11,textvariable=self.belt,font="arial 15")
      Belt_txt.grid(row=5,column=1,pady=10,padx=6)
      
      Saree_lbl = Label(F5,text="Saree :",bg=bg_colr,fg="white",font=("arial",15,"bold"))
      Saree_lbl.grid(row=6,column=0,padx=15,pady=10,sticky="w")
      Saree_txt = Entry(F5,width=11,textvariable=self.saree,font="arial 15")
      Saree_txt.grid(row=6,column=1,pady=10,padx=6)
      
      
      #============================		Bill Area	  ============================#
      
      
      F6=Frame(self.root,bg=bg_colr,bd=10,relief=GROOVE)
      F6.place(x=1172,y=227,width=381,height=510)
      bill_title=Label(F6,text="Bill Area",fg="green",bg="lightyellow",font="arial 15 bold",bd=7,relief=GROOVE)
      bill_title.pack(fill=X)
      scrol_y=Scrollbar(F6,orient=VERTICAL)
      self.txtarea=Text(F6,bg="lightgrey",yscrollcommand=scrol_y.set)
      scrol_y.pack(side=RIGHT,fill=Y)
      scrol_y.config(command=self.txtarea.yview)
      self.txtarea.pack(fill=BOTH,expand=1)

      
      #====================== 		Price and TAX Frame 	=========================#
      
      
      F7=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F7.place(x=6,y=629,width=877,height=215)
      
      M1_lbl=Label(F7,text="Total Cosmetics Price : ",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M1_lbl.grid(row=0,column=0,padx=18,pady=3,sticky="w")
      M1_txt=Entry(F7,width=18,textvariable=self.m1,font="arial 11 bold",bd=7,relief=SUNKEN)
      M1_txt.grid(row=0,column=1,padx=9,pady=3)
      
      M2_lbl=Label(F7,text="Total Cold Drinks Price : ",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M2_lbl.grid(row=1,column=0,padx=18,pady=3,sticky="w")
      M2_txt=Entry(F7,width=18,textvariable=self.m2,font="arial 11 bold",bd=7,relief=SUNKEN)
      M2_txt.grid(row=1,column=1,padx=9,pady=3)
      
      M3_lbl=Label(F7,text="Total Groceries Price : ",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M3_lbl.grid(row=2,column=0,padx=18,pady=3,sticky="w")
      M3_txt=Entry(F7,width=18,textvariable=self.m3,font="arial 11 bold",bd=7,relief=SUNKEN)
      M3_txt.grid(row=2,column=1,padx=9,pady=3)
      
      M4_lbl=Label(F7,text="Total Groceries Price 1 : ",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M4_lbl.grid(row=3,column=0,padx=18,pady=3,sticky="w")
      M4_txt=Entry(F7,width=18,textvariable=self.m4,font="arial 11 bold",bd=7,relief=SUNKEN)
      M4_txt.grid(row=3,column=1,padx=9,pady=3)
      
      M5_lbl=Label(F7,text="Cosmetics TAX :",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M5_lbl.grid(row=0,column=2,padx=18,pady=3,sticky="w")
      M5_txt=Entry(F7,width=18,textvariable=self.m5,font="arial 11 bold",bd=7,relief=SUNKEN)
      M5_txt.grid(row=0,column=3,padx=9,pady=3)
      
      M6_lbl=Label(F7,text="Cold Drinks TAX :",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M6_lbl.grid(row=1,column=2,padx=18,pady=3,sticky="w")
      M6_txt=Entry(F7,width=18,textvariable=self.m6,font="arial 11 bold",bd=7,relief=SUNKEN)
      M6_txt.grid(row=1,column=3,padx=9,pady=3)
      
      M7_lbl=Label(F7,text="Groceries TAX :",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M7_lbl.grid(row=2,column=2,padx=18,pady=3,sticky="w")
      M7_txt=Entry(F7,width=18,textvariable=self.m7,font="arial 11 bold",bd=7,relief=SUNKEN)
      M7_txt.grid(row=2,column=3,padx=9,pady=3)
      
      M8_lbl=Label(F7,text="Groceries 1 TAX :",bg=bg_colr,fg="red",font=("times new roman",15,"bold"))
      M8_lbl.grid(row=3,column=2,padx=18,pady=3,sticky="w")
      M8_txt=Entry(F7,width=18,textvariable=self.m8,font="arial 11 bold",bd=7,relief=SUNKEN)
      M8_txt.grid(row=3,column=3,padx=9,pady=3)
      
      
      #============================	 	 Button Frame	   ============================#
      
      #++++++++++++++++++++ 	Bill Button		++++++++++++++++#
      
      F8=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Generate",font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F8.place(x=886,y=629,width=283,height=215)
      
      total_btn=Button(F8,command=self.total,text="Total Bill",font="arial 15 bold",bd=7,bg="white",fg="blue",pady=12,width=8)
      total_btn.grid(row=0,column=0,padx=55,pady=7)
      
      bill_gen_btn=Button(F8,text="Generate Bill",command=self.bill_area,font="arial 15 bold",bd=7,bg="white",fg="blue",pady=12,width=12)
      bill_gen_btn.grid(row=1,column=0,padx=45,pady=7)
      
      
      #+++++++++++++++++++		Exit & Clear Button		++++++++++++++++++++++#
      
      F9=LabelFrame(self.root,bd=10,relief=GROOVE,font=("arial",22,"bold"),fg="blue",bg=bg_colr)
      F9.place(x=1172,y=741,width=381,height=102)
      
      clear_btn=Button(F9,text="Clear",command=self.clear_data,font="arial 16 bold",bd=7,bg="white",fg="blue",pady=12,width=8)
      clear_btn.grid(row=0,column=0,padx=25,pady=7)
      
      exit_btn=Button(F9,text="EXIT",command=self.EXIT_app,font="arial 15 bold",bd=7,bg="white",fg="blue",pady=12,width=8)
      exit_btn.grid(row=0,column=1,padx=20,pady=7)
      
      self.bill_entry()
      
    
    #=======================		Calculate Area 		=======================#
    
    def total(self):
      
      #+++++++++++		Store the Cosmetic Price		+++++++++++#
      
      self.c1_p = self.soap.get()*40
      self.c2_p = self.lotion.get()*40
      self.c3_p = self.cream.get()*40
      self.c4_p = self.powder.get()*40
      self.c5_p = self.hair_g.get()*40
      self.c6_p = self.perfume.get()*40
      self.c7_p = self.body_o.get()*40
      
      #+++++++++++    Cosmetic   &&   Cosmetics TAX  Total    ++++++++++#
      
      self.cosmetic_price=float(self.c1_p + self.c2_p + self.c3_p + self.c4_p + self.c5_p + self.c6_p + self.c7_p)
      
      self.m1.set("Rs/- "+str(self.cosmetic_price))

      self.c_TAX=round((self.cosmetic_price*0.18),2)
      
      self.m5.set("Rs/- "+str(self.c_TAX))

      self.T_C_P = self.cosmetic_price + self.c_TAX
      
      
      #+++++++++++		Store the Cold Drinks Price		+++++++++++#
      
      self.cd1_p = self.pepsi.get()*40
      self.cd2_p = self.sprite.get()*40
      self.cd3_p = self.limca.get()*40
      self.cd4_p = self.fizz.get()*40
      self.cd5_p = self.mazza.get()*40
      self.cd6_p = self.fanta.get()*40
      self.cd7_p = self.appy.get()*40
      
     #++++++++++ Cold Drinks   &&   Cold Drinks TAX  Total      ++++++++++#
      
      self.cold_drinks_price=float(self.cd1_p + self.cd2_p + self.cd3_p + self.cd4_p + self.cd5_p + self.cd6_p + self.cd7_p)
      
      self.m2.set("Rs/- "+str(self.cold_drinks_price))

      self.cd_TAX=round((self.cold_drinks_price*0.18),2)
      
      self.m6.set("Rs/- "+str(self.cd_TAX))

      self.T_Cd_P = self.cold_drinks_price + self.cd_TAX
      
      
      #+++++++++++		Store the Grocery Price		+++++++++++#
      
      self.g1_p = self.rice.get()*40
      self.g2_p = self.wheat.get()*40
      self.g3_p = self.oil.get()*40
      self.g4_p = self.sugar.get()*40
      self.g5_p = self.tea.get()*40
      self.g6_p = self.salt.get()*40
      self.g7_p = self.spice.get()*40
     
     #++++++++++++      Grocery  &&  Grocery TAX  Total       +++++++++#
      
      self.grocery_price=float(self.g1_p + self.g2_p + self.g3_p + self.g4_p + self.g5_p + self.g6_p + self.g7_p)
      
      self.m3.set("Rs/- "+str(self.grocery_price))

      self.g_TAX=round((self.grocery_price*0.18),2)
      
      self.m7.set("Rs/- "+str(self.g_TAX))

      self.T_G_P = self.grocery_price + self.g_TAX
      
      
      #+++++++++++		Store the Cloths Price		+++++++++++#
      
      self.cl1_p = self.shirt.get()*40
      self.cl2_p = self.jeans.get()*40
      self.cl3_p = self.top.get()*40
      self.cl4_p = self.skirt.get()*40
      self.cl5_p = self.pants.get()*40
      self.cl6_p = self.belt.get()*40
      self.cl7_p = self.saree.get()*40
      
      #++++++++++++      Cloths  && Cloths TAX Total       +++++++++#
      
      self.cloth_price=float(self.cl1_p + self.cl2_p + self.cl3_p + self.cl4_p + self.cl5_p + self.cl6_p + self.cl7_p)
      
      self.m4.set("Rs/- "+str(self.cloth_price))

      self.cl_TAX=round((self.cloth_price*0.18),2)
      
      self.m8.set("Rs/- "+str(self.cl_TAX))

      self.T_Cl_P = self.cloth_price + self.cl_TAX


      #++++++++++++      All Items  &&  TAX Total       +++++++++#

      self.Total_Bill = float ( self.T_C_P + self.T_Cd_P + self.T_G_P + self.T_Cl_P )
      
      
      #========================      Total Bill Area       ==========================#
      
      #++++++++++++++		Customer Details		++++++++++++++++#
    
    def bill_entry(self):
      self.txtarea.delete('1.0',END)
      
      self.txtarea.insert(END,"\t\t-: WELCOME :-")
      self.txtarea.insert(END,f"\n\n Bill Number : {self.bno.get()}")
      self.txtarea.insert(END,f"\n Customer Name : {self.cname.get()}")
      self.txtarea.insert(END,f"\n Phone Number : {self.cno.get()}")
      
      self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")
      self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")
      
      self.txtarea.insert(END,"\n\n Products\t\t Quantity\t\t Price")
      
      self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")
      self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __\n")
      
      
      #++++++++++++		Bill Generate Area		+++++++++++++#
      
    def bill_area(self):

      if self.cname.get()=="" or self.cno.get()=="" :
        messagebox.showerror("ERROR","Customer Details are must!!!")

      elif self.m1.get()=="Rs/- 0.0" and self.m2.get()=="Rs/- 0.0" and self.m3.get()=="Rs/- 0.0" and self.m4.get()=="Rs/- 0.0" :
        messagebox.showerror("ERROR","No Product Purchased...")

      else :
        self.bill_entry()
      
        #++++++++++++		Cosmetic Bill Area		+++++++++++++#
      
        if self.soap.get()!=0:
          self.txtarea.insert(END,f"\n Soap\t\t  {self.soap.get()}\t\t  {self.c1_p}")
        
        if self.lotion.get()!=0:
          self.txtarea.insert(END,f"\n Lotions\t\t  {self.lotion.get()}\t\t  {self.c2_p}")
        
        if self.cream.get()!=0:
          self.txtarea.insert(END,f"\n Cream\t\t  {self.cream.get()}\t\t  {self.c3_p}")
        
        if self.powder.get()!=0:
          self.txtarea.insert(END,f"\n Powder\t\t  {self.powder.get()}\t\t  {self.c4_p}")
        
        if self.hair_g.get()!=0:
          self.txtarea.insert(END,f"\n Hair Gel\t\t  {self.hair_g.get()}\t\t  {self.c5_p}")
        
        if self.perfume.get()!=0:
          self.txtarea.insert(END,f"\n Perfume\t\t  {self.perfume.get()}\t\t  {self.c6_p}")
        
        if self.body_o.get()!=0:
          self.txtarea.insert(END,f"\n Body Oil\t\t  {self.body_o.get()}\t\t  {self.c7_p}")
        
        #++++++++++++		Cold Drinks Bill Area		+++++++++++++#
      
        if self.pepsi.get()!=0:
          self.txtarea.insert(END,f"\n Pepsi\t\t  {self.pepsi.get()}\t\t  {self.cd1_p}")
        
        if self.sprite.get()!=0:
          self.txtarea.insert(END,f"\n Sprite\t\t  {self.sprite.get()}\t\t  {self.cd2_p}")
        
        if self.limca.get()!=0:
          self.txtarea.insert(END,f"\n Limca\t\t  {self.limca.get()}\t\t  {self.cd3_p}")
        
        if self.fizz.get()!=0:
          self.txtarea.insert(END,f"\n Fizz\t\t  {self.fizz.get()}\t\t  {self.cd4_p}")
        
        if self.mazza.get()!=0:
          self.txtarea.insert(END,f"\n Mazza\t\t  {self.mazza.get()}\t\t  {self.cd5_p}")
        
        if self.fanta.get()!=0:
          self.txtarea.insert(END,f"\n Fanta\t\t  {self.fanta.get()}\t\t  {self.cd6_p}")
        
        if self.appy.get()!=0:
          self.txtarea.insert(END,f"\n Appy\t\t  {self.appy.get()}\t\t  {self.cd7_p}")
        
        #++++++++++++		Grocery Bill Area		+++++++++++++#
      
        if self.rice.get()!=0:
          self.txtarea.insert(END,f"\n Rice\t\t  {self.rice.get()}\t\t  {self.g1_p}")
        
        if self.wheat.get()!=0:
          self.txtarea.insert(END,f"\n Wheat\t\t  {self.wheat.get()}\t\t  {self.g2_p}")
        
        if self.oil.get()!=0:
          self.txtarea.insert(END,f"\n Oil\t\t  {self.oil.get()}\t\t  {self.g3_p}")
        
        if self.sugar.get()!=0:
          self.txtarea.insert(END,f"\n Sugar\t\t  {self.sugar.get()}\t\t  {self.g4_p}")
        
        if self.tea.get()!=0:
          self.txtarea.insert(END,f"\n Tea\t\t  {self.tea.get()}\t\t  {self.g5_p}")
        
        if self.salt.get()!=0:
          self.txtarea.insert(END,f"\n Salt\t\t  {self.salt.get()}\t\t  {self.g6_p}")
        
        if self.spice.get()!=0:
          self.txtarea.insert(END,f"\n Spice\t\t  {self.spice.get()}\t\t  {self.g7_p}")
        
        #++++++++++++		Cloths Bill Area		+++++++++++++#
      
        if self.shirt.get()!=0:
          self.txtarea.insert(END,f"\n Shirt\t\t  {self.shirt.get()}\t\t  {self.cl1_p}")
        
        if self.jeans.get()!=0:
          self.txtarea.insert(END,f"\n Jeans\t\t  {self.jeans.get()}\t\t  {self.cl2_p}")
        
        if self.top.get()!=0:
          self.txtarea.insert(END,f"\n Top\t\t  {self.top.get()}\t\t  {self.cl3_p}")
        
        if self.skirt.get()!=0:
          self.txtarea.insert(END,f"\n Skirt\t\t  {self.skirt.get()}\t\t  {self.cl4_p}")
        
        if self.pants.get()!=0:
          self.txtarea.insert(END,f"\n Pants\t\t  {self.pants.get()}\t\t  {self.cl5_p}")
        
        if self.belt.get()!=0:
          self.txtarea.insert(END,f"\n Belt\t\t  {self.belt.get()}\t\t  {self.cl6_p}")
        
        if self.saree.get()!=0:
          self.txtarea.insert(END,f"\n Saree\t\t  {self.saree.get()}\t\t  {self.cl7_p}")
        
      
        #+++++++++++++++ 		TAX Bill Generate Area		++++++++++++++++#
       
        self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")
        self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __\n")

        if self.m5.get()!="Rs/- 0.0" :
          self.txtarea.insert(END,f"\n Cosmetic TAX   :\t\t\t\t{self.m5.get()}")
      

        if self.m6.get()!="Rs/- 0.0" :
          self.txtarea.insert(END,f"\n Cold Drink TAX :\t\t\t\t{self.m6.get()}")
      

        if self.m7.get()!="Rs/- 0.0" :
          self.txtarea.insert(END,f"\n Grocery TAX    :\t\t\t\t{self.m7.get()}")
      

        if self.m8.get()!="Rs/- 0.0" :
          self.txtarea.insert(END,f"\n Cloths TAX     :\t\t\t\t{self.m8.get()}")
      
        self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")
        self.txtarea.insert(END,"\n __ __ __ __ __ __ __ __ __ __ __ __ __ __")

        self.txtarea.insert(END,f"\n\n Total Bill     :\t\t\t\tRs/- {self.Total_Bill}")

        self.save_bill()
      
    def save_bill(self):
      op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill???")
      if op>0 :
        self.bill_data=self.txtarea.get('1.0',END)
        a1=open("Bill Store/"+str(self.bno.get())+".txt","w")
        a1.write(self.bill_data)
        a1.close()
        messagebox.showinfo("Saved",f"Bill {self.bno.get()} saved Successfully")
      else:
        return


    def find_bill(self):
      present="no"
      for i in os.listdir("Bill Store/"):
        if i.split('.')[0]==self.srch.get():
          a1=open(f"Bill Store/{i}","r")
          self.txtarea.delete('1.0',END)
          for d in a1:
            self.txtarea.insert(END,d)
          a1.close()
          present="yes"

      if present=="no":
        messagebox.showerror("ERROR","Invalid Bill Number...")


    def clear_data(self):

      op=messagebox.askyesno("Clear","Do You Want To Clear ???")
      if op>0:

        #===========================		Inner Work		==================================#
      
        #++++++++++++++++		Cosmetics		+++++++++++++++#
      
        self.soap.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.powder.set(0)
        self.hair_g.set(0)
        self.perfume.set(0)
        self.body_o.set(0)
      
        #++++++++++++++++		Cold Drinks		+++++++++++++++#
      
        self.pepsi.set(0)
        self.sprite.set(0)
        self.limca.set(0)
        self.fizz.set(0)
        self.mazza.set(0)
        self.fanta.set(0)
        self.appy.set(0)
      
       #++++++++++++++++		Grocery		+++++++++++++++#
      
        self.rice.set(0)
        self.wheat.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        self.salt.set(0)
        self.spice.set(0)
      
       #++++++++++++++++		Cloths		+++++++++++++++#
      
        self.shirt.set(0)
        self.jeans.set(0)
        self.top.set(0)
        self.skirt.set(0)
        self.pants.set(0)
        self.belt.set(0)
        self.saree.set(0)
      
        #++++++++++++++		Customer	  +++++++++++++#
      
        self.cname.set("")
        self.cno.set("")
      
        self.bno.set("")
        x=random.randint(1,1000)
        self.bno.set(str(x))
      
        self.srch.set("")
      
        #+++++++++++++++		Goods Price & TAX		++++++++++++++++#

        self.m1.set("")
        self.m2.set("")
        self.m3.set("")
        self.m4.set("")
        self.m5.set("")
        self.m6.set("")
        self.m7.set("")
        self.m8.set("")

      
        self.bill_entry()
      

    def EXIT_app(self):
      op=messagebox.askyesno("EXIT","Do You Want To EXIT ???")
      if op>0:
        self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()
