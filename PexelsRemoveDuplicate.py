import os
from os import walk
import sys

ParentFolder = r'\\syn07.iil.intel.com\bgs\detection_office\pexels'
LocalFolder = r'\\syn07.iil.intel.com\bgs\detection_office\pexels\15_03_2022'
ImageFormat = ['jpeg', 'png']


def SearchForDuplicates():
    LocalFiles = next(walk(LocalFolder), (None, None, []))[2]
    LocalDictionary = {}
    print(f'Loading all images from "{os.path.basename(LocalFolder)}" ...')
    for x in LocalFiles:
        if x.split(".")[1] in ImageFormat:
            if "_" in x:
                LocalDictionary[x.split("_")[0]] = os.path.join(LocalFolder, x)
            else:
                LocalDictionary[x.split(".")[0]] = os.path.join(LocalFolder, x)

    ChildDictionary = {}
    Duplicates = {}
    for Child in os.listdir(ParentFolder):
        if Child != os.path.basename(LocalFolder):
            ChildFolder = os.path.join(ParentFolder, Child)
            ChildFiles = next(walk(ChildFolder), (None, None, []))[2]
            for x in ChildFiles:
                if x.split(".")[1] in ImageFormat:
                    if "_" in x:
                        ChildDictionary[x.split("_")[0]] = os.path.join(ChildFolder, x)
                    else:
                        ChildDictionary[x.split(".")[0]] = os.path.join(ChildFolder, x)
            print(f'Searching for duplicates in {os.path.basename(ChildFolder)} ...')
            for key in LocalDictionary:
                if key in ChildDictionary:
                    Duplicates[LocalDictionary[key]] = ChildDictionary[key]

    RemoveDuplicates(Duplicates)


def RemoveDuplicates(Duplicates):
    if len(Duplicates) < 1:
        print('--------------- No duplicates found --------------')
        return
    print(f'\n\n********** Found {len(Duplicates)} duplicates **************')
    for duplicate in Duplicates:
        print('\tFound duplicates: ' + duplicate + ' => ' + Duplicates[duplicate])
    Result = input("Delete all duplicates? [y/n] ")
    if Result.lower() == 'y':
        for File2Remove in Duplicates:
            os.remove(File2Remove)
            print(f'\n\t\t Removed -> {File2Remove}\n')
        print('################ COMPLETED ################')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        ParentFolder = sys.argv[1]
        LocalFolder = sys.argv[2]
        SearchForDuplicates()
    else:
        print('Parameters: <ParentFolder> <LocalFolder>')
