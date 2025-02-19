import requests
import os
import random
import time
from tqdm import tqdm
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

load_dotenv()

# def download_trim_downscale_video(clip_duration=1, min_video_len=10, max_video_len=20, output_dir="videos"):
#     """
#     Download a DCI 4K video and trim to specified duration from a random position.
#     clip_duration: desired clip duration in seconds
#     min_video_len: minimum video length in seconds
#     max_video_len: maximum video length in seconds
#     """
    
#     api_key = os.getenv("PEXELS_API_KEY")
    
#     os.makedirs(output_dir, exist_ok=True)
    
#     headers = {"Authorization": api_key}
#     url = "https://api.pexels.com/videos/search"
#     params = {
#         "query": "nature",
#         "per_page": 80,
#         "size": "large"
#     }
    
#     try:
#         # Step 1: Get video list
#         start_time = time.time()
#         response = requests.get(url, headers=headers, params=params)
#         data = response.json()
#         elapsed_time = time.time() - start_time
#         print(f"Time taken to fetch videos: {elapsed_time:.2f} seconds")
        
#         if "videos" not in data:
#             print("No videos found or API error")
#             return
        
#         # Step 2: Filter DCI 4K videos based on length
#         dci4k_videos = []
#         for video in data["videos"]:
#             video_length = video["duration"]
#             # Filter for DCI 4K videos (4096x2160)
#             dci4k_files = [f for f in video["video_files"] if f["width"] == 4096 and f["height"] == 2160]
#             if dci4k_files and min_video_len <= video_length <= max_video_len:
#                 dci4k_videos.append((video, dci4k_files[0]))
        
#         if not dci4k_videos:
#             print("No suitable DCI 4K videos found")
#             return
        
#         # Step 3: Randomly select one video
#         video, video_file = random.choice(dci4k_videos)
#         video_url = video_file["link"]
        
#         temp_path = f"{output_dir}/{video['id']}_4k_original.mp4"  # Downloaded DCI 4K file
#         clipped_path = f"{output_dir}/{video['id']}_4k.mp4"  # Clipped DCI 4K file
#         hd_path = f"{output_dir}/{video['id']}_hd.mp4"  # Downscaled HD file
#         hevc_path = f"{output_dir}/{video['id']}_hd.hevc"  # HEVC file
#         video_id = video['id']
        
#         # Step 4: Download video
#         print(f"\nDownloading DCI 4K video...")
#         print(f"Resolution: {video_file['width']}x{video_file['height']}")
#         print(f"Original duration: {video['duration']}s")
        
#         start_time = time.time()
#         response = requests.get(video_url, stream=True)
#         total_size = int(response.headers.get('content-length', 0))
        
#         with open(temp_path, 'wb') as f, tqdm(
#             desc="Downloading",
#             total=total_size,
#             unit='iB',
#             unit_scale=True,
#             unit_divisor=1024,
#         ) as pbar:
#             for data in response.iter_content(chunk_size=1024):
#                 size = f.write(data)
#                 pbar.update(size)
        
#         elapsed_time = time.time() - start_time
#         print(f"Time taken to download video: {elapsed_time:.2f} seconds")
        
#         # Step 5: Trim video
#         print("\nTrimming video...")
#         start_time = time.time()
#         video_clip = VideoFileClip(temp_path)
        
#         if video_clip.duration <= clip_duration:
#             print(f"Video is shorter than {clip_duration}s, keeping full length")
#             start_time_clip = 0
#         else:
#             max_start = video_clip.duration - clip_duration
#             start_time_clip = random.uniform(0, max_start)
#             print(f"Trimming {clip_duration}s from position {start_time_clip:.1f}s")
        
#         # Create clipped video
#         clipped_clip = video_clip.subclip(start_time_clip, start_time_clip + min(clip_duration, video_clip.duration))
#         clipped_clip.write_videofile(clipped_path, codec='libx264')
        
#         elapsed_time = time.time() - start_time
#         print(f"Time taken to clip video: {elapsed_time:.2f} seconds")
        
