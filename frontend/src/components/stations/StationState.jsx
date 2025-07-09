import React, { useState, useEffect } from 'react';
import Switch from 'rc-switch';
import 'rc-switch/assets/index.css';
import axios from 'axios';

import { useParams } from 'react-router-dom';


function StationState() {
    const [stationState, setStationState] = useState(true);

    const { stationId } = useParams();
    const stationIdInt = parseInt(stationId);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/station/${stationIdInt}/currentState`)
            .then(
                response => {
                    setStationState(response.data);
                }
            )
            .catch(err => console.error('Error fetching station:', err));
    });

    const handleStationStateChange = (value) => {
        axios.post(
            `http://localhost:8000/api/station/${stationIdInt}/setState`,
            {
                "new_state": value ? 'active' : 'inactive'
            }
        ).then(
            response => {
                if (response.status === 200) {
                    console.log("Toogled station state to " + value ? "active" : "inactive")
                    setStationState(value);
                } else {
                    console.error('Unexpected response:', response);
                }
            }
        ).catch(err => console.error('Error changing station state:', err));
    };


    return (
        <>
            <h3>Station state: </h3>
            <Switch
                checked={stationState}
                onChange={handleStationStateChange}
            />
        </>
    );
}

export default StationState;