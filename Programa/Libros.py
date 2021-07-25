import random

class Libro:
    def __init__(self, nombre, autor,leido=False):
        assert type(nombre) == str, 'Error de formato en el nombre (str)'
        assert type(autor) == str, 'Error de formato en el autor(str)'
        assert type(leido)== bool, 'leido debe ser un booleano'
        self.nombre=nombre
        self.autor=autor
        self.leido=leido

    def cambiarLeido(self):
        self.leido = True

    def aString(self,preservaLeido=True, nuevoValor=True):
        '''
        Retorna un string con los datos del libros en el formato de una linea
        del archivo .txt necesario para que funcione la clase Estante.
        '''
        assert type(preservaLeido)== bool
        if preservaLeido:
            if self.leido:
                Leido='t'
            elif not self.leido:
                Leido='f'
            linea = self.nombre+','+self.autor+','+Leido
            return linea
        else:
            if nuevoValor:
                Leido='t'
            elif not nuevoValor:
                Leido='f'
            linea = self.nombre+','+self.autor+','+Leido
            return linea
        
libro = Libro('Bhagavad Gita', 'La vida')



class Estante:
    ''' 
    Hola
    '''
    def __init__(self):
        self.libros=[]
        self.Leidos=[]
        self.noLeidos=[]
        self.archivoEstante='biblioteca.txt'
        
        
    def cargarLibrosALista(self, archivo):
        self.archivoEstante = archivo
        Archivo = open(archivo, "r")
        for linea in Archivo:
            linea = linea.strip()
            lista = linea.split(",") 
            nombre = lista[0]
            autor = lista[1]
            leido = lista[2]
            if leido == 't':
                formatedBook = Libro(nombre, autor, True)
                self.libros.append(formatedBook)
                self.Leidos.append(formatedBook)
                continue
            elif leido == "f":
                formatedBook = Libro(nombre, autor)
                self.libros.append(formatedBook)
                self.noLeidos.append(formatedBook)
                continue
            else:
                continue
        Archivo 
    
    def buscaNombre(self,nombre):    
        libros = self.libros
        count = 0
        for libro in libros:
            count +=1
            if libro.nombre.lower() == nombre.lower():
                return True, count, libro
        return False, 0
    
    def buscaAutor(self, autor, Bool=False):    
        libros = self.libros
        count = 0
        indices = []
        for libro in libros:
            count +=1
            if libro.autor.lower() == autor.lower():
                Bool = True
                indices.append(count)
        return Bool, indices
    
    def agregaLibro(self, nombre, autor, leido=False):
        assert type(nombre) == str, 'Error de formato en el nombre (str)'
        assert type(autor) == str, 'Error de formato en el autor(str)'
        assert type(leido) == bool, 'Leido debe ser un booleano'
        
        if leido:
            Leido='t'
        elif not leido:
            Leido='f'
        linea = [nombre+','+autor+','+Leido+'\n']
        with open(self.archivoEstante, 'a') as f:
                f.writelines('\n'.join(linea))
                print(nombre+' fue agregado exitosamente!')
    
    
    def eliminaLibro(self, nombre):
        busqueda = self.buscaNombre(nombre)
        fueEncontrado = busqueda[0]       
        numeroLinea = busqueda[1]
        libro = busqueda[2]
        if fueEncontrado:
            del_line = numeroLinea    #line to be deleted: no. 3 (first line is no. 1)
            
            with open(self.archivoEstante,"r") as textobj:
                lista = list(textobj)    #puts all lines in a list
            
            del lista[del_line - 1]    #delete regarding element
            
                #rewrite the textfile from list contents/elements:
            with open(self.archivoEstante,"w") as textobj:
                for n in lista:
                    textobj.write(n)
            print(libro.nombre+' fue eliminado exitosamente!')
    
    def cambiaLeido(self, nombre):
        busqueda = self.buscaNombre(nombre)
        fueEncontrado = busqueda[0]       
        numeroLinea = busqueda[1]
        libro = busqueda[2]
        if fueEncontrado:
            with open(self.archivoEstante,'r') as f:
                get_all=f.readlines()
    
            with open(self.archivoEstante,'w') as f:
                for i,line in enumerate(get_all,1):           
                    if i == numeroLinea:
                        f.writelines(libro.aString(False))
                    else:
                        f.writelines(line)
            print(libro.nombre+' ahora figura como leido en el archivo de texto!')
        else:
            print('Este libro No fue encontrado, ningún cambio realizado')
    
    def cambiaNoLeido(self, nombre):
        busqueda = self.buscaNombre(nombre)
        fueEncontrado = busqueda[0]       
        numeroLinea = busqueda[1]
        libro = busqueda[2]
        if fueEncontrado:
            with open(self.archivoEstante,'r') as f:
                get_all=f.readlines()
    
            with open(self.archivoEstante,'w') as f:
                for i,line in enumerate(get_all,1):           
                    if i == numeroLinea:
                        f.writelines(libro.aString(False, False))
                    else:
                        f.writelines(line)
            print(libro.nombre+' ya no figura como leido en el archivo de texto!')
        else:
            print('Este libro No fue encontrado, ningún cambio realizado')
    
    def porcentajeLeidos(self, leidos=0, total=0):
        for libro in self.libros:
            if libro.leido:
                leidos+=1
                total+=1
            else:
                total+=1
        rawPercentage =  (leidos*100)/total
        return round(rawPercentage , 2)
    
    def porcentajeNoLeidos(self, noLeidos=0, total=0):
        for libro in self.libros:
            if not libro.leido:
                noLeidos+=1
                total+=1
            else:
                total+=1
        rawPercentage =  (noLeidos*100)/total
        return round(rawPercentage , 2)
    
    def recomiendaLibro(self):
        largoLista = len(self.libros)
        indiceRandom = random.randrange(0,largoLista)
        titulo = self.libros[indiceRandom].nombre
        autor = self.libros[indiceRandom].autor
        print("Te recomiendo leer " + titulo + " escrito por " + autor + ".")
    
    
    def recomiendaLeido(self):
        largoLista = len(self.Leidos)
        indiceRandom = random.randrange(0,largoLista)
        titulo = self.Leidos[indiceRandom].nombre
        autor = self.Leidos[indiceRandom].autor
        print("Te recomiendo leer " + titulo + " escrito por " + autor + ".")
    
    
    def recomiendaNoLeido(self):
        largoLista = len(self.NoLeidos)
        indiceRandom = random.randrange(0,largoLista)
        titulo = self.NoLeidos[indiceRandom].nombre
        autor = self.NoLeidos[indiceRandom].autor
        print("Te recomiendo leer " + titulo + " escrito por " + autor + ".")
    
    def verLibros(self):
        for libro in self.libros:
            nombre = libro.nombre
            autor = libro.autor
            print(nombre + ' de ' + autor + '.')
    
    def verLeidos(self):
        for libro in self.Leidos:
            nombre = libro.nombre
            autor = libro.autor
            print(nombre + ' de ' + autor + '.')
    
    def verNoLeidos(self):
        for libro in self.noLeidos:
            nombre = libro.nombre
            autor = libro.autor
            print(nombre + ' de ' + autor + '.')        
        
    def verAutores(self):
        autores = []
        for libro in self.libros:
            if libro.autor in autores:
                continue
            else:
                autores.append(libro.autor)
                print(libro.autor)
    
    
    
    
prueba = Estante()
prueba.cargarLibrosALista('biblioteca.txt')
prueba.verLeidos()
print('----------------------------------------------------------------')
prueba.verNoLeidos()

#more_lines = ['Así hablo Zaratustra,F. Nietzsche,f']
#with open('biblioteca.txt', 'a') as f:
#    f.writelines('\n'.join(more_lines))


#with open("biblioteca.txt",'r') as f:
#    get_all=f.readlines()


#with open("biblioteca.txt",'w') as f:
#    for i,line in enumerate(get_all,1):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
#        if i == 112:                              ## OVERWRITES line:112
#            f.writelines("Así hablo Zaratustra,Friedrich Nietzsche,f")
#        else:
#            f.writelines(line)
#La mente nueva del Emperador,Roger Penrose,f