#         # Step 6: Downscale to HD and save as .mp4 using the clipped video
#         print("\nSaving HD version...")
#         start_time = time.time()
#         hd_clip = clipped_clip.resize(height=1080)  # Resize to HD (1080p) using the clipped video
#         hd_clip.write_videofile(hd_path, codec='libx264')  # Save as HD .mp4
        
#         elapsed_time = time.time() - start_time
#         print(f"Time taken to save HD version: {elapsed_time:.2f} seconds")
        
#         # Step 7: Convert to HEVC
#         # print("\nConverting to HEVC...")
#         # start_time = time.time()
#         # hd_clip.write_videofile(hevc_path, codec='libx265')  # Convert to HEVC
        
#         elapsed_time = time.time() - start_time
#         print(f"Time taken to convert to HEVC: {elapsed_time:.2f} seconds")
        
#         # Cleanup
#         video_clip.close()
#         clipped_clip.close()
#         hd_clip.close()
        
#         print(f"\nDone! Saved to: {temp_path}, {clipped_path}, {hd_path}, and {hevc_path}")
        
#         # return hevc_path, video_id
#         return hd_path, video_id
        
#     except Exception as e:
#         print(f"Error: {str(e)}")

# api_key = os.getenv("PEXELS_API_KEY")

# def fetch_4k_video_ids(query_list=None, max_results=2000):
#     """
#     Fetch video IDs of DCI 4K resolution (4096x2160) from Pexels API.
    
#     query_list: List of search terms to broaden results.
#     max_results: Maximum number of video IDs to return.
    
#     Returns a list of video IDs.
#     """
#     api_key = os.getenv("PEXELS_API_KEY")
#     if not api_key:
#         print("Error: Missing Pexels API Key")
#         return []

#     headers = {"Authorization": api_key}
    
#     if query_list is None:
#         query_list = ["nature", "landscape", "city", "ocean", "mountains", "forest", "water", "sunset"]

#     valid_video_ids = []
#     per_page = 80  # Max allowed by Pexels API
    
#     for query in query_list:
#         page = 1
#         while len(valid_video_ids) < max_results:
#             params = {
#                 "query": query,
#                 "per_page": per_page,
#                 "page": page,
#                 "size": "large",
#             }
            
#             try:
#                 response = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)
#                 response.raise_for_status()
#                 data = response.json()
                
#                 if "videos" not in data or not data["videos"]:
#                     print(f"No more videos found for '{query}' on page {page}.")
#                     break  # Stop paging for this query
                
#                 # Filter only DCI 4K (4096x2160) videos
#                 for video in data["videos"]:
#                     dci4k_files = [f for f in video["video_files"] if f["width"] == 4096 and f["height"] == 2160]
#                     if dci4k_files:
#                         valid_video_ids.append(video["id"])
                
#                 print(f"Fetched {len(valid_video_ids)} valid 4K videos so far...")

#                 if len(data["videos"]) < per_page:  
#                     break  # Stop if no more pages available

#                 page += 1  # Go to the next page
            
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching videos for '{query}': {e}")
#                 break  # Move to the next query if an error occurs
    
#     print(f"Total DCI 4K videos found: {len(valid_video_ids)}")
#     return valid_video_ids

import requests
import os
import random

def get_video_resolution(video_id):
    """
    Fetches the resolution details of a specific video from Pexels.
    
    video_id: The ID of the Pexels video.
    
    Returns a tuple (width, height) or None if the request fails.
    """
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        print("Error: Missing Pexels API Key")
        return None

    headers = {"Authorization": api_key}
    url = f"https://api.pexels.com/videos/videos/{video_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "video_files" not in data:
            print(f"No resolution data found for video ID {video_id}")
            return None

        # Extract the highest resolution available
        best_resolution = max(data["video_files"], key=lambda f: f["width"] * f["height"])
        return best_resolution["width"], best_resolution["height"]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching video ID {video_id}: {e}")
        return None

