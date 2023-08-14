# OneLifeAPI
A drop in modern replacement of OneLifeWeb (Under construction)

Using [FastAPI](https://fastapi.tiangolo.com/)

## Plan
Initailly, this project will support a subset of the existing web servers. Version 1 will include the minimum servers for 2HOL to begin using it at that moment (reflector, tickets, lineage, photos). Later in version 1, support will be extended to additional servers as required (tokens, review, curse, fitness).

Version 2 will be a major breaking change, with the intention to remove the required `action` query parameter on all endpoints and instead use modern REST API standards.


### Version planning
#### 0.x.x
Unstable, in progress development.

#### 1.x.x
Stable, drop in replacement of OneLifeWeb/OneLife web servers

#### 2.x.x
Stable, API overhauled with modern REST API standards, large changes required to OneLife/Client/Server for compatibility

## Notable TODO
- Database schema setup handling
 - Schema update handling
 - Object handling within Python
- Project layout and hierarchy
 - Tickets
 - Reflector
 - Lineage
 - Photos
- Deployment
 - CICD Pipeline
 - Container
- ???

## Commands
```py
pipenv sync --dev
pipenv run uvicorn main:app --reload
```