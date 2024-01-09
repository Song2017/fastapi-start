# fastapi-start
A lightweight, flexible API template based on FastAPI + OpenAPI + Redis + PostgresSQL.

## Guideline
1. modify project yaml(/server/data/demo.yaml)
2. generate swagger code(bin/gen_swagger_server.sh)
3. modify apis(/server/api and fastapi_server.py)
4. run fastapi server(bin/run_http_server.sh)
5. access swagger ui(http://localhost:9000/api/docs)

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