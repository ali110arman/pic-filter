import sys
import stddraw
import stdio
import random
import math
from color import Color
from picture import Picture
def convert_to_gray(pic):
#in tabe tasavir ra be siah va sefid tabdil mikonad
#ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar haye red green blue har pixel ra daryaft mikonad
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #ba estefade az foormool be siah sefid tabdil mikonim
            y =  int((.299 * red) + (.587 * green) + (0.114 *blue))
            gray = Color(y, y, y)
            #set kardan megdar rang dar pixel
            pic.set(col, row, gray)
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def darken(pic):
#in tabe tasavir ra ba tavagooh be darage tire tar mikonad
    #daryaft megdar tiregy
    # be onvan mesal 10
    percent = int(input("degree:"))/100
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar haye red green blue har pixel ra daryaft mikonad v dar darsad zarb mikonad
            red = pixel.getRed()*percent
            green = pixel.getGreen()*percent
            blue = pixel.getBlue()*percent
            coler = Color(int(red), int(green), int(blue))
            pic.set(col, row, coler)
    #tagir abad boom
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def lighter(pic):
#in tabe tasavir ra ba tavagooh be darage roshan tar mikonad
    #daryaft megdar tiregy
    # be onvan mesal 90
    percent = int(input("degree:"))/100
    percent = 1 + percent
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar haye red green blue har pixel ra daryaft mikonad v dar darsad zarb mikonad
            #agar megdar bish az 255 bood haman 255 ra dar nazar migirad
            red = pixel.getRed()*percent
            if (red > 255):
                red = 255
            green = pixel.getGreen()*percent
            if (green > 255):
                green = 255
            blue = pixel.getBlue()*percent
            if (blue > 255):
                blue = 255
            x =  (red) + (green) + (blue)
            y = int(x)
            gray = Color(int(red), int(green), int(blue))
            pic.set(col, row, gray)
    #tagir abad boom
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()   
def H_miror(pic):
    #in tabe tasvir ra az vast garine mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #magadir ra nesbat be mehvar H garine mikonad
            pic.set(col, pic.height() - row - 1, pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def V_miror(pic):
    #in tabe tasvir ra az vast garine mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #magadir ra nesbat be mehvar v garine mikonad
            pic.set(pic.width() - col - 1,row , pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def hv_miror(pic):
    #in tabe tasvir ra az vast garine mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #magadir ra nesbat be mehvar v va h garine mikonad
            pic.set(col, pic.height() - row - 1, pic.get(col, row))
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pic.set(pic.width() - col - 1,row , pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def flip_horizontal(pic):
    #in tabe tasvir ra nesbat be mehvar H  mitabanad
    #aks jadid baraye zakhire kardan
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #charkhesh dadan ba aks
            target.set(col, pic.height() - row - 1, pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def flip_Vertical(pic):
    #in tabe tasvir ra nesbat be mehvar v  mitabanad
    #aks jadid baraye zakhire kardan
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #charkhesh dadan ba aks
            target.set(pic.width() - col - 1, row, pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show() 
def scale(pic):
    #in tabe tasvir ra nesbat be scale bozog ya koochack mikonad
    #daryaft megdar
    # be onvan mesal 0.5
    scale = float(input("scale:"))
    #abad jadid boom
    wt = int(pic.width()*scale)
    ht = int(pic.height()*scale)
    #dorost kardan boom ba abad jadid
    target = Picture(wt, ht)
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for tcol in range(wt):
        for trow in range(ht):
            scol = tcol * pic.width() // wt
            srow = trow * pic.height() // ht
            #sabt pixel dar makan jadid
            target.set(tcol, trow, pic.get(scol, srow))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()  
def flip_clock90(pic):
    #in tabe tasvir ra 90 darge dar gahat saat mitabanad
    #aks jadid baraye zakhire kardan
    target = Picture(pic.height(), pic.width())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #zakhire pixel dar jaye jadid
            target.set(pic.height() - row - 1, col, pic.get(col, row))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def flip_clockwize90(pic):
    #in tabe tasvir ra 90 darge dar gahat khalaf saat mitabanad
    #aks jadid baraye zakhire kardan
    target = Picture(pic.height(), pic.width())
    #aks jadid baraye zakhire kardan
    target2 = Picture(pic.height(), pic.width())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    #ebteda dar jahat saat mitabanim va sepas garine mikonim
    for col in range(pic.width()):
        for row in range(pic.height()):
            #zakhire pixel dar jaye jadid
            target.set(pic.height() - row - 1, col, pic.get(col, row))
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col2 in range(target.width()):
        for row2 in range(target.height()):
            #zakhire pixel dar jaye jadid
            target2.set(target.width() - col2 - 1, row2, target.get(col2, row2))
    flip_horizontal(target2)
def rotate(pic):
#in tabe tasvir ra ba tavaggoh be megdar degree charkhesh midahad
    #datyaft degree va tabdil be radian
    #be onvan mesal 25
    theta = math.radians(float(input("degree:")))
    #dorost kardan boom jadid
    target = Picture(pic.width(), pic.height())
    #peida kardan mokhtasat markas barabary emal charkhesh
    center_width  = int((pic.width()) / 2)
    center_height = int((pic.height()) / 2)
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for row in range(pic.height()):
        for col in range(pic.width()):
            #mokhtasat noght ba tavaggoh be fasele az markaz
            width_distance = col - center_width
            height_distance = row - center_height
            #mokhtasat jadid noght ba tavaggoh be fasele az markaz
            newcol = int(width_distance * math.cos(theta) - height_distance * math.sin(theta) + center_width)
            newrow = int(width_distance * math.sin(theta) + height_distance * math.cos(theta) + center_height)
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft rang har pixel
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue() 
            #agar pixel jadid dakhel boom bood sabt mishavad
            if (newcol >= 0) and (newcol < pic.width()) and  (newrow >= 0) and (newrow < pic.height()):
                target.set(col, row, Color(red, green, blue))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def red_filter(pic):
# in tabe filter germez ra ba roye aks emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar red har pixel ra daryaft mikonad
            red = pixel.getRed()
            pic.set(col, row, Color(red, 0, 0))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def green_filter(pic):
# in tabe filter sabz ra ba roye aks emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar green har pixel ra daryaft mikonad
            green = pixel.getGreen()
            pic.set(col, row, Color(0, green, 0))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def blue_filter(pic):
# in tabe filter aby ra ba roye aks emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar blue har pixel ra daryaft mikonad
            blue = pixel.getBlue()
            pic.set(col, row, Color(0, 0, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def negative(pic):
# in tabe filter negative ra ba roye aks emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #megdar red green blue har pixel ra daryaft mikonad
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #ekhtelaf har rang ba 255 ra dar boom set mitabanad
            pic.set(col, row, Color(255-red, 255-green, 255-blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def swirl(pic):
#in tabe bar roye aks yek pichesh amal mikonad
    #daryaft megdar pichesh
    alpha = float(input("degree:"))*100
    #dorost karadan boom jadid
    target = Picture(pic.width(), pic.height())
    #peida kardan mokhtasat markas barabary emal charkhesh
    widthCenter  = int((pic.width()) / 2)
    heightCenter = int((pic.height()) / 2)
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for row in range(pic.height()):
        for col in range(pic.width()):
            #mokhtasat noght ba tavaggoh be fasele az markaz
            column_distance = col - widthCenter
            row_distance = row - heightCenter
            #peida kardan zavie ba tavaggoh be foormool ketab
            theta = math.pi / alpha * (math.sqrt(column_distance*column_distance + row_distance*row_distance))
            #peida kardan mokhtasat jadid ba tavaggoh be foormool ketab
            newcol = int(column_distance * math.cos(theta) - row_distance * math.sin(theta) + widthCenter)
            newrow = int(column_distance * math.sin(theta) + row_distance * math.cos(theta) + heightCenter)
            #agar pixel jadid dakhel boom bood sabt mishavad
            if (newcol >= 0) and (newcol < pic.width()) and (newrow >= 0) and (newrow < pic.height()):
                target.set(col, row, pic.get(newcol, newrow))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def zoom(pic):
    #in tabe tasvir ra nesbat be scale bozog ya koochack mikonad
    #daryaft megdar
    # be onvan mesal 2
    scale = float(input("scale:"))
    #abad jadid boom
    wt = int(pic.width()*scale)
    ht = int(pic.height()*scale)
    #dorost kardan boom ba abad jadid
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for tcol in range(wt):
        for trow in range(ht):
            scol = tcol * pic.width() // wt
            srow = trow * pic.height() // ht
            #sabt pixel dar makan jadid
            target.set(tcol, trow, pic.get(scol, srow))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show() 
def opacity(pic):
    #in tabe tasvir ra nesbat be scale opacity namyesh mdidahad
    #daryaft megdar
    # be onvan mesal 50
    alpha = 1.0-float(input("degree:"))/100
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #daryaft va taghir shedat har rang har pixel
            red = int((1-alpha)*pixel.getRed()+ alpha *255)
            green = int((1-alpha)*pixel.getGreen()+ alpha *255)
            blue = int((1-alpha)*pixel.getBlue()+ alpha *255)
            #set kardan magadir jadid
            pic.set(col, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def left_gradiant(pic):
    #in tabe yek gradiant sefid ba roye aks az samt chap emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #taen hodood gradiant
            alpha = col / (pic.width())
            if(alpha <= 1):
                alpha = 1 - alpha
                #tagir megar har rang ba tavaggoh be alpha
                red = int((1-alpha)*pixel.getRed()+ alpha *255)
                green = int((1-alpha)*pixel.getGreen()+ alpha *255)
                blue = int((1-alpha)*pixel.getBlue()+ alpha *255)
            pic.set(col, row, Color(red, green, blue))            
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()   
def right_gradiant(pic):
    #in tabe yek gradiant sefid ba roye aks az samt rast emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            alpha = col / (pic.width())
            if(alpha <= 1):
                red = int((1-alpha)*pixel.getRed()+ alpha *255)
                green = int((1-alpha)*pixel.getGreen()+ alpha *255)
                blue = int((1-alpha)*pixel.getBlue()+ alpha *255)
            pic.set(col, row, Color(red, green, blue))            
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()   
def top_gradiant(pic):
    #in tabe yek gradiant sefid ba roye aks az samt bala emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #daryaft pixel
            alpha = row / (pic.height())
            if(alpha <= 1):
                alpha = 1 - alpha            
                red = int((1-alpha)*pixel.getRed()+ alpha *255)
                green = int((1-alpha)*pixel.getGreen()+ alpha *255)
                blue = int((1-alpha)*pixel.getBlue()+ alpha *255)
            pic.set(col, row, Color(red, green, blue))            
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()  
def down_gradiant(pic):
    #in tabe yek gradiant sefid ba roye aks az samt paen emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            #daryaft pixel
            alpha = row / (pic.height())
            if(alpha <= 1):
                red = int((1-alpha)*pixel.getRed()+ alpha *255)
                green = int((1-alpha)*pixel.getGreen()+ alpha *255)
                blue = int((1-alpha)*pixel.getBlue()+ alpha *255)
            pic.set(col, row, Color(red, green, blue))            
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def wave(pic):
# in tabe bar roye tasvir yek halat moj ghone ejad mikonad
    #sheddat moh ja daryaft mishavad
    #be onvan mesal 5
    degree = float(input("degree:"))
    #dorost kardan boom jadid
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for row in range(pic.height()):
        for col in range(pic.width()):
            #ba estefade az formol ketab makan jadid pixel taein mishavad
            Pixelrow = int(row + degree * math.sin(col * 2.0 * math.pi / 100))
            #agar dakhel boom jadid bod pixel sabt mishavad
            if (Pixelrow >= 0) and (Pixelrow < pic.height()):
                target.set(col, row, pic.get(col, Pixelrow))
    #tagir abad boom  
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def magic_color(pic):
    #in tabe yek filter rangi makoos emal mikonad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            pic.set(col, row, Color(blue, green, red ))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def burn(pic):
    #in tabe tasvir ra nesbat be scale burn tire tar mikonad
    #daryaft megdar
    # be onvan mesal 50
    alpha = 1.0-float(input("degree:"))/100
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang v emal megadir jadid ba tavaggoh be darsad burn
            red = int((1-alpha)*pixel.getRed()+ alpha *100)
            green = int((1-alpha)*pixel.getGreen()+ alpha *100)
            blue = int((1-alpha)*pixel.getBlue()+ alpha *100)
            pic.set(col, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def saturation(pic):
    #in tabe tasvir ra nesbat be alpha az teif rangi kamel ta siah sefid namesh midihad
    #daryaft megdar
    # be onvan mesal 50
    alpha = 1.0-float(input("degree:"))/100
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang v emal megadir jadid ba tavaggoh be darsad burn
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #emal filter khakestary
            x =  (.299 * red) + (.587 * green) + (0.114 *blue)
            y = int(x)
            #email rang jadid ba tavajoh be darsad rang khakestary
            red = int((1-alpha)*pixel.getRed()+ alpha *y)
            green = int((1-alpha)*pixel.getGreen()+ alpha *y)
            blue = int((1-alpha)*pixel.getBlue()+ alpha *y)
            pic.set(col, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def add_noise(pic):
#in tabe bar roye tasvir yek halat shatrangi be onvan noise ezafe mikonad
#ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang v emal megadir jadid ba tavaggoh be darsad burn
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #emal pixel haye siah ba estefade az shart
            if ((col * row)% 2 == 1):
                pic.set(col, row, Color(red, green, blue))
            else:
                pic.set(col, row, Color(0, 0, 0)) 
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def grid(pic):
    #in tabe bar roye tasvir yek grid emal mikonad
    #be tori ke mehvar x ra be tedad darage tagsim mikonad
    #daryaft megdar
    # be onvan mesal 5
    degree = int(pic.width()/int(input("degree:")))
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #emal pixel siah dar soorat barabary shart dar row
            if ((row)% degree == 1):
                pic.set(col, row, Color(0, 0, 0))
            else:
                pic.set(col, row, Color(red, green, blue)) 
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #emal pixel siah dar soorat barabary shart dar col
            if ((col)% degree == 1):
                pic.set(col, row, Color(0, 0, 0))
            else:
                pic.set(col, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def thrush(pic):
#in tabe bar roye aks noise televison ra emal mikonad
    #in tedad tekrar in halge ba hads v azmayesh be dast amade
    for i in range(int(pic.width() * pic.height()/5)):
        #peida karan col random
        col = random.randint(0, pic.width())
        #peida karan row random
        row = random.randint(0, pic.height())
        #peida kardan adad random barabary red
        red = random.randint(0, 255)
        #peida kardan adad random barabary green
        green = random.randint(0, 255)
        #peida kardan adad random barabary blue
        blue = random.randint(0, 255)
        pic.set(col, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def brush_paint(pic):
#in tabe bar roye aks nogte haye khali brush ro mekeshad
    #in tedad tekrar in halge ba hads v azmayesh be dast amade
    for i in range(int(pic.width() * pic.height()/5)):
        #peida karan col random
        col = random.randint(0, pic.width())
        #peida karan row random
        row = random.randint(0, pic.height())
        pic.set(col, row, Color(202, 224, 245))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def old_pic(pic):
#in tabe aks ra be tasvir gadimi tabdil mikonad
    alpha = .7
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #emal filter khakestary
            x = (.299 * red) + (.587 * green) + (0.114 *blue)
            #emal shedat rang ha ba tavaggoh be alpha
            red = int((1-alpha)* x + alpha *95)
            green = int((1-alpha)* x + alpha *64)
            blue = int((1-alpha)* x + alpha *17)
            pic.set(col, row, Color(red, green, blue))
    #in halge baraye ezafe karadan nogte haye sefid va siah estefade mishavad
    for i in range(int(pic.width() * pic.height()/5000)):
        #peida karan col random
        col = random.randint(0, pic.width())
        #peida karan row random
        row = random.randint(0, pic.height())
        #in do shart baraye teshkhis sefid va ya siah estefade mishavad
        if (i%2==0):
            pic.set(col, row, Color(0, 0, 0))
        if (i%2==1):
            pic.set(col, row, Color(255, 255, 255))    
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show()
def damage_monitor(pic):
#in tabe ba taghir makan pixel ha baas taghir tasvir va namanyesh manand manitor kharab amal midahad
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #set kardan rang dar makan jadid
            pic.set(col*2, row, Color(red, green, blue))
    #tagir abad boom        
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(pic)
    stddraw.show() 
def camrea_shake(pic):
# in tabe tasvir ra be nahvy taghir midahad ke ghaya hengam akasy dast harekat karde
    i = int(0)
    #dorost kardan boom jadid
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #tagir makan pixel baraye emal harket
            if(i%2==0):
                target.set(col -2 , row +2 , Color(red, green, blue))
            else:
                target.set(col +2, row -2 , Color(red, green, blue))
            i += 1
    #tagir abad boom  
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()   
def blur(pic):
# in tabe tasvir ra mat tar mikonad
    i = int(0)
    #dorost kardan boom jadid
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #tagir makan pixel baraye emal harket
            if(i%2==0):
                target.set(col +2, row , Color(red, green, blue))
            else:
                target.set(col , row -2, Color(red, green, blue))
            i += 1
    #tagir abad boom  
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show() 
def find_edge(pic):
#in tabe khat haye aks ya be estelah edge ha ra shenasaye mikonad
#dorost kardan boom jadid
    target = Picture(pic.width(), pic.height())
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for col in range(pic.width()):
        for row in range(pic.height()):
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #in adad ba azmayesh va tekrar be dast amade ast
            if ((red + green + blue)/3 > 40):
                #set karadan rang siah
                target.set(col, row, Color(255, 255, 255))
            elif ((red + green + blue)/3 < 40):
                #set karadan rang sefid
                target.set(col, row, Color(0, 0, 0))
    #tagir abad boom  
    stddraw.setCanvasSize(pic.width(), pic.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show() 
def glass(pic):
#in tabe tasvir ri be nahvy taghir midahad ke goha yek shishe bar roye aks gharar darad
    #copy kardan aks dar target
    target = pic
    #ba estefade az do halge for dar tak tak pixel ha peimayesh anjam midahad
    for row in range(pic.height()):
        for col in range(pic.width()):
            #yek pixel be tor random dar fasele -10 ta 10 dar col entekhab mishavad
            calrand = random.randint(col - 10, col + 10)
            #yek pixel be tor random dar fasele -10 ta 10 dar row entekhab mishavad
            rowrand = random.randint(row - 10, row + 10)
            #daryaft pixel
            pixel = pic.get(col, row)
            #daryaft har rang
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            #sabt tar target
            target.set(col, row, Color(red, green, blue))
            #agar pixel jadid dakhel boom bood sabt mishavad
            if (calrand >= 0 and calrand < pic.width()) and (rowrand >= 0 and rowrand < pic.height()):
                target.set(calrand, rowrand, Color(red, green, blue))
            else:
                target.set(col, row, Color(red, green, blue))
    #tagir abad boom
    stddraw.setCanvasSize(target.width(), target.height())
    #namayesh aks
    stddraw.picture(target)
    stddraw.show()
def main():
    pic = Picture("test.jpg")
    #convert_to_gray(pic)
    #darken(pic)
    #lighter(pic)
    #H_miror(pic)
    #V_miror(pic)
    #hv_miror(pic)
    #flip_horizontal(pic)
    #flip_Vertical(pic)
    #rotate(pic)
    #scale(pic)
    #flip_clock90(pic)
    #flip_clockwize90(pic)
    #red_filter(pic)
    #green_filter(pic)
    #blue_filter(pic)
    #negative(pic)
    #swirl(pic)
    #zoom(pic)
    #opacity(pic)
    #left_gradiant(pic)
    #right_gradiant(pic)
    #down_gradiant(pic)
    #top_gradiant(pic)
    #wave(pic)
    #magic_color(pic)
    #burn(pic)
    #saturation(pic)
    #add_noise(pic)
    #grid(pic)
    #thrush(pic)
    #brush_paint(pic)
    #old_pic(pic)
    #damage_monitor(pic)
    #camrea_shake(pic)
    #blur(pic)
    #find_edge(pic)
    glass(pic)    
if __name__ == '__main__':
    main()

