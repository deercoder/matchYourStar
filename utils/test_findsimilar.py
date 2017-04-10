#!/usr/bin/env python
import pickle
import httplib, urllib, base64
import json
import os
import shutil
import operator

# using raw image/file as body, header type should be different
raw_headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}

json_headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}

detect_params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
})

### Step 1: load the locally stored face id mapping
print "##### Step1: load faceid mapping for search later #####"

faceid_pair = pickle.load( open("save.p", "rb") )
print faceid_pair


### Step 2: detect face in query, fetch faceid
print "#### Step 2: detect face from test image to get faceID for querying request ####"
test_img = "/home/cliu/Downloads/IJSC_TSC_pic.jpg"
test_face_id = ""

try:
		print "detect face from test images ", test_img
		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		body = open(test_img, 'rb').read()
    		conn.request("POST", "/face/v1.0/detect?%s" % detect_params, body, raw_headers)
    		response = conn.getresponse()
    		data = response.read()
    		print(data)
    		conn.close()
	
		# parse the response string to JSON Array
		content = json.loads(data)	
		test_face_id = content[0]["faceId"]
		print test_face_id
	
except Exception as e:
		print str(e)


### Step 3: use faceID with images to query in the server
print "#### Step 3: use faceID to query in the server"

facelist = ["star_v1", "star_v2", "star_v3", "star_v4", "star_v5"]

### requet body for query/search using find similarity API

## fID:score that store sthe fiD and its condifentce
result_pair = {}

for item in facelist:
	query_body = "{" + \
    		"\"faceId\": \"%s\"," % test_face_id + \
    		"\"faceListId\": \"%s\"," % item + \
    		"\"maxNumOfCandidatesReturned\":10," + \
    		"\"mode\": \"matchFace\"" + \
    		"}"
	print "query_body is: ", query_body

	try:
    		body = open(test_img, 'rb').read()
    		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    		conn.request("POST", "/face/v1.0/findsimilars", query_body, json_headers)
    		response = conn.getresponse()
    		data = response.read()
    		print(data)
    		conn.close()
	except Exception as e:
    		print str(e)


	arr_data = json.loads(data)
	for det_ret in arr_data:
		det_persist_id = det_ret["persistedFaceId"]		
		det_score = det_ret["confidence"]
		mapped_original_face = faceid_pair[det_persist_id]
		print det_persist_id, det_score, mapped_original_face

		### insert into the pair to sort
		result_pair[det_persist_id] = float(det_score)
	
		path_list = test_img.split(os.sep)
		directory = "./" + path_list[-1][:-4]
		if not os.path.exists(directory):
			os.makedirs(directory)

		shutil.copyfile(mapped_original_face, directory+"/"+mapped_original_face.split(os.sep)[-1])		


### Step 4: stored the confidence pairs, sort them, use the correct fID and mapped filename to fetch top-k images
print result_pair
sorted_result_pair = sorted(result_pair.items(), key=operator.itemgetter(1))
sorted_result_pair.reverse()
print sorted_result_pair

path_list = test_img.split(os.sep)
directory = "./" + path_list[-1][:-4] + "/top-20"
if not os.path.exists(directory):
	os.makedirs(directory)


star_score = {}

if len(sorted_result_pair) < 20:
	## item is the key, for a dict
	i = 0
	for item in sorted_result_pair:
		shutil.copyfile(faceid_pair[item[0]], directory+"/"+ str(i) + "_" + faceid_pair[item[0]].split(os.sep)[-1])
		path_list = faceid_pair[item[0]].split(os.sep)
		people = path_list[-2]
		#print people
		star_score[people] = star_score.get(people, 0) + 1
		#print star_score[people]
		i = i + 1
else:
	i = 0
	### why?? sorted_result_pair is NOT dict, but list of tuples?????
	for item in sorted_result_pair:	
		# first fetch the item, then get key
		shutil.copyfile(faceid_pair[item[0]], directory+"/"+ str(i) + "_" + faceid_pair[item[0]].split(os.sep)[-1])
		i = i + 1
		path_list = faceid_pair[item[0]].split(os.sep)
		people = path_list[-2]
		#print people
		star_score[people] = star_score.get(people, 0) + 1
		#print star_score[people]
		if i == 20:
			break


### Step 5: sort the results
#print star_score
sorted_star_score = sorted(star_score.items(), key=operator.itemgetter(1))
sorted_star_score.reverse()
print sorted_star_score

i = 0
for item in sorted_star_score:
	# unicode has to be decoded as utf-8, then we can encode it using utf-8
	if i < 3:
		print "top-%d:"%(i+1), item[0].decode('utf-8').encode('utf-8')
	i += 1
