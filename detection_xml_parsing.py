import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys
import os
import shutil
import tqdm

tree = ET.parse(sys.argv[1])
root = tree.getroot()
ids = {'person':1,
        'chair':62,
        'couch':63,
        'potted_plant': 64,
        'dinning_table': 67,
        'door': 90,
        'window': 120,
        'closet': 150,
        'refrigerator': 82}



for image in tqdm.tqdm(root.findall('image')):
    dst_root = ET.Element("annotations")

    src_image_path = image.get('name')
    for box in image.findall('box'):

        label = box.get('label')
        x1 = int(float(box.get('xtl')))
        x2 = int(float(box.get('xbr')))
        y1 = int(float(box.get('ytl')))
        y2 = int(float(box.get('ybr')))

        object_ = ET.SubElement(dst_root, 'object')
        ET.SubElement(object_, 'id').text = str(ids[label])
        ET.SubElement(object_, 'name').text = label
        dst_box = ET.SubElement(object_, 'bndbox')
        ET.SubElement(dst_box, 'xmin').text = str(x1)
        ET.SubElement(dst_box, 'ymin').text = str(y1)
        ET.SubElement(dst_box, 'xmax').text = str(x2)
        ET.SubElement(dst_box, 'ymax').text = str(y2)

    dst_tree = ET.ElementTree(dst_root)
    dst_path = os.path.split(sys.argv[1])[0].split(os.sep)[:-1]
    dst_path = os.sep.join(dst_path)
    dst_path = os.path.join(dst_path,src_image_path)

    string = ET.tostring(dst_tree.getroot(),'utf8')
    reparsed = minidom.parseString(string)

    with open(dst_path.replace('_color.png','_ann.xml'),'w') as xml:
        reparsed.writexml(xml,indent='  \n',addindent='\t')










