Find Your Star
====

This project is used for finding the most similar star according to the face similarity ranked by Microsoft Cognitive Service.

## Step 1: Prepare Dataset

Use `icrawler` to download the top-100 stars from China, according to the forbes ranking. The `test.py` under `icrawler` shows
the code to download every 50 images from Google Image Search.

## Step 2: Building facelist in the Cognitive Cloud Server

For each images in the above crawled folders, use Cognitive Service API to detect face, create facelist, add to facelist in the
cloud server, store the mapping locally.

## Step 3: Find face similiarity locally, rank by matched score

For one test image, use API to detect face, find face similarities and output all the matched top-20 scores. Then among these
20 results, count how many are corresponding to the exact star, then rank by the matches. The topped matches are the most likely
one, then the second one, third one. Output the top-3 matched stars

The output is like as follows:

```
5f586ded-0779-4d31-a4d3-ffb288829ca3 0.51954 /home/cliu/github/matchYourStar/icrawler/images/google/徐峥/000015.jpg
eeb5f02f-8a35-4cd5-8ebc-222548e2d04e 0.44692 /home/cliu/github/matchYourStar/icrawler/images/google/李晨/000037.jpg
a29406ac-4670-48f6-96b1-318994ffe696 0.43264 /home/cliu/github/matchYourStar/icrawler/images/google/唐家三少/000016.jpg
758b6a0b-1862-4ec5-b9f0-f41ea620fa68 0.42448 /home/cliu/github/matchYourStar/icrawler/images/google/汪峰/000028.jpg
3ddd5119-12ab-4f40-934d-411a6a3ced96 0.42319 /home/cliu/github/matchYourStar/icrawler/images/google/陈奕迅/000050.jpg
c06fc744-a0ff-4266-80d4-bf407a65a82f 0.42253 /home/cliu/github/matchYourStar/icrawler/images/google/徐峥/000020.jpg
18383cc7-a7c0-4057-bd8f-544a843f584d 0.39413 /home/cliu/github/matchYourStar/icrawler/images/google/李娜/000023.jpg
cf74f7b9-c9f6-4aa0-ada6-1bc29508d961 0.39346 /home/cliu/github/matchYourStar/icrawler/images/google/汪峰/000031.jpg
529b3c25-36f3-4885-b3f3-24253c5917e9 0.39201 /home/cliu/github/matchYourStar/icrawler/images/google/唐家三少/000004.jpg
65c61f9c-2e01-4c8b-a19b-7d396c1f5939 0.38661 /home/cliu/github/matchYourStar/icrawler/images/google/汪峰/000044.jpg
query_body is:  {"faceId": "3c74fcf2-9cf1-4ed9-be5f-59cee4962328","faceListId": "star_v2","maxNumOfCandidatesReturned":10,"mode": "matchFace"}
[{"persistedFaceId":"3e893584-d36b-4168-8688-758643174360","confidence":0.46626},{"persistedFaceId":"e18b9a45-6b85-4bb4-b46b-0a1bd6f093ae","confidence":0.45764},{"persistedFaceId":"540627cf-77e9-4c8f-867d-37bf48aef036","confidence":0.45671},{"persistedFaceId":"2cd2d030-a3f5-4c60-aa62-448892fb4c64","confidence":0.44804},{"persistedFaceId":"7e75ab6b-6d8e-47dd-b109-03f6ce1b7101","confidence":0.43223},{"persistedFaceId":"74b74da0-7dfb-4d80-86ad-8240ff97ffa6","confidence":0.42485},{"persistedFaceId":"22bd6189-f200-4f26-ae24-4d789fa5d37f","confidence":0.40984},{"persistedFaceId":"e42d9d84-1a1e-4737-9b15-ea517e8125a1","confidence":0.40799},{"persistedFaceId":"37812804-c555-4842-a958-cc00f489d8f2","confidence":0.3908},{"persistedFaceId":"a2e2e2c5-2733-4fe3-a6b8-78ffab3f6aa6","confidence":0.38503}]
3e893584-d36b-4168-8688-758643174360 0.46626 /home/cliu/github/matchYourStar/icrawler/images/google/吴镇宇/000021.jpg
e18b9a45-6b85-4bb4-b46b-0a1bd6f093ae 0.45764 /home/cliu/github/matchYourStar/icrawler/images/google/韩寒/000045.jpg
540627cf-77e9-4c8f-867d-37bf48aef036 0.45671 /home/cliu/github/matchYourStar/icrawler/images/google/周润发/000020.jpg
2cd2d030-a3f5-4c60-aa62-448892fb4c64 0.44804 /home/cliu/github/matchYourStar/icrawler/images/google/吴镇宇/000039.jpg
7e75ab6b-6d8e-47dd-b109-03f6ce1b7101 0.43223 /home/cliu/github/matchYourStar/icrawler/images/google/吴镇宇/000018.jpg
74b74da0-7dfb-4d80-86ad-8240ff97ffa6 0.42485 /home/cliu/github/matchYourStar/icrawler/images/google/陈晓/000021.jpg
22bd6189-f200-4f26-ae24-4d789fa5d37f 0.40984 /home/cliu/github/matchYourStar/icrawler/images/google/吴镇宇/000026.jpg
e42d9d84-1a1e-4737-9b15-ea517e8125a1 0.40799 /home/cliu/github/matchYourStar/icrawler/images/google/郭德纲/000005.jpg
37812804-c555-4842-a958-cc00f489d8f2 0.3908 /home/cliu/github/matchYourStar/icrawler/images/google/郭德纲/000043.jpg
a2e2e2c5-2733-4fe3-a6b8-78ffab3f6aa6 0.38503 /home/cliu/github/matchYourStar/icrawler/images/google/吴镇宇/000010.jpg
query_body is:  {"faceId": "3c74fcf2-9cf1-4ed9-be5f-59cee4962328","faceListId": "star_v3","maxNumOfCandidatesReturned":10,"mode": "matchFace"}
[{"persistedFaceId":"66d80917-0725-4850-b802-c9348115ec7a","confidence":0.4437},{"persistedFaceId":"9df06761-ba21-4c78-8f40-27ec1489e620","confidence":0.37993},{"persistedFaceId":"7fe484df-aaa4-4669-9b7a-75a5b2dbe7f4","confidence":0.37584},{"persistedFaceId":"a813ad04-8d12-4d94-a064-26bde9ab7e7f","confidence":0.37558},{"persistedFaceId":"cc544920-ea0c-4663-b656-0a41fb46398a","confidence":0.36826},{"persistedFaceId":"5b6a928c-f96c-4bf3-aa59-07e07d41f75e","confidence":0.36701},{"persistedFaceId":"a2598556-81fd-405e-b298-886b011a011f","confidence":0.36466},{"persistedFaceId":"7863dd68-ed5b-4b59-9236-eb8a07944422","confidence":0.36265},{"persistedFaceId":"05da8a14-6090-4c02-ae23-4e89ba03d173","confidence":0.35646},{"persistedFaceId":"e24df6fa-02fc-486b-b26f-f67b0b646073","confidence":0.34696}]
66d80917-0725-4850-b802-c9348115ec7a 0.4437 /home/cliu/github/matchYourStar/icrawler/images/google/宁浩/000040.jpg
9df06761-ba21-4c78-8f40-27ec1489e620 0.37993 /home/cliu/github/matchYourStar/icrawler/images/google/贾乃亮/000037.jpg
7fe484df-aaa4-4669-9b7a-75a5b2dbe7f4 0.37584 /home/cliu/github/matchYourStar/icrawler/images/google/Angelababy/000050.jpg
a813ad04-8d12-4d94-a064-26bde9ab7e7f 0.37558 /home/cliu/github/matchYourStar/icrawler/images/google/贾乃亮/000017.jpg
cc544920-ea0c-4663-b656-0a41fb46398a 0.36826 /home/cliu/github/matchYourStar/icrawler/images/google/胡歌/000021.jpg
5b6a928c-f96c-4bf3-aa59-07e07d41f75e 0.36701 /home/cliu/github/matchYourStar/icrawler/images/google/贾乃亮/000047.jpg
a2598556-81fd-405e-b298-886b011a011f 0.36466 /home/cliu/github/matchYourStar/icrawler/images/google/姜文/000025.jpg
7863dd68-ed5b-4b59-9236-eb8a07944422 0.36265 /home/cliu/github/matchYourStar/icrawler/images/google/贾乃亮/000038.jpg
05da8a14-6090-4c02-ae23-4e89ba03d173 0.35646 /home/cliu/github/matchYourStar/icrawler/images/google/胡歌/000034.jpg
e24df6fa-02fc-486b-b26f-f67b0b646073 0.34696 /home/cliu/github/matchYourStar/icrawler/images/google/胡歌/000041.jpg
query_body is:  {"faceId": "3c74fcf2-9cf1-4ed9-be5f-59cee4962328","faceListId": "star_v4","maxNumOfCandidatesReturned":10,"mode": "matchFace"}
[{"persistedFaceId":"9011d1e4-ef36-4e2e-94a5-d63ff5999665","confidence":0.5183},{"persistedFaceId":"cbed50e8-ccb9-42fa-8553-a2f621469ce0","confidence":0.4634},{"persistedFaceId":"513067f6-8462-4fc7-b146-94cfc7a40b34","confidence":0.45058},{"persistedFaceId":"7817eb12-5119-4305-9450-03d6f1b88427","confidence":0.44391},{"persistedFaceId":"54eb118e-9fcb-4714-a1e2-1c84a333843e","confidence":0.44336},{"persistedFaceId":"83ebe438-e7e2-461d-81f5-76bda369e060","confidence":0.4396},{"persistedFaceId":"a5a0dce6-fe83-4caa-82e3-2b54757abd65","confidence":0.43187},{"persistedFaceId":"64c99f64-719e-4c73-bf38-348f3c5e3887","confidence":0.43155},{"persistedFaceId":"6a113226-63b8-4428-b250-f366a1765a59","confidence":0.43134},{"persistedFaceId":"f9ce7131-ad68-404c-b8a3-177b5a14ea02","confidence":0.42914}]
9011d1e4-ef36-4e2e-94a5-d63ff5999665 0.5183 /home/cliu/github/matchYourStar/icrawler/images/google/黄磊/000038.jpg
cbed50e8-ccb9-42fa-8553-a2f621469ce0 0.4634 /home/cliu/github/matchYourStar/icrawler/images/google/黄磊/000010.jpg
513067f6-8462-4fc7-b146-94cfc7a40b34 0.45058 /home/cliu/github/matchYourStar/icrawler/images/google/黄渤/000047.jpg
7817eb12-5119-4305-9450-03d6f1b88427 0.44391 /home/cliu/github/matchYourStar/icrawler/images/google/林丹/000021.jpg
54eb118e-9fcb-4714-a1e2-1c84a333843e 0.44336 /home/cliu/github/matchYourStar/icrawler/images/google/王宝强/000005.jpg
83ebe438-e7e2-461d-81f5-76bda369e060 0.4396 /home/cliu/github/matchYourStar/icrawler/images/google/黄渤/000016.jpg
a5a0dce6-fe83-4caa-82e3-2b54757abd65 0.43187 /home/cliu/github/matchYourStar/icrawler/images/google/黄磊/000039.jpg
64c99f64-719e-4c73-bf38-348f3c5e3887 0.43155 /home/cliu/github/matchYourStar/icrawler/images/google/黄磊/000036.jpg
6a113226-63b8-4428-b250-f366a1765a59 0.43134 /home/cliu/github/matchYourStar/icrawler/images/google/黄渤/000012.jpg
f9ce7131-ad68-404c-b8a3-177b5a14ea02 0.42914 /home/cliu/github/matchYourStar/icrawler/images/google/黄渤/000029.jpg
query_body is:  {"faceId": "3c74fcf2-9cf1-4ed9-be5f-59cee4962328","faceListId": "star_v5","maxNumOfCandidatesReturned":10,"mode": "matchFace"}
[{"persistedFaceId":"0b88bf25-adf1-4496-8cba-c6b396615e7d","confidence":0.45066},{"persistedFaceId":"729daec1-2aa2-4ad0-9d26-9905056e884c","confidence":0.44396},{"persistedFaceId":"d6dca26c-4674-4f7c-b6e6-95575a37fe64","confidence":0.42734},{"persistedFaceId":"9244c25e-6436-41a4-aa86-30dbfa23b4de","confidence":0.4177},{"persistedFaceId":"a2ba3a53-ca0e-4797-8d78-037f3ee950ad","confidence":0.38005},{"persistedFaceId":"375cd198-57b6-41f2-b0e1-39f06a0e3c95","confidence":0.37693},{"persistedFaceId":"f063844f-a9a9-4708-a4e3-f760707900b1","confidence":0.37579},{"persistedFaceId":"eea5db1a-e9df-479f-bc1a-a406017b67ba","confidence":0.37544},{"persistedFaceId":"145d2afc-a2b2-47a3-86d5-cefb21878f2c","confidence":0.37364},{"persistedFaceId":"0137ac2e-bff1-4b7a-89b3-ea3e18dc9142","confidence":0.37222}]
0b88bf25-adf1-4496-8cba-c6b396615e7d 0.45066 /home/cliu/github/matchYourStar/icrawler/images/google/佟大为/000001.jpg
729daec1-2aa2-4ad0-9d26-9905056e884c 0.44396 /home/cliu/github/matchYourStar/icrawler/images/google/吴奇隆/000047.jpg
d6dca26c-4674-4f7c-b6e6-95575a37fe64 0.42734 /home/cliu/github/matchYourStar/icrawler/images/google/徐熙娣/000035.jpg
9244c25e-6436-41a4-aa86-30dbfa23b4de 0.4177 /home/cliu/github/matchYourStar/icrawler/images/google/陈赫/000012.jpg
a2ba3a53-ca0e-4797-8d78-037f3ee950ad 0.38005 /home/cliu/github/matchYourStar/icrawler/images/google/成龙/000002.jpg
375cd198-57b6-41f2-b0e1-39f06a0e3c95 0.37693 /home/cliu/github/matchYourStar/icrawler/images/google/成龙/000042.jpg
f063844f-a9a9-4708-a4e3-f760707900b1 0.37579 /home/cliu/github/matchYourStar/icrawler/images/google/陈赫/000008.jpg
eea5db1a-e9df-479f-bc1a-a406017b67ba 0.37544 /home/cliu/github/matchYourStar/icrawler/images/google/成龙/000005.jpg
145d2afc-a2b2-47a3-86d5-cefb21878f2c 0.37364 /home/cliu/github/matchYourStar/icrawler/images/google/张嘉译/000044.jpg
0137ac2e-bff1-4b7a-89b3-ea3e18dc9142 0.37222 /home/cliu/github/matchYourStar/icrawler/images/google/成龙/000027.jpg
{u'65c61f9c-2e01-4c8b-a19b-7d396c1f5939': 0.38661, u'e42d9d84-1a1e-4737-9b15-ea517e8125a1': 0.40799, u'64c99f64-719e-4c73-bf38-348f3c5e3887': 0.43155, u'5b6a928c-f96c-4bf3-aa59-07e07d41f75e': 0.36701, u'54eb118e-9fcb-4714-a1e2-1c84a333843e': 0.44336, u'9df06761-ba21-4c78-8f40-27ec1489e620': 0.37993, u'c06fc744-a0ff-4266-80d4-bf407a65a82f': 0.42253, u'e18b9a45-6b85-4bb4-b46b-0a1bd6f093ae': 0.45764, u'3e893584-d36b-4168-8688-758643174360': 0.46626, u'7863dd68-ed5b-4b59-9236-eb8a07944422': 0.36265, u'18383cc7-a7c0-4057-bd8f-544a843f584d': 0.39413, u'a5a0dce6-fe83-4caa-82e3-2b54757abd65': 0.43187, u'0b88bf25-adf1-4496-8cba-c6b396615e7d': 0.45066, u'145d2afc-a2b2-47a3-86d5-cefb21878f2c': 0.37364, u'eeb5f02f-8a35-4cd5-8ebc-222548e2d04e': 0.44692, u'f9ce7131-ad68-404c-b8a3-177b5a14ea02': 0.42914, u'66d80917-0725-4850-b802-c9348115ec7a': 0.4437, u'540627cf-77e9-4c8f-867d-37bf48aef036': 0.45671, u'a2598556-81fd-405e-b298-886b011a011f': 0.36466, u'3ddd5119-12ab-4f40-934d-411a6a3ced96': 0.42319, u'f063844f-a9a9-4708-a4e3-f760707900b1': 0.37579, u'd6dca26c-4674-4f7c-b6e6-95575a37fe64': 0.42734, u'a813ad04-8d12-4d94-a064-26bde9ab7e7f': 0.37558, u'eea5db1a-e9df-479f-bc1a-a406017b67ba': 0.37544, u'6a113226-63b8-4428-b250-f366a1765a59': 0.43134, u'529b3c25-36f3-4885-b3f3-24253c5917e9': 0.39201, u'5f586ded-0779-4d31-a4d3-ffb288829ca3': 0.51954, u'375cd198-57b6-41f2-b0e1-39f06a0e3c95': 0.37693, u'758b6a0b-1862-4ec5-b9f0-f41ea620fa68': 0.42448, u'05da8a14-6090-4c02-ae23-4e89ba03d173': 0.35646, u'cf74f7b9-c9f6-4aa0-ada6-1bc29508d961': 0.39346, u'0137ac2e-bff1-4b7a-89b3-ea3e18dc9142': 0.37222, u'e24df6fa-02fc-486b-b26f-f67b0b646073': 0.34696, u'9011d1e4-ef36-4e2e-94a5-d63ff5999665': 0.5183, u'37812804-c555-4842-a958-cc00f489d8f2': 0.3908, u'74b74da0-7dfb-4d80-86ad-8240ff97ffa6': 0.42485, u'2cd2d030-a3f5-4c60-aa62-448892fb4c64': 0.44804, u'7fe484df-aaa4-4669-9b7a-75a5b2dbe7f4': 0.37584, u'a2e2e2c5-2733-4fe3-a6b8-78ffab3f6aa6': 0.38503, u'9244c25e-6436-41a4-aa86-30dbfa23b4de': 0.4177, u'513067f6-8462-4fc7-b146-94cfc7a40b34': 0.45058, u'7817eb12-5119-4305-9450-03d6f1b88427': 0.44391, u'a2ba3a53-ca0e-4797-8d78-037f3ee950ad': 0.38005, u'cbed50e8-ccb9-42fa-8553-a2f621469ce0': 0.4634, u'83ebe438-e7e2-461d-81f5-76bda369e060': 0.4396, u'a29406ac-4670-48f6-96b1-318994ffe696': 0.43264, u'7e75ab6b-6d8e-47dd-b109-03f6ce1b7101': 0.43223, u'22bd6189-f200-4f26-ae24-4d789fa5d37f': 0.40984, u'729daec1-2aa2-4ad0-9d26-9905056e884c': 0.44396, u'cc544920-ea0c-4663-b656-0a41fb46398a': 0.36826}
[(u'5f586ded-0779-4d31-a4d3-ffb288829ca3', 0.51954), (u'9011d1e4-ef36-4e2e-94a5-d63ff5999665', 0.5183), (u'3e893584-d36b-4168-8688-758643174360', 0.46626), (u'cbed50e8-ccb9-42fa-8553-a2f621469ce0', 0.4634), (u'e18b9a45-6b85-4bb4-b46b-0a1bd6f093ae', 0.45764), (u'540627cf-77e9-4c8f-867d-37bf48aef036', 0.45671), (u'0b88bf25-adf1-4496-8cba-c6b396615e7d', 0.45066), (u'513067f6-8462-4fc7-b146-94cfc7a40b34', 0.45058), (u'2cd2d030-a3f5-4c60-aa62-448892fb4c64', 0.44804), (u'eeb5f02f-8a35-4cd5-8ebc-222548e2d04e', 0.44692), (u'729daec1-2aa2-4ad0-9d26-9905056e884c', 0.44396), (u'7817eb12-5119-4305-9450-03d6f1b88427', 0.44391), (u'66d80917-0725-4850-b802-c9348115ec7a', 0.4437), (u'54eb118e-9fcb-4714-a1e2-1c84a333843e', 0.44336), (u'83ebe438-e7e2-461d-81f5-76bda369e060', 0.4396), (u'a29406ac-4670-48f6-96b1-318994ffe696', 0.43264), (u'7e75ab6b-6d8e-47dd-b109-03f6ce1b7101', 0.43223), (u'a5a0dce6-fe83-4caa-82e3-2b54757abd65', 0.43187), (u'64c99f64-719e-4c73-bf38-348f3c5e3887', 0.43155), (u'6a113226-63b8-4428-b250-f366a1765a59', 0.43134), (u'f9ce7131-ad68-404c-b8a3-177b5a14ea02', 0.42914), (u'd6dca26c-4674-4f7c-b6e6-95575a37fe64', 0.42734), (u'74b74da0-7dfb-4d80-86ad-8240ff97ffa6', 0.42485), (u'758b6a0b-1862-4ec5-b9f0-f41ea620fa68', 0.42448), (u'3ddd5119-12ab-4f40-934d-411a6a3ced96', 0.42319), (u'c06fc744-a0ff-4266-80d4-bf407a65a82f', 0.42253), (u'9244c25e-6436-41a4-aa86-30dbfa23b4de', 0.4177), (u'22bd6189-f200-4f26-ae24-4d789fa5d37f', 0.40984), (u'e42d9d84-1a1e-4737-9b15-ea517e8125a1', 0.40799), (u'18383cc7-a7c0-4057-bd8f-544a843f584d', 0.39413), (u'cf74f7b9-c9f6-4aa0-ada6-1bc29508d961', 0.39346), (u'529b3c25-36f3-4885-b3f3-24253c5917e9', 0.39201), (u'37812804-c555-4842-a958-cc00f489d8f2', 0.3908), (u'65c61f9c-2e01-4c8b-a19b-7d396c1f5939', 0.38661), (u'a2e2e2c5-2733-4fe3-a6b8-78ffab3f6aa6', 0.38503), (u'a2ba3a53-ca0e-4797-8d78-037f3ee950ad', 0.38005), (u'9df06761-ba21-4c78-8f40-27ec1489e620', 0.37993), (u'375cd198-57b6-41f2-b0e1-39f06a0e3c95', 0.37693), (u'7fe484df-aaa4-4669-9b7a-75a5b2dbe7f4', 0.37584), (u'f063844f-a9a9-4708-a4e3-f760707900b1', 0.37579), (u'a813ad04-8d12-4d94-a064-26bde9ab7e7f', 0.37558), (u'eea5db1a-e9df-479f-bc1a-a406017b67ba', 0.37544), (u'145d2afc-a2b2-47a3-86d5-cefb21878f2c', 0.37364), (u'0137ac2e-bff1-4b7a-89b3-ea3e18dc9142', 0.37222), (u'cc544920-ea0c-4663-b656-0a41fb46398a', 0.36826), (u'5b6a928c-f96c-4bf3-aa59-07e07d41f75e', 0.36701), (u'a2598556-81fd-405e-b298-886b011a011f', 0.36466), (u'7863dd68-ed5b-4b59-9236-eb8a07944422', 0.36265), (u'05da8a14-6090-4c02-ae23-4e89ba03d173', 0.35646), (u'e24df6fa-02fc-486b-b26f-f67b0b646073', 0.34696)]
[('\xe9\xbb\x84\xe7\xa3\x8a', 4), ('\xe9\xbb\x84\xe6\xb8\xa4', 3), ('\xe5\x90\xb4\xe9\x95\x87\xe5\xae\x87', 3), ('\xe7\x8e\x8b\xe5\xae\x9d\xe5\xbc\xba', 1), ('\xe4\xbd\x9f\xe5\xa4\xa7\xe4\xb8\xba', 1), ('\xe5\x91\xa8\xe6\xb6\xa6\xe5\x8f\x91', 1), ('\xe6\x9d\x8e\xe6\x99\xa8', 1), ('\xe5\x94\x90\xe5\xae\xb6\xe4\xb8\x89\xe5\xb0\x91', 1), ('\xe6\x9e\x97\xe4\xb8\xb9', 1), ('\xe9\x9f\xa9\xe5\xaf\x92', 1), ('\xe5\xbe\x90\xe5\xb3\xa5', 1), ('\xe5\x90\xb4\xe5\xa5\x87\xe9\x9a\x86', 1), ('\xe5\xae\x81\xe6\xb5\xa9', 1)]
top-1: 黄磊
top-2: 黄渤
top-3: 吴镇宇
```
