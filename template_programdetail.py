from jinja2 import  Template
import re
import datetime

date_format = "%d %b %Y"
time_format = "%H:%M"

def sigthseeing_program_message(program, idvez, program_details):

    Event_short_name = program['Program']
    Date = program['Program Date'].strftime(date_format)
    event_Start_time = program['Program Start Time'].strftime(time_format)
    event_Finish_time = program['Program Finish Time'].strftime(time_format)
    Meeting_point = program_details['Start location']
    Pax = str(int(program['Pax']))
    No_of_tour_leader = str(int(program['No. of tour leader']))
    Idvez = program['IdVez']
    Idvez_phone = idvez['Phone number']

    varosnezes = Template("{{Event_short_name}}: {{Date}}, {{event_Start_time}}-{{event_Finish_time}}\n"
                     "Meeting point: {{Meeting_point}}\n"
                     "Start: {{event_Start_time}} CET\n"
                     "Finish point: TBD\n"
                     "Pax: {{Pax}} + {{No_of_tour_leader}}\n"
                     "Tour Guide Info:\n"
                     "Name: {{Idvez}}\n"
                     "Phone No.: {{Idvez_phone}}")
    print(varosnezes.render(Event_short_name= Event_short_name, Date=Date,event_Start_time=event_Start_time,event_Finish_time=event_Finish_time,
                            Meeting_point=Meeting_point, Pax=Pax, No_of_tour_leader=No_of_tour_leader, Idvez=Idvez, Idvez_phone=Idvez_phone))


def eating_program_message(program, restaurant):
    print(program)
    print(restaurant)

    Program = program['Program']
    Date = program['Program Date'].strftime(date_format)
    event_Start_time = program['Program Start Time'].strftime(time_format)
    event_Finish_time = program['Program Finish Time'].strftime(time_format)
    Address = restaurant['Address']
    Web = restaurant['Web']
    Tel = restaurant['Phone number']
    Pax = str(int(program['Pax']) + int(program['No. of tour leader']))
    menu_pax = re.findall('\d+', program['Menu'])
    No_of_menu1 = menu_pax[0]
    No_of_menu2 = menu_pax[1]
    Menu1 = str(restaurant['Menu1 1st course'] + ', ' + restaurant['Menu1 main course'])
    Menu2 = str(restaurant['Menu2 1st course'] + ', ' + restaurant['Menu2 main course'])

    eating = Template("{{Program}}: {{Date}}, {{event_Start_time}}-{{event_Finish_time}}\n"
                          "ADD: {{Address}}\n"
                          "www: {{Web}}\n"
                          "Start: {{event_Start_time}} CET\n"
                          "Tel: {{Tel}}\n"
                          "Pax: {{Pax}}\n"
                          "Menu:\n"
                          "{{No_of_menu1}} pax: {{Menu1}}\n"
                          "{{No_of_menu2}} pax: {{Menu1}}\n")
    print(eating.render(Program=Program, Date=Date, event_Start_time=event_Start_time, event_Finish_time=event_Finish_time,
                        Address=Address, Web=Web, Tel=Tel, Pax=Pax,
                        No_of_menu1=No_of_menu1, Menu1=Menu1,
                        No_of_menu2=No_of_menu2, Menu2=Menu2))
