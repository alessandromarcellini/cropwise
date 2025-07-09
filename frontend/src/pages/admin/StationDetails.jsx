import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import 'rc-switch/assets/index.css';
import axios from 'axios';

import StationState from '../../components/stations/StationState'
import StationSensors from '../../components/stations/StationSensors'
import StationInterval from '../../components/stations/StationInterval'
import UsersViewing from '../../components/stations/UsersViewing'

function StationDetails() {

    const [station, setStation] = useState(null);
    const { stationId } = useParams();
    const stationIdInt = parseInt(stationId);

    if (isNaN(stationIdInt)) {
        return (
            <div>
                <h1>Error</h1>
                <p>Invalid station ID. Please provide a valid integer.</p>
            </div>
        );
    }

    useEffect(() => {
        axios.get(`http://localhost:8000/api/station/${stationIdInt}`)
            .then(
                response => {
                    if (response.status == 200) {
                        setStation(response.data);
                    }
                    else {
                        console.log("Error fetching the station data");
                    }
                }
            )
            .catch(err => console.error('Error fetching station:', err));
    }, [stationIdInt]);

    if (!station) return <p>Loading station...</p>;

    return (
        <>
            <h1>Station Details: {station.name}</h1>
            <StationState />

            <StationSensors />

            <StationInterval />

            <UsersViewing />

            <button>View Associtaed Farmers</button>
        </>
    );
}

export default StationDetails;