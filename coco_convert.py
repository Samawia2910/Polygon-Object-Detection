import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "doc/val"

# set path for coco json to be saved
save_json_path = "doc/instances_val2017.json"

# conert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)