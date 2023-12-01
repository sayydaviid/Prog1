
from flet import *
import flet as ft

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    Green = '#24a424'
    teste = ft.Image(src=f"https://picsum.photos/200/200")

    tasks = Column()
    categories_card = Row(
        scroll= 'auto'
    )
    
    categories = ['SSD NVME 2.0', '2X8 DDR4 3200', 'Ryzen 7 7700x', 'RTX 3090']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor = BG,
                height=110,
                width=170,
                padding=15,
                content= Column(
                    controls=[
                        Text('40 Unidades'),
                        Text(category),
                        Container(
                            width= 160,
                            height= 5,
                            bgcolor = 'white12',
                            border_radius= 20,
                            padding= padding.only(right= i*30),
                            content= Container(
                                bgcolor= Green,
                            )
                        )
                    ]
                    
                )
            )
        )
    conteudo_primeira_pagina = Container(
        content= Column(
            controls=[
                Row(alignment = 'spaceBetween',
                    controls=[
                        Container(
                            content= Icon(icons.MENU)),
                    Row(
                        controls=[
                            Container(
                                content= Icon(icons.SEARCH)),
                            Container(
                                content= Icon(icons.SHOPPING_CART))
                            ],
                            
                        ),
                        
                    ],
                ),
                Container(height= 20),
                Text(
                    value= 'Olá Professor, o que vai ser hoje?'
                ),
                Text(
                    value= 'OFERTA RELÂMPAGO'
                ),
                Container(
                    padding=padding.only(top= 10, bottom=20),
                    content=categories_card
                ),
                Container(height= 20),
                Text('PRODUTOS MAIS VENDIDOS'),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon=icons.ADD, on_click=lambda _: page.go('/create_tasks')
                        )
                        
                    ]
                )
            ]
        )
        
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor= FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20, 
                    right=20, bottom=5
                    ),
                    content= Column(
                        controls=[
                            conteudo_primeira_pagina
                        ]
                    )
            )
        ]
    )
    
    container = Container( 
        width=400,
        height=850,
        bgcolor= BG,
        border_radius=35,
        content= Stack(
        controls=[
        page_1, 
        page_2,
        
        
        ]
        
        )
    )
    page.add(container)
    

app(target=main)
