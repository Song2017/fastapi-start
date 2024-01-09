# fastapi-start
A lightweight, flexible API template based on FastAPI + OpenAPI + Redis + PostgresSQL.

## Guideline
1. modify project yaml(/server/data/demo.yaml)
2. generate swagger code(bin/gen_swagger_server.sh)
3. modify apis(/server/api and fastapi_server.py)
4. run fastapi server(bin/run_http_server.sh)
5. access swagger ui(http://localhost:9000/api/docs)

## Docker
1. build image
`docker build -f deploy/Dockerfile -t test .`
2. run container
`docker run -it -p 9000:9000 -e APP_SETTINGS=eyJBUFBfQ09ORiI6eyJBUFBfTkFNRSI6IkRlbW8iLCJBUFBfVElNRU9VVCI6IjUiLCJBUFBfTU9ERSI6ImRlYnVnIiwiUE9SVCI6OTAwMCwiVE9LRU4iOiJ0ZXN0In0sIlJFRElTX0NPTkYiOnsiREIiOiI1IiwiUkVESVNfSE9TVCI6InItaC5yZWRpcy5yZHMuYWxpeXVuY3MuY29tOjYzNzkiLCJSRURJU19QQVNTIjoicGFzcyEifSwiUEdfQ09ORiI6eyJQR19VUkkiOiJwb3N0Z3Jlc3FsOi8vdTp0ZXN0c0BwZ20tdGVzdHMucGcucmRzLmFsaXl1bmNzLmNvbS9kYiIsIk5BTUUiOiJ0ZXN0In19Cg== test`

## Project Layout
```text
├── bin                             execute shell
│  ├── gen_swagger_server.sh        generate swagger server    
│  └── run_http_server.sh           run fastapi server
├── core                            core libs which can be shared
├── server                          project files, adjusting for new projects
│  ├── api                          new project apis, referring to swagger code
│  └── fastapi_server.py            main file   
├── swagger_server                  generated swagger code
├── tests                 
├── web                             web files                 
└── core                            core libs which can be shared
```