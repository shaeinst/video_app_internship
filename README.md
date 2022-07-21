# Assignment for python internship


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

