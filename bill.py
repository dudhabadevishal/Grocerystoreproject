from email import message
from fileinput import close
from importlib.resources import path
from msilib.schema import AppId
from tkinter import *
import math,random,os
from setuptools import Command
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Grocery Shop Bill")
        bg_color="#2F4F4F"
        title=Label(self.root,text="Grocery Shop Bill",bd=12,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #===============Variables==============
        #===============Cosmetic==============
        self.Soap=IntVar()
        self.Face_cream=IntVar()
        self.Powder=IntVar()
        self.Hair_oil=IntVar()
        self.Body_lotion=IntVar()
        self.Hair_gel=IntVar()
        self.Body_spray=IntVar()

        #==============Grocery=============
        self.Wheat=IntVar()
        self.Food_oil=IntVar()
        self.Daal=IntVar()
        self.Rice=IntVar()
        self.Sugar=IntVar()
        self.Tea=IntVar()
        self.Detergent=IntVar()

        #============Cold Drinks==========
        self.Fruti=IntVar()
        self.Sprite=IntVar()
        self.Maza=IntVar()
        self.Cock=IntVar()
        self.Appy=IntVar()
        self.Slice=IntVar()
        self.Thumbsup=IntVar()

       #=========Total Product Price & Tax Variable=======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #=========Customer=========
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()


        #===============Customer Details Frame================

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15").grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Mobile No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15").grid(row=0,column=3,pady=5,padx=10)
  
        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15").grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


        #================Cosmatics Frame================

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_Soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_Soap_txt=Entry(F2,width=10,textvariable=self.Soap,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.Face_cream,font=("times new roman",16,"bold")).grid(row=1,column=1,padx=10,pady=10)

        Powder_lbl=Label(F2,text="Powder",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Powder_txt=Entry(F2,width=10,textvariable=self.Powder,font=("times new roman",16,"bold")).grid(row=2,column=1,padx=10,pady=10)
        
        Hair_oil_lbl=Label(F2,text="Hair oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_oil_txt=Entry(F2,width=10,textvariable=self.Hair_oil,font=("times new roman",16,"bold")).grid(row=3,column=1,padx=10,pady=10)

        Body_lotionlbl=Label(F2,text="Body lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Body_lotion_txt=Entry(F2,width=10,textvariable=self.Body_lotion,font=("times new roman",16,"bold")).grid(row=4,column=1,padx=10,pady=10)
    
        Hair_gel_lbl=Label(F2,text="Hair gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Hair_gel_txt=Entry(F2,width=10,textvariable=self.Hair_gel,font=("times new roman",16,"bold")).grid(row=5,column=1,padx=10,pady=10)
  
        Body_spray_lbl=Label(F2,text="Body spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Body_spray_txt=Entry(F2,width=10,textvariable=self.Body_spray,font=("times new roman",16,"bold")).grid(row=6,column=1,padx=10,pady=10)


        #================Grocery Frame================

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery Product",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        Wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt=Entry(F3,width=10,textvariable=self.Wheat,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=10,pady=10)

        Food_Oil_lbl=Label(F3,text="Food oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_Oil_txt=Entry(F3,width=10,textvariable=self.Food_oil,font=("times new roman",16,"bold")).grid(row=1,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_txt=Entry(F3,width=10,textvariable=self.Daal,font=("times new roman",16,"bold")).grid(row=2,column=1,padx=10,pady=10)
        
        Rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Rice_txt=Entry(F3,width=10,textvariable=self.Rice,font=("times new roman",16,"bold")).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt=Entry(F3,width=10,textvariable=self.Sugar,font=("times new roman",16,"bold")).grid(row=4,column=1,padx=10,pady=10)
    
        Tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_txt=Entry(F3,width=10,textvariable=self.Tea,font=("times new roman",16,"bold")).grid(row=5,column=1,padx=10,pady=10)
  
        Detergant_lbl=Label(F3,text="Detergant",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Detergant_txt=Entry(F3,width=10,textvariable=self.Detergent,font=("times new roman",16,"bold")).grid(row=6,column=1,padx=10,pady=10)

        #================Cold Drink Frame================

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Fruti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.Fruti,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.Sprite,font=("times new roman",16,"bold")).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.Maza,font=("times new roman",16,"bold")).grid(row=2,column=1,padx=10,pady=10)
        
        c4_lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.Cock,font=("times new roman",16,"bold")).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Appy",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.Appy,font=("times new roman",16,"bold")).grid(row=4,column=1,padx=10,pady=10)
    
        c6_lbl=Label(F4,text="Slice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.Slice,font=("times new roman",16,"bold")).grid(row=5,column=1,padx=10,pady=10)
  
        c7_lbl=Label(F4,text="Thumbs up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F4,width=10,textvariable=self.Thumbsup,font=("times new roman",16,"bold")).grid(row=6,column=1,padx=10,pady=10)

       #===========Bill Area============

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=340,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===========Button Frame===========

        F6=LabelFrame(self.root,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.grocery_price).grid(row=1,column=1,padx=5,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.cold_drink,font="arial 10 bold").grid(row=2,column=1,padx=5,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.cosmetic_tax).grid(row=0,column=3,padx=5,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.grocery_tax).grid(row=1,column=3,padx=5,pady=1)

        c3_lbl=Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",).grid(row=2,column=3,padx=5,pady=1)

        btn_F=Frame(F6,relief=GROOVE)
        btn_F.place(x=750,width=585,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="blue",fg="white",pady=6,width=6,font="arail 12 bold").grid(row=1,column=0,padx=4,pady=4)
        GenBill_btn=Button(btn_F,text="Gen Bill",command=self.bill_area,bg="blue",fg="white",pady=6,width=6,font="arail 12 bold").grid(row=1,column=1,padx=4,pady=4)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="blue",fg="white",pady=6,width=6,font="arail 12 bold").grid(row=1,column=2,padx=4,pady=4)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="blue",fg="white",pady=6,width=6,font="arail 12 bold").grid(row=1,column=3,padx=4,pady=4)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.Soap.get()*40
        self.c_fc_p=self.Face_cream.get()*120
        self.c_p_p=self.Powder.get()*60
        self.c_ho_p=self.Hair_oil.get()*180
        self.c_bl_p=self.Body_lotion.get()*140
        self.c_hg_p=self.Hair_gel.get()*180
        self.c_bs_p=self.Body_spray.get()*250

        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_p_p+
                                    self.c_ho_p+
                                    self.c_bl_p+
                                    self.c_hg_p+
                                    self.c_bs_p
                                    )                

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_w_p=self.Wheat.get()*200
        self.g_f_p=self.Food_oil.get()*115
        self.g_d_p=self.Daal.get()*95
        self.g_r_p=self.Rice.get()*110
        self.g_s_p=self.Sugar.get()*85
        self.g_t_p=self.Tea.get()*95
        self.g_d_p=self.Detergent.get()*105

        self.total_grocery_price=float(
                                    self.g_w_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_r_p+
                                    self.g_s_p+
                                    self.g_t_p+
                                    self.g_d_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_f_p=self.Fruti.get()*190
        self.d_s_p=self.Sprite.get()*80
        self.d_m_p=self.Maza.get()*76
        self.d_c_p=self.Cock.get()*155
        self.d_a_p=self.Appy.get()*110
        self.d_s_p=self.Slice.get()*95
        self.d_t_p=self.Thumbsup.get()*85

        self.total_cold_drink_price=float(
                                       self.d_f_p+
                                       self.d_s_p+
                                       self.d_m_p+
                                       self.d_c_p+
                                       self.d_a_p+
                                       self.d_s_p+
                                       self.d_t_p
                                       )
        self.cold_drink.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                            )
        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Prayas Retail\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()} ")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")
        
        

        

    def bill_area(self): 
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink.get()=="Rs. 0.0" :    
            messagebox.showerror("Error","No Product Select")
        else:      
          self.welcome_bill()
        #====cosmetics=====
        if self.Soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.Soap.get()}\t\t{self.c_s_p}")
        if self.Face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.Face_cream.get()}\t\t{self.c_fc_p}")
        if self.Powder.get()!=0:
            self.txtarea.insert(END,f"\n Powder\t\t{self.Powder.get()}\t\t{self.c_p_p}")
        if self.Hair_oil.get()!=0:
            self.txtarea.insert(END,f"\n Hair Oil\t\t{self.Hair_oil.get()}\t\t{self.c_ho_p}")
        if self.Body_lotion.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t{self.Body_lotion.get()}\t\t{self.c_bl_p}")
        if self.Hair_gel.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gel\t\t{self.Hair_gel.get()}\t\t{self.c_hg_p}")
        if self.Body_spray.get()!=0:
            self.txtarea.insert(END,f"\n Body Spray\t\t{self.Body_spray.get()}\t\t{self.c_bs_p}")
                                    
        #====Grocery=====
        if self.Wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.Wheat.get()}\t\t{self.g_w_p}")
        if self.Food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food oil\t\t{self.Food_oil.get()}\t\t{self.g_f_p}")
        if self.Daal.get()!=0:
            self.txtarea.insert(END,f"\n Daal\t\t{self.Daal.get()}\t\t{self.g_d_p}")
        if self.Rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.Rice.get()}\t\t{self.g_r_p}")
        if self.Sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.Sugar.get()}\t\t{self.g_s_p}")
        if self.Tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t{self.Tea.get()}\t\t{self.g_t_p}")
        if self.Detergent.get()!=0:
            self.txtarea.insert(END,f"\n Detergent\t\t{self.Detergent.get()}\t\t{self.g_d_p}")
        
         #====Drinks=====
        if self.Fruti.get()!=0:
            self.txtarea.insert(END,f"\n Fruti\t\t{self.Fruti.get()}\t\t{self.d_f_p}")
        if self.Sprite.get()!=0:
            self.txtarea.insert(END,f"\n Sprite\t\t{self.Sprite.get()}\t\t{self.d_s_p}")
        if self.Maza.get()!=0:
            self.txtarea.insert(END,f"\n Maza\t\t{self.Maza.get()}\t\t{self.d_m_p}")
        if self.Cock.get()!=0:
            self.txtarea.insert(END,f"\n Cock\t\t{self.Cock.get()}\t\t{self.d_c_p}")
        if self.Appy.get()!=0:
            self.txtarea.insert(END,f"\n Appy\t\t{self.Appy.get()}\t\t{self.d_a_p}")
        if self.Slice.get()!=0:
            self.txtarea.insert(END,f"\n Slice\t\t{self.Slice.get()}\t\t{self.d_s_p}")
        if self.Thumbsup.get()!=0:
            self.txtarea.insert(END,f"\n Thumbsup\t\t{self.Thumbsup.get()}\t\t{self.d_t_p}")
        
        self.txtarea.insert(END,f"\n-------------------------------------")
        if self.cosmetic_tax.get()!="Rs. 0.0":
           self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
        
        if self.grocery_tax.get()!="Rs. 0.0":
           self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

        if self.cold_drink_tax.get()!="Rs. 0.0":
           self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")   

        self.txtarea.insert(END,f"\n Total Bill :\t\t\t Rs. {self.Total_bill}")   
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()}saved Successfully")

        else:
            return    

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                  f1=open(f"bills/{i}","r")
                  self.txtarea.delete('1.0',END)
                  for d in f1:
                      self.txtarea.insert(END,d)
                  f1=close()
                  present="yes"

        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")   


    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:

        
            #===============Cosmetic==============
            self.Soap.set(0)
            self.Face_cream.set(0)
            self.Powder.set(0)
            self.Hair_oil.set(0)
            self.Body_lotion.set(0)
            self.Hair_gel.set(0)
            self.Body_spray.set(0)

            #==============Grocery=============
            self.Wheat.set(0)
            self.Food_oil.set(0)
            self.Daal.set(0)
            self.Rice.set(0)
            self.Sugar.set(0)
            self.Tea.set(0)
            self.Detergent.set(0)

            #============Cold Drinks==========
            self.Fruti.set(0)
            self.Sprite.set(0)
            self.Maza.set(0)
            self.Cock.set(0)
            self.Appy.set(0)
            self.Slice.set(0)
            self.Thumbsup.set(0)

        #=========Total Product Price & Tax Variable=======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #=========Customer=========
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
    
        
        
        
         
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()