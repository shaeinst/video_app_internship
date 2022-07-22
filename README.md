# Assignment for python internship

# Question
 Create a web application backend in any of your desired framework of python which should be having:
1. An api endpoint to receive video file
2. Add validation in length, type and size of video file
3. The video cannot exceed 10 min of length, 1GB of size and it should be either mp4 or mkv
4. Another api endpoint which can respond with a list of videos being uploaded.
5. You are free to add filters like get the video uploaded in a particular date, or size range. We leave this creativity to you.
6. Treat this application like a video storing application, so also add one another api which will take video size, length and type as input,  do validation and return charges to the user as applicable.
7. Charges : 5$ for video below 500MB and 12.5$ above 500MB. Additional 12.5$ if the video is under 6 minutes 18 second and 20$ if above.

# Project Stracture
```
./video_app_internship/
│
├── video_store/
│   ├── media/            - uploaded videos directory
│   ├── video_api/        - Video web API app
│   └── video_store/      - Video Project
│
└── venv                  - python virtual environment
```


# Installation
```bash
$ git clone https://github.com/shaeinst/video_app_internship
$ cd video_app_internship/
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


# Login

```
username: admin
password: admin
```

# API endpoints
```
/api/videos/list/     - [GET] get videos list
/api/videos/upload/   - [POST] upload video
/api/videos/cost/     - [POST] inquiry video uploading cost
```

# RESPONSES
```
this will return all uploaded video
/api/videos/list/
{
	"id": 1,
	"title": "",
	"created": "",
	"upload": ""
}


this will upload the video
/api/videos/upload/
{
	title: "video title"             - optional
	"upload": "video to be uploaded" - required
}


this will accept video type, duration and size and return cost
/api/videos/cost/
{
	"type": "mkv"   - mkv or mp4
	"size": 121     - size in MB
	"duration": 231 - duration in seconds
}

response:
{
	cost: 212
}
```

