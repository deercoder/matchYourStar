#!/usr/bin/env python
import httplib, urllib, base64, glob
import json, io
from PIL import Image
import pickle
import os

json_headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}


# using raw image/file as body, header type should be different
raw_headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}


### Step2: Detect image's face

print "########Step 2: detect face from every image ########"

detect_params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
})


#facelist_params = urllib.urlencode({
#})

img_lists = []
folder_lists = glob.glob(u"/home/cliu/github/matchYourStar/icrawler/images/google/*/")
for item in folder_lists:
	print item.encode('utf-8')
	tmp_lists = glob.glob(item.encode('utf-8') + '/*.jpg')
	img_lists = img_lists + tmp_lists
	print img_lists

print len(img_lists)

facelist = ["star_v1", "star_v2", "star_v3", "star_v4", "star_v5"]
index = 0
count = 0
err_count = 0
faceid_pair = {}


for img in img_lists:
	try:
		print "detect face from ", img
		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		body = open(img, 'rb').read()
    		conn.request("POST", "/face/v1.0/detect?%s" % detect_params, body, raw_headers)
    		response = conn.getresponse()
    		data = response.read()
    		print(data)
    		conn.close()
	
		# parse the response string to JSON Array
		content = json.loads(data)	
		imgfile = Image.open(img)
		
		# list all rectangles in the image[faces]
		for item in content:
			top = int(item["faceRectangle"]["top"])
			left = int(item["faceRectangle"]["left"])
			width = int(item["faceRectangle"]["width"])
			height = int(item["faceRectangle"]["height"])
			print top, left, width, height
			crop_img = imgfile.crop((left, top, left+width, top+height))
			
			# debug, save the cropped the faces in case of error
			path_list = img.split(os.sep)
			crop_img.save("./test/" + path_list[-1][:-4] + "crop.jpg")	

			##### Step 3: add face regions into the faceList
			print "##### Step 3: add face regions into the faceList ##### "					

			# Construct the hex-data(binary) from PIL:Image structure
			#output = io.BytesIO()
			#crop_img.save(output, format="JPEG")
			#hex_data = output.getvalue()
			raw_img_data = open(img, 'rb').read()


			facelist_params = "targetFace=%d,%d,%d,%d"%(left, top, width, height)
			print "facelist_params of targetFace = ", facelist_params
    			conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    			conn.request("POST", "/face/v1.0/facelists/%s/persistedFaces?%s" % (facelist[index], facelist_params), raw_img_data, raw_headers)
    			response = conn.getresponse()
    			data = response.read()
    			print(data)
    			conn.close()

			datastr = json.loads(data)
			persist_id = datastr["persistedFaceId"]
			if persist_id is not None:
				faceid_pair[datastr["persistedFaceId"]] = img
				#print faceid_pair
			else:
				print "NULL!!!!!!"

			count = count + 1
			if (count % 1000 == 0):
				index = index + 1
				print faceid_pair
				print "Now processing: ", facelist[index]

	except Exception as e:
		err_count = err_count + 1
		print str(e)


### Step4: Save the dictionary into file (persist_id: file_name)
print "#### Step 4: saving dictionary and print it out ######"
pickle.dump(faceid_pair, open("save.p", "wb"))
print faceid_pair
print "total counts = ", count
print "error count(no face detected) = ", err_count
