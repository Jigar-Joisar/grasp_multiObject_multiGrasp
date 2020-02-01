cd yolov3/ 
python3 detect.py --save-txt --output "../tools/output" --source "../data/demo_color" --conf-thres 0.3 --classes 41 45 75 40 39
cd ..
cd tools/
python3 mask_gen.py