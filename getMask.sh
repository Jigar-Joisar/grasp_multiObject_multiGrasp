cd yolov3/ 
python3 detect.py --save-txt --output "../tools/output12" --source "../data/demo" --conf-thres 0.1 
cd ..
cd tools/
python3 mask_gen.py