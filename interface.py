#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast
import iptc

srIP = ''
desIP = ''
regText = ''
protText = ''
port_inText = ''
port_outText = ''
int_inText = ''
int_outText = ''
selection = 0
mt = 1  #pour tester les match
rule = iptc.Rule()
r = 2
match = iptc.Match(rule, "tcp")
target = iptc.Target(rule, "ACCEPT")

##>>configuration general de depart<<##
window = tk.Tk()
window.title("configuration du parfeu")
window.geometry("700x550")
window.resizable(width=False, height=False)
#############

##>>>pour le style###
style = ttk.Style()
style.theme_use('clam')
#############

###>>>action et les commandes
def add_btn():
    global rule, r, selection, srIP, desIP, protText, port_inText,port_outText, int_inText, int_outText, regText, match, target, mt
    srIP = srEntry.get()
    desIP = destEntry.get()
    protText = protEntry.get()
    port_inText = port_inEntry.get()
    port_outText = port_outEntry.get()
    int_inText = int_inEntry.get()
    int_outText = int_outEntry.get()
    regText = regEntry.get().upper()
    if protText != '':
        rule.protocol = protText
    if srIP != '':
        rule.src = srIP
    if desIP != '':
        rule.dst = desIP
    if int_inText != '':
        rule.in_interface = int_inText
    if int_outText != '':
        rule.out_interface = int_outText
    if port_inText != '':
        mt = 0
        if protText != '':
            match = rule.add_match(protText)
            match.dport = port_inText
            mt = 1
        else:
            messagebox.showerror(title="ajout", message="veuillez choisir un protocole")
    if port_outText != '':
        mt = 0
        if protText != '':
            match = rule.add_match(protText)
            match.sport = port_outText
            mt = 1
        else:
            messagebox.showerror(title="ajour", message="veuillez choisir un protocole")
    target = rule.create_target(regText)

    if selection == 1 and mt == 1:
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        try:
            chain.insert_rule(rule)
            r = 1
        except:
            r = 0
    elif selection == 2 and mt == 1:
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "FORWARD")
        try:
            chain.insert_rule(rule)
            r = 1
        except:
            r = 0
    elif selection == 3 and mt == 1:
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
        try:
            chain.insert_rule(rule)
            r = 1
        except:
            r = 0
    if r == 1:
        messagebox.showinfo(title='resultat', message="ajout reussi")
    elif r == 0:
        messagebox.showerror(title='resultat', message="verifiez vos informations")
def dump_btn():
    global selection
    if selection == 1:
        res = iptc.easy.dump_chain('filter','INPUT',ipv6=False)
        i = 1
        list.delete(0, tk.END)
        for val in res:
            list.insert(i, val)
            i += 1

    elif selection == 2:
        res = iptc.easy.dump_chain('filter', 'FORWARD', ipv6=False)
        i = 1
        list.delete(0, tk.END)
        for val in res:
            list.insert(i, val)
            i += 1
    elif selection == 3:
        res = iptc.easy.dump_chain('filter', 'OUTPUT', ipv6=False)
        i = 1
        list.delete(0, tk.END)
        for val in res:
            list.insert(i, val)
            i += 1
    else:
        messagebox.showerror(title="listage", message="veuillez choisir une Chain")

def select_chain():
    global selection
    selection = radio.get()

def del_btn():
    global rule
    global selection
    if list.selection_get() == '':
        messagebox.showinfo(message="cliquez sur une regle")
    else:
        if selection == 1:
            rule_d = ast.literal_eval(list.selection_get())
            iptc.easy.delete_rule("filter", "INPUT", rule_d, ipv6=False)
            dump_btn()
        elif selection == 2:
            rule_d = ast.literal_eval(list.selection_get())
            iptc.easy.delete_rule("filter", "FORWARD", rule_d, ipv6=False)
            dump_btn()
        elif selection == 3:
            rule_d = ast.literal_eval(list.selection_get())
            iptc.easy.delete_rule("filter", "OUTPUT", rule_d, ipv6=False)
            dump_btn()


def in_check():
    if intin_var.get() == 1:
        int_inEntry.configure(state="normal")
    else:
        int_inEntry.configure(state="disabled")
def out_check():
    if intout_var.get() == 1:
        int_outEntry.configure(state="normal")
    else:
        int_outEntry.configure(state="disabled")

def pint_check():
    if portin_var.get() == 1:
        port_inEntry.configure(state="normal")
    else:
        port_inEntry.configure(state="disabled")
def pout_check():
    if portout_var.get() == 1:
        port_outEntry.configure(state="normal")
    else:
        port_outEntry.configure(state="disabled")
########################

##>>les menus
menubar = tk.Menu(window)
menubar.add_command(label="ajouter", command=add_btn)
menubar.add_command(label="lister", command=dump_btn)
menubar.add_command(label="supprimer", command=del_btn, background="red")
window.config(menu=menubar)
#################

##>>label des input<<##
tk.Label(window, text="Adresse ip source:").place(x=30, y=50)
tk.Label(window, text="Adresse ip destination:").place(x=30, y=80)
tk.Label(window, text="protocole cible:").place(x=30, y=110)
tk.Label(window, text="Règle:").place(x=30, y=140)
tk.Label(window, text="choisir la Chain:").place(x=450 ,y= 50)
tk.Label(window, text="specifier des ports----").place(x=30, y=180)
tk.Label(window, text="specifier des interfaces----").place(x=350, y=180)
####################

##>>les input<<##
srEntry = tk.Entry()
srEntry.place(x=200, y=50)
destEntry = tk.Entry()
destEntry.place(x=200, y=80)
protEntry = ttk.Combobox(state="readonly", values=["tcp","udp"])
protEntry.place(x=200, y=110)
port_inEntry = tk.Entry(width=10, state="disabled")
port_inEntry.place(x=40, y=230)
port_outEntry = tk.Entry(width=10, state="disabled")
port_outEntry.place(x=160, y=230)

int_inEntry = tk.Entry(width=10, state="disabled")
int_inEntry.place(x=330, y=230)
int_outEntry = tk.Entry(width=10, state="disabled")
int_outEntry.place(x=480, y=230,)
regEntry = ttk.Combobox(state="readonly", values=["DROP", "ACCEPT", "REJECT", "RETURN"])
regEntry.set("ACCEPT")
regEntry.place(x=200, y=140)
###################

##>>les radio<<##
radio = tk.IntVar()
inpRad = tk.Radiobutton(window, text="INPUT", variable=radio, value=1, command=select_chain)
fordRad = tk.Radiobutton(window, text="FORWARD", variable=radio, value=2, command=select_chain)
outRad = tk.Radiobutton(window, text="OUTPUT", variable=radio, value=3, command=select_chain)
inpRad.place(x=550, y=50)
fordRad.place(x=550, y=70)
outRad.place(x=550, y=90)
############

##>>les checkbox<<##
portin_var = tk.IntVar()
portout_var = tk.IntVar()
intin_var = tk.IntVar()
intout_var = tk.IntVar()
tk.Checkbutton(window, text="entrée", variable=portin_var, onvalue=1, offvalue=0, command=pint_check).place(x=30, y=200)
tk.Checkbutton(window, text="sortie", variable=portout_var, onvalue=1, offvalue=0, command=pout_check).place(x=150, y=200)
tk.Checkbutton(window, text="entrée", variable=intin_var, onvalue=1, offvalue=0, command=in_check).place(x=320, y=200)
tk.Checkbutton(window, text="sortie", variable=intout_var, onvalue=1, offvalue=0, command=out_check).place(x=470, y=200)

##>>pour l'affichage de la table
list = tk.Listbox(window, selectmode=tk.SINGLE)

list.pack(side=tk.BOTTOM, fill=tk.X)
window.mainloop()
