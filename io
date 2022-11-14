MDBottomNavigation:
        text_color_active: "black"

#Primera pantalla
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Tasca'
            icon: 'checkbox-marked-circle-plus-outline'

            MDLabel:
                text: 'Llistat Tasques'
                halign: 'center'

#Segona pantalla
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Kanban'
            icon: 'clipboard-check-multiple'
            Image:
                source: 'files/KivyMD/ImgProva/Kanban.png'

            MDLabel:
#                text: 'Kanban'
                halign: 'center'

#Tercera pantalla
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Gantt'
            icon: 'calendar-multiple'
            Image:
                source: 'files/KivyMD/ImgProva/Gantt.png'

            MDLabel:
#                text: 'Gantt'
                halign: 'center'



MDScreen:
                    name: "screen2"                 
                    MDIcon:
                        icon: "gmail"
                        pos_hint: {"center_x": .5, "center_y": .5}


on_release: 
                root.nav_drawer.set_state("close")
                root.manager.current="screen1"


                
#Falta fer les screens per a cada "menu"
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Inicio'
                            on_release: 
                                root.nav_drawer.set_state("close")
                                root.manager.current="Inicio"
                        OneLineListItem:
                            text: 'Questionarios'
                            on_release: 
                                root.nav_drawer.set_state("close")
                                root.manager.current="Questionarios"
                        OneLineListItem:
                            text: 'Informes'
                        OneLineListItem:
                            text: 'Formacion'
                        OneLineListItem:
                            text: 'Contacto'
            
