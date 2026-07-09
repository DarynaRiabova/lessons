import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)

tree = ET.parse("/Volumes/Untitled/hillel/lesson_1/lesson_15/groups.xml")
root = tree.getroot()


def find_incoming(number):
    for group in root.findall("group"):
        if group.find("number").text == str(number):
            return group.find("timingExbytes/incoming").text


logging.info(find_incoming(2))
