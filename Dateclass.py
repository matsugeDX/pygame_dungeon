class Date():

    def __init__(self):
        
        file = open("save.txt","r")
        rl = file.readlines()
        file.close()
        
        self.get_exp = int(rl[0].strip("\n")) #取得経験値
        self.lv_up = int(rl[1].strip("\n")) #必要経験値
        self.lv = int(rl[2].strip("\n")) #現在レベル
        self.pl_x = int(rl[3].strip("\n")) #現在x座標
        self.pl_y = int(rl[4].strip("\n")) #現在y座標
        self.room = eval(rl[5].strip("\n")) #map情報
        self.stair = (rl[6].strip("\n")) #データリセットした場合のフラグ
        self.stair_x = int(rl[7].strip("\n")) #現在フロアの階段x座標
        self.stair_y = int(rl[8].strip("\n")) #現在フロアの階段y座標
        self.stair_now = int(rl[9].strip("\n")) #現在フロア
    
    def savefile(self):
        file = open("save.txt","w")
        file.write(str(self.get_exp)+"\n")
        file.write(str(self.lv_up)+"\n")
        file.write(str(self.lv)+"\n")
        file.write(str(self.pl_x)+"\n")
        file.write(str(self.pl_y)+"\n")
        file.write(str(self.room)+"\n")
        file.write(str(self.stair)+"\n")
        file.write(str(self.stair_x)+"\n")
        file.write(str(self.stair_y)+"\n")
        file.write(str(self.stair_now)+"\n")
        file.close()

para = Date()