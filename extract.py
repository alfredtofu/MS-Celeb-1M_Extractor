import os
import base64
import struct

fid = open("./MsCelebV1-Faces-Cropped.tsv", "r")
base_path = './MsCeleb/'
if not os.path.exists(base_path):
  os.mkdir(base_path)
bbox_file = open(base_path + '/bboxes.txt', 'w')
while True:
  line = fid.readline()
  if line:
    data_info = line.split('\t')
    # 0: Freebase MID (unique key for each entity)
    # 1: ImageSearchRank
    # 4: FaceID
    # 5: bbox
    # 6: img_data
    filename = data_info[0] + "/" + data_info[1] + "_" + data_info[4] + ".jpg"
    bbox = struct.unpack('ffff', data_info[5].decode("base64"))
    bbox_file.write(filename + " "+ (" ".join(str(bbox_value) for bbox_value  in bbox)) + "\n")

    img_data = data_info[6].decode("base64")
    output_file_path = base_path + "/" + filename 
    if os.path.exists(output_file_path):
      print output_file_path + " exists"

    output_path = os.path.dirname(output_file_path)
    if not os.path.exists(output_path):
      os.mkdir(output_path)

    img_file = open(output_file_path, 'w')
    img_file.write(img_data)
    img_file.close()
  else:
    break

bbox_file.close()
fid.close()
