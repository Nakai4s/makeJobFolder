import os

ROOT_NAME = "sample"
FOLDER_LIST = 
["外部設計","詳細設計","単体設計","検収設計","製造","単体テスト","結合テスト","総合テスト"]

def main():
    mkdir(ROOT_NAME)
    os.chdir(ROOT_NAME)

    for i in FOLDER_LIST:
        phase = str(FOLDER_LIST.index(i + 1)) + "_" + i
        mkdir(phase)
        os.chdir(phase)

        for j in range(1,5):
            review = "Rv" + str(j)
            mkdir(review)
            
        os.chdir("../")
        

def mkdir(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)

if __name__ == "__main__":
    main()