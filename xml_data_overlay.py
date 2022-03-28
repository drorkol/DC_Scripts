import xml.etree.ElementTree as ET
import sys
import os
import cv2

ids = {'person':(255,255,0),
        'chair':(0,204,102),
        'couch':(204,0,102),
        'potted_plant': (0,51,102),
        'dinning_table': (51,255,255),
        'door': (76,153,0),
        'window': (0,128,255),
        'closet': (255,153,204),
        'refrigerator': (0,0,255)}





font = cv2.FONT_HERSHEY_SIMPLEX

def parse_single_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    color_image = cv2.imread(xml_path.replace('_ann.xml','_color.png'))
    for object_ in root.findall('object'):
        bndbox = object_.find('bndbox')
        name = object_.find('name').text
        x1 = int(bndbox.find('xmin').text)
        x2 = int(bndbox.find('xmax').text)
        y1 = int(bndbox.find('ymin').text)
        y2 = int(bndbox.find('ymax').text)
        cv2.rectangle(color_image,(x1,y1),(x2,y2),ids[name],2)
        cv2.putText(color_image,name,(x1,y1-10),font,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.imshow('image with anno',color_image)
    cv2.waitKey(0)




if __name__ == '__main__':
    for root,subdirs,files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith('_ann.xml'):
                parse_single_xml(os.path.join(root,file))


