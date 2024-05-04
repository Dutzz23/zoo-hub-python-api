from fastapi import  APIRouter


def generate_router_description(router: APIRouter) -> dict:
    router_details = {
        "router_path": router.prefix,
        "tags": router.tags,
        "deprecated": router.deprecated,
        "responses": router.responses,
        "dependencies": router.dependencies,
        "routes": [{"route": route.path,
                    "summary": route.summary,
                    "description": route.description,
                    "methods": route.methods,
                    "dependencies": route.dependencies,
                    "responses": [response for response in route.responses]
                    } for route in router.routes],
        # Add more attributes as needed
    }
    return router_details
