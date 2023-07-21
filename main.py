 

from flask import Flask, render_template 

 
 

app = Flask(__name__) 

 
 

@app.route ('/hola') 

 
 

def hola(): 

    return 'Hola' 

@app.route('/paises') 

def paises(): 

     

    paises=[ 

                [ 

                    { 

                        "nombre":"America", 

                        'paises':[ 

                                    "Colombia", 

                                    "Peru" 

                                ] 

                    } 

                ], 

                [ 

                    { 

                        "nombre":"Asia", 

                        'paises':[ 

                                    "Japon", 

                                    "Irlanda", 

                                    "Corea" 

                                ] 

                    } 

                ]  

            ] 

    ''''variables de conteo para cada continente''' 

     

    contador_paises_america =0 

    for pais in paises[0][0]['paises']: 

        contador_paises_america= contador_paises_america+1 

        print(contador_paises_america) 

         

 
 

    contador_paises_asia =0 

    for pais in paises[1][0]['paises']: 

        contador_paises_asia= contador_paises_asia+1 

        print(contador_paises_asia) 

     

         

    user ='Valentina Guzman' 

    return render_template('paises_listas.html', 

                           user= user, 

                           continentes= paises, 

                           Asia=contador_paises_asia, 

                            America=contador_paises_america )