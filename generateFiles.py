
def createFileFuction():
    
    #the quantity of files you want to create
    qtyOfFiles = 2
    #Filename extension
    filenameExtension = '.py'

    for x in range(qtyOfFiles):
        fileName = f'e{x}{filenameExtension}'
        file_builder = open(fileName, "w+")
        print(fileName)

    file_builder.close()

createFileFuction() 