while True:
    # Load your saved list of 500 video IDs
    video_ids = [1448735, 4919750, 4763826, 1874715, 4887282, 4887279, 2257054, 4887915, 4887912, 4060265, 856479, 2248630, 4887913, 4206989, 4503294, 4887281, 4887276, 4185204, 3880377, 4887907, 4215373, 4651625, 4332086, 8371593, 2360941, 3151482, 3151442, 8114890, 3433955, 8334943, 4919748, 3151463, 1443653, 8418270, 6933752, 4887185, 8747377, 8418269, 8747376, 9153874, 8114996, 856480, 30635884, 30708755, 30706266, 30706265, 30706264, 2491284, 1858244, 1390942, 10214232, 6933537, 5639717, 9632691, 856478, 1394254, 1583096, 9153882, 1436812, 5639718, 1454363, 857268, 4937374, 5966363, 10214233, 5416362, 2491282, 4652096, 5668821, 4763786, 3191421, 5667131, 1564582, 3191109, 856481, 10556461, 2965291, 10559394, 3704256, 5639701, 8419637, 8344020, 4763869, 3151436, 8968930, 8208004, 10570816, 10140478, 1966382, 4763823, 4254118, 4937781, 2851008, 8207846, 5013967, 11266060, 4881698, 5616868, 10214240, 7944931, 8969048, 3191251, 10677317, 5415979, 10499646, 5435288, 4937038, 4762563, 11025568, 5128911, 5639714, 2558580, 1681023, 3998275, 4272432, 8348420, 4921860, 4936971, 4974438, 6318317, 6014225, 5280134, 4763787, 5358965, 10544197, 10544199, 7944614, 4921862, 4938470, 5667127, 2908583, 11025693, 10559385, 5427576, 4928695, 4974755, 2927933, 5385964, 5616866, 5679002, 10559105, 10570847, 8891325, 7353189, 8091551, 4763871, 8447510, 4882635, 4762901, 3972289, 10384139, 18089625, 8891324, 7354245, 8231639, 1181911, 4762565, 4933713, 5427562, 10384145, 10384145, 10570819, 10653575, 9166286, 8795959, 8968000, 5978075, 5640075, 5126545, 3150402, 5638276, 10678275, 10678345, 10214235, 10485794, 4762566, 9800130, 4937032, 4936972, 2958503, 4332083, 5365060, 5427565, 5827666, 10559384, 10536481, 10570725, 10220174, 8891327, 9800135, 10203948, 11760013, 4058085, 5978814, 6837432, 2895754, 5827662, 6134582, 4927963, 4921861, 4993933, 5126333, 3826737, 5667134, 5966354, 6650240, 10678930, 10677319, 9428862, 7663345, 4269182, 4938103, 11760750, 9800121, 3150403, 6134637, 5669120, 4927323, 4908195, 4921859, 4936978, 5126335, 3704257, 3998280, 3992463, 5427331, 5795043, 6610060, 10484749, 18089314, 10213767, 10558691, 9631752, 10570820, 8208008, 8746767, 8190638, 19805999, 6541895, 6208342, 5639706, 5640074, 4928679, 4937775, 5390478, 5627476, 5658998, 5668618, 6398499, 8335344, 11264796, 11760746, 10556806, 10556701, 10536487, 10570122, 10499656, 10556691, 10678288, 8398057, 8232440, 8207842, 8208010, 7944941, 8208015, 8335344, 11264796, 11760746, 10556806, 4101231, 6008074, 5668620, 5640072, 4908205, 4937034, 4933720, 5128908, 3151454, 3943279, 3151462, 6610065, 19093555, 10384140, 10435533, 10537262, 10543884, 10678273, 9861587, 10558692, 10558695, 10499649, 10499657, 8891321, 10559392, 7353182, 4254119, 7353182, 4254119, 7523416, 8231493, 5427575, 10559392, 5826916, 6016143, 6620930, 6255492, 5615991, 5639716, 5617017, 5668810, 4908206, 4938105, 5027202, 4763032, 4763872, 4925965, 4938046, 4504159, 2927931, 3151449, 3826730, 5415975, 5980032, 5978392, 10384147, 10544170, 10558699, 10601395, 10677318, 10677322, 10556463, 10556465, 10537263, 8968434, 8968534, 9153883, 10220218, 10485454, 12724036, 4139992, 8348502, 8357295, 8517520, 8091705, 7884026, 5416358, 4763785, 8362274, 10220218, 10485454, 12724036, 1841002, 6016400, 6609509, 6636878, 5639713, 5659913, 5637324, 5668820, 5826917, 6134576, 6134627, 6118044, 4921866, 5126552, 4786649, 4937035, 5102663, 4937778, 4937779, 4919853, 5128919, 4502464, 3992584, 4269187, 5473978, 5666725, 5840477, 5795049, 5854338, 5960698, 6650294, 6620500, 6063484, 8447704, 8968972, 9063826, 11265370, 11760783, 10049411, 10601399, 9799935, 9799899, 10537258, 10667657, 10556695, 10556696, 10559108, 10570717, 9907159, 10034023, 10220171, 11759805, 12354766, 12715013, 6777067, 8360962, 7353183, 7353185, 8233015, 8231577, 8968001, 4936166, 8447704, 8968972, 9063826, 11265370, 11760783, 10049411, 10601399, 9799935, 9799899, 2491285, 6016144, 5265096, 6318574, 2895749, 6120138, 5659157, 5874065, 4911913, 4800098, 4918173, 4927329, 4927330, 4763031, 4503695, 4594921, 4578034, 4578035, 4612981, 2519222, 3998269, 5853152, 5978806, 6610053, 10678923, 10536904, 10558701, 10570850, 10570986, 10678377, 18089238, 10213766, 10213769, 10570665, 10499644, 10536924, 10556807, 10203475, 10212662, 10613633, 10678384, 9586827, 9153877, 10363702, 10678920, 10495022, 10839346, 9798089, 7236525, 7038134, 4612264, 8745304, 8745308, 4272382, 4739598, 8348370, 7944943, 8091541, 8232678, 7884046, 7278989, 8891043, 5126746, 5126757, 9800137, 9800137, 7236525, 7038134, 10839346, 10363702, 10678920, 10495022, 5978078, 6016148, 5978986, 6620812, 5617016, 5679004, 5658773, 5637476, 6117580, 6134571, 6134577, 4762418, 4821109, 4918223, 4937167, 4927326, 4929835, 4932538, 4938141, 4937370, 4937033, 4937782, 4874612, 5119551, 4821115, 5119551, 4821115, 3151460, 2927937, 3151458, 3992469, 4057976, 4203563, 5329313, 5416024, 5416026, 5645686, 5290794, 5795135, 5855901, 5874447, 5794699, 5978699, 6621144, 10679051, 10453251, 10493904, 10499742, 10536484, 10556697, 10559386, 10559389, 10670002, 10677382, 10677458, 10678279, 18089380, 19806005, 10679051, 10453251, 10493904, 10499742, 10536484, 10556697, 10559386, 10559389, 10670002, 10677382, 10677458, 10678279, 18089380, 9950684, 10559110, 10570120, 10570126, 10570660, 10570662, 10570817, 10499650, 10499659, 10556464, 10556546, 10556547, 10556690, 10203957, 5976551, 6320379, 10839351, 9798090, 9906582, 11025497, 7038136, 4513018, 4270947, 4739667, 7353954, 8418263, 8891110, 7538711, 8191385, 8232557, 8231634, 8232810, 8107796, 8075703, 8795424, 8865366, 4763471, 4945360, 4762421, 9799824, 9632692, 10049406, 9862722, 9733975, 9798088, 9799829, 19806005, 5978825, 6016150, 5978885, 5981558, 6331330, 6620815, 2256072, 2895820, 2932339, 3626972, 6256817, 6133102, 5639709, 5659909, 5616864, 5637314, 5667408, 5658544, 6134584, 6184545, 4887477, 4887663, 4911914, 4921867, 4937172, 4928667, 4928668, 5028340, 4908396, 4908399, 4937369, 4938045, 5125035, 4513059, 5120249, 4651925, 2851007, 2908570, 2927947, 3912498, 4332085, 4188834, 3992465, 4185212, 4272421, 5542375, 5615994, 5852984, 5926952, 5853148, 5692165, 5875725, 5826919, 5978808, 6639953, 6421252, 16769840, 10212070, 10384142, 10534246, 10556698, 10556700, 10556705, 10569178, 10569291, 10559119, 10559387, 10570987, 10602196, 10660703, 10669195, 10678927, 10677463, 10677479, 12032406, 10549749, 10556805, 10569167, 9862548, 10045433, 9797821, 9797822, 9800124, 9733912, 9733917, 16769840, 10212070, 10384142, 10534246, 10556698, 10556700, 10556705, 10569178, 10569291, 10559119, 10559387, 10570987, 10602196, 10660703, 10669195, 10678927, 10677463, 10677479, 9304251, 11760020, 10210554, 10214231, 10367204, 10559117, 10559118, 10570119, 10559391, 10559395, 10203950, 10203952, 10203953, 10220215, 10366518, 10484780, 10493914, 10545052, 11760285, 11760301, 5976563, 12481758, 11025402, 4503287, 4651367, 12481758, 11025402, 6305801, 7353180, 7353188, 4739596, 8357166, 8348004, 8418260, 7481859, 7496395, 7354247, 7509029, 8208130, 8231713, 8191389, 6620469, 7190326, 6975441, 7109476, 8724236, 5364842, 5390479, 4762782, 4927545, 5372326, 5279934, 856477, 5275207, 8343767, 8331808, 8961642, 9797816, 9797818, 9836646, 12032406, 10549749, 10556805, 10569167, 9862548, 10045433, 9797821, 9797822, 9800124, 9733912, 9733917, 3723653, 5978083, 5994915, 5978981, 5977917, 6008080, 6318572, 6650190, 6811237, 6837588, 6541889, 6636887, 6620929, 6636781, 2932340, 3943588, 6255484, 5639705, 5668613, 5678005, 5640076, 5678965, 5923463, 5923466, 5951212, 5841958, 6134572, 6134581, 6256990, 6255500, 6183916, 4762422, 4763081, 4763082, 4821102, 4887410, 4887482, 4927726, 4933885, 4933886, 4932584, 4937166, 4762371, 4908194, 4938143, 4762968, 4830304, 4887189, 4887192, 4908394, 4919854, 4937372, 4937780, 5126326, 5128922, 4936974, 4937726, 5084215, 5125037, 4828294, 4911896, 4503918, 3046683, 3150400, 3959601, 2912907, 3151453, 3278949, 3967163, 1396928, 1466464, 4273471, 4008327, 4057973, 4185218, 4272429, 5417149, 5427335, 5429929, 5435724, 5365340, 5435290, 5386138, 5616865, 5636707, 5645685, 5853030, 5875723, 5701927, 5833142, 5976340, 5721748, 5978809, 6609494, 6620517, 6621171, 6636748, 6470389, 6608005, 6328203, 6328625, 6328481, 5632845, 6965769, 10384146, 10453246, 10453491, 10485460, 10651087, 10212506, 10484750, 10485797, 10499746, 10556693, 10556694, 10556702, 10556704, 10558696, 10570849, 10570989, 18812522, 10213764, 10213768, 10570125, 10570659, 10570721, 9291176, 9292894, 10212073, 10499643, 10499647, 10556692, 10569162, 10203602, 10203607, 9799828, 9799832, 9733957, 10384146, 10453246, 10453491, 10485460, 10651087, 10212506, 10484750, 10485797, 10499746, 10556693, 10556694, 10556702, 10556704, 10558696, 10570849, 10570989, 18812522, 12715035, 11760007, 5977442, 6320404, 6320760, 11760131, 12715012, 9553595, 9943173, 8968592, 7243383, 4595180, 4188339, 4188463, 4269130, 4739641, 8747385, 8692170, 7353187, 7354256, 4269126, 4631139, 4736803, 8370808, 8435959, 8371167, 8865369, 8869461, 8865227, 8968192, 8447605, 6805037, 8865369, 8869461, 8865227, 8968192, 8447605, 6805037, 7354249, 7354834, 7614803, 8231590, 8343754, 8189761, 8191326, 8207843, 8231580, 8121059, 8190212, 8191097, 8077301, 8191332, 6803085, 7243382, 8428493, 8844495, 8968044, 8746813, 8865223, 8795666, 8909664, 8891044, 8865607, 8910048, 5385960, 5385962, 5416134, 5427791, 5538178, 4993938, 3967206, 4996615, 5013968, 5128789, 5365073, 9389084, 9794025, 8447664, 8371486, 8191046, 8334109, 8335342, 8795652, 8968733, 8968862, 9037421, 8968971, 9798086, 9907158, 10543889, 10543890, 10543892, 10556804, 10569166, 10569169, 10569170, 10569173, 10600944, 9733950, 9800123, 9961932, 9800129, 9862723, 9733888, 9733974, 9733977, 9734051, 9799828, 9799832, 9733957, 3972389, 5977922, 5993799, 6016551, 6016552, 6013196, 5979471, 5979715, 5977940, 6318569, 6650172, 6650206, 6636788, 6650241, 6620291, 6980573, 3014063, 3943336, 3959614, 6133539, 6255483, 6255487, 5617010, 5617014, 5617015, 5658999, 5639399, 5639720, 5637323, 5678014, 5639719, 5639703, 5951213, 5966547, 5876313, 5874061, 6134629, 6256992, 6293203, 6294930, 6133754, 6184263, 6256580, 6132960, 6256779, 6256780, 4762323, 4887403, 4887404, 4887407, 4887480, 4887668, 4887672, 4888024, 4921869, 4921870, 4937168, 4945339, 5119285, 4800100, 4909853, 4909959, 4928672, 4927725, 4937031, 4886864, 4909658, 4909660, 4933910, 4938468, 4974428, 4974431, 4762906, 4762967, 4762969, 4887043, 4908398, 4920651, 4938043, 4974426, 5124629, 5124633, 4919746, 4919749, 4938039, 4938041, 4819601, 4993176, 5027581, 4921864, 4974434, 4974436, 4555729, 4502467, 4503957, 2912917, 2850991, 1874725, 2249469, 3151452, 2908574, 2908585, 3954976, 3838402, 2958502, 2932295, 4254115, 4275787, 4185348, 4188338, 4057923, 5590932, 5358952, 5358954, 5429928, 5429930, 5385967, 5396551, 5496176, 5358960, 5358966, 5415976, 5415932, 5329484, 5615840, 5666505, 5666506, 5615836, 5632851, 5926140, 5926951, 5819488, 5934658, 5934660, 5960696, 5967724, 5925967, 5838667, 6008085, 6566843, 6610055, 6610064, 6620518, 6650237, 6318314, 6328200, 6328202, 6256793, 7015962, 7038130, 9943800, 10212071, 10537259, 10652883, 10679050, 11760302, 9892810, 9941080, 9961756, 10143261, 10212499, 10435032, 10484752, 10536483, 10543885, 10536901, 10536909, 10556707, 10558704, 10569293, 10570851, 10570988, 10661878, 10678375, 10678376, 10665533, 10678925, 10677321, 10677460, 10677461, 8968458, 8968530, 8968859, 9049359, 11025490, 9800133, 10132245, 10548179, 10569168, 10569171, 10569175, 10601157, 9999478, 10033146, 10034019, 9861973, 9798100, 9798104, 9799900, 9943800, 10212071, 10537259, 10652883, 10679050, 11760302, 9892810, 9941080, 9961756, 10143261, 10212499, 10435032, 10484752, 10536483, 10543885, 10536901, 10536909, 10556707, 10558704, 10569293, 10570851, 10570988, 10661878, 10678375, 10678376, 10665533, 10678925, 10677321, 10677460, 10677461, 18209569, 9836548, 9861590, 9861592, 9950685, 10203255, 10215315, 10215321, 10212502, 10212661, 10536485, 10543895, 10534252, 10569161, 10559109, 10570723, 10602090, 9293442, 9389096, 9943274, 10212507, 10485789, 10484386, 10556548, 10556549, 10632772, 9941137, 10046894, 10203470, 10203958, 10220214, 10485787, 10660696, 10661678, 10667648, 10667654, 10667777, 10678381, 10678415, 10678757, 10678916, 10670007, 8865483, 8891316, 8889751, 8889788, 8916901, 8447344, 8968546, 9242522, 9292898, 8943769, 4503290, 4272659, 4273472, 4709633, 4739655, 6693842, 6305785, 7658503, 7658511, 8745391, 8746009, 8724231, 8640842, 7664029, 4269115, 4269184, 4300850, 4736801, 4686904, 8418266, 8435868, 8435870, 8357290, 8845448, 8845147, 8927768, 8845147, 8927768, 6811076, 7539277, 7621844, 7481708, 7538863, 7494121, 7494737, 7505109, 7539585, 7539590, 7354825, 7507019, 7622305, 7354826, 7431512, 7481856, 7539592, 8143239, 8191386, 8191222, 8231625, 8191054, 8191015, 8191042, 8189925, 8231635, 8191383, 8208131, 8208132, 7876576, 8191268, 8233005, 7778210, 7877154, 8107567, 8191018, 8191019, 7944930, 8231300, 7976078, 7788771, 7884048, 7944617, 8191008, 8077761, 8191390, 8191265, 6620470, 7109350, 7243862, 8419108, 8844504, 8841376, 8968009, 8629582, 8692159, 8927748, 8918124, 8925160, 8795159, 8865363, 8967997, 8865809, 5364841, 5365072, 5388634, 5415986, 5416359, 4763473, 4873808, 4936156, 4937036, 4937728, 2491277, 5591029, 4763086, 5103580, 9441293, 9586824, 9631900, 9733958, 8441006, 6768265, 10839355, 11760756, 9834571, 9941139, 9836597, 10213760, 10214236, 10214238, 10366815, 10366721, 10366722, 10436069, 10544163, 10544164, 10544167, 10212657, 10366807, 10484772, 10484385, 10499748, 10494886, 11760149, 11760753, 26627558, 5976549, 5976553, 6320389, 8626584, 2248641, 2908582, 3943127, 3967182, 3973051, 5978082, 6015156, 6008072, 5795215, 5832999, 6016550, 6014221, 6014235, 6008089, 6002908, 5265098, 5260022, 5265097, 4659721, 5979710, 6016405, 5979916, 6397754, 6328629, 6318308, 6328213, 6063481, 6609506, 6621215, 6620925, 6621237, 6650286, 6551819, 6636080, 1583096, 1436812, 3151442, 1443653, 2851008, 1454363, 1448735, 2932335, 2360941, 1874715, 4919748, 2932343, 4763786, 4887915, 2253719, 4763869, 4887912, 4887907, 3150402, 4763826, 1003936, 4060265, 2248641, 30708755, 30706266, 30706265, 30706264, 10839348, 10214232, 6933537, 4919750, 1394254, 9153882, 5966363, 10214233, 2491282, 3151482, 5667131, 1564582, 856481, 10559394, 5639701, 8419637, 3151436, 856479, 1966382, 4763823, 4254118, 4937781, 11266060, 5013967, 8969048, 7944931, 10214240, 10677317, 5415979, 4937038, 4762563, 5128911, 4887279, 1681023, 3151463, 6118049, 4936971, 6318317, 5280134, 4763787, 10544199, 4921862, 4887913, 5616866, 10559105, 10570847, 4763871, 4762901, 4887282, 18089625, 4762565, 11892760, 8795959, 8968000, 5126545, 3723554, 5638276, 10214235, 10485794, 4762566, 4937032, 2958503, 5427565, 10559384, 10570725, 10203948, 11760013, 10203948, 11760013, 5978814, 2895754, 5827662, 4927963, 4921861, 5126333, 5667134, 5966354, 6650240, 11760750, 7663345, 5669120, 4921859, 4936978, 5795043, 18089314, 10213767, 10558691, 10570820, 19805999, 6208342, 5640074, 4928679, 4937775, 6398499, 10570122, 8232440, 8865816, 8335344, 11264796, 10556806, 6008074, 4937034, 5128908, 3151454, 3151462, 19093555, 10537262, 10543884, 10678273, 9861587, 10558692, 10499649, 10499657, 10559392, 8436253, 8968542, 2248630, 5826916, 6016143, 6255492, 5639716, 5617017, 4938105, 4763032, 4763872, 4925965, 4938046, 4504159, 2927931, 3151449, 5845751, 10544170, 10558699, 10601395, 10677322, 8968434, 8968534, 9153883, 10220218, 8357295, 8418270, 4763785, 8419638, 9834903, 5826917, 5126552, 4786649, 5102663, 4937779, 5128919, 5666725, 5840477, 5854338, 6650294, 10556695, 10556696, 10559108, 9907159, 10034023, 9153871, 10559108, 9907159, 10034023, 9153871, 24984223, 20244149, 12354766, 8233015, 7109368, 6777067, 10214239, 10553956, 10559393, 11759805, 11760015, 2491285, 6318574, 2895749, 6120138, 5659157, 4918173, 4763031, 4594921, 4578034, 4578035, 2938865, 4185204, 5845260, 6610053, 10570986, 10678377, 18089238, 10213766, 10213769, 10570665, 10203475, 10613633, 10678384, 9586827, 9153877, 10678920, 10839346, 7069320, 7038134, 8745304, 4739598, 8232678, 5126746, 8334944, 10556708, 10613908, 9862734, 4762418, 4918223, 4937167, 4938141, 4887276, 4937370, 4937033, 5119551, 3151460, 2927937, 5290794, 10679051, 10453251, 10559386, 10670002, 10677382, 10677458, 10678279, 18089380, 9950684, 10570120, 10570126, 10570660, 10570662, 10570817, 10556547, 10556690, 10203957, 10667774, 10214234, 10544168, 10548176, 10203951, 12174830, 5976551, 6320379, 7304302, 9906582, 7038136, 7353954, 8891110, 7538711, 8232557, 8232810, 4763471, 4762421, 7038136, 10214234, 10544168, 10548176, 10203951, 12174830, 6320379, 5976551, 7304302, 6331330, 2256072, 2895820, 6256817, 5616864, 4887477, 4887663, 4928667, 4928668, 4908396, 4938045, 4651925, 2851007, 3912498, 4188834, 5417150, 5615994, 5852984, 5978808, 16769840, 10534246, 10556700, 10569178, 10569291, 10559119, 10559387, 10678927, 10677463, 18089239, 9881741, 10559111, 10570658, 10570661, 10570719, 10367208, 10678380, 8794898, 8968588, 10214231, 10559117, 10559118, 10570119, 10559395, 10203950, 10203952, 10203953, 10220215, 10545052]  # Replace with your actual list

    # Randomly pick a video ID and check its resolution
    random_video_id = random.choice(video_ids)
    resolution = get_video_resolution(random_video_id)

    if resolution:
        print(f"Video ID {random_video_id} has resolution: {resolution[0]}x{resolution[1]}")
    else:
        print(f"Failed to get resolution for Video ID {random_video_id}")



# if __name__ == "__main__":
#     llt = get_video_resolution()
    # print(llt)