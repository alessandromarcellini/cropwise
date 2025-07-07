from fastapi import APIRouter, Request


router = APIRouter(
	prefix="/api/station",
	tags=["Station"],
)

@router.get("/{station_id}/")
async def root(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.get("/{station_id}/currentState")
async def get_current_state(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.get("/{station_id}/currentInterval")
async def get_current_interval(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.get("/{station_id}/sensors")
async def get_sensors(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.get("/{station_id}/basicData")
async def get_basic_data(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}


@router.get("/{station_id}/numberOfViewingUsers")
async def get_number_of_viewing_users(station_id: int, request: Request):
    return {"message": "This will not be implemented right away (probably never)"}

@router.get("/{station_id}/associatedFarmers")
async def get_associated_farmers(station_id: int, request: Request):
    return {"message": "Associated farmers"}
# POST ----------------------------------

@router.post("/{station_id}/setInterval")
async def set_interval(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.post("/{station_id}/setInterval")
async def set_interval(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.post("/{station_id}/setInterval")
async def set_interval(station_id: int, request: Request):
    return {"message": "Station!", "station_id": station_id}

@router.post("/{station_id}/setState")
async def set_state(station_id: int, request: Request):
    return {
        "message": "Set state!",
        "station_id": station_id,
    }

@router.post("/{station_id}/sensor/{sensor_id}/setState")
async def set_sensor_state(station_id: int, sensor_id: int, request: Request):
    return {
        "message": "Set sensor state!",
        "station_id": station_id,
        "sensor_id": sensor_id
    }
