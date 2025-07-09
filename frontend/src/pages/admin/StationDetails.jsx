import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Switch from 'rc-switch';
import 'rc-switch/assets/index.css';
import axios from 'axios';

import StationState from '../../components/stations/StationState'

function StationDetails() {
    const [checkedStates, setCheckedStates] = useState({});
    const [station, setStation] = useState(null);
    const { stationId } = useParams();
    const stationIdInt = parseInt(stationId);

    const handleSensorStateChange = (sensorId, value) => {
        //TODO call the api to set the sensor's state
        setCheckedStates(prev => ({ ...prev, [sensorId]: value }));
        console.log(`Sensor ${sensorId} is now:`, value);
    };

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
                    setStation(response.data);
                }
            )
            .catch(err => console.error('Error fetching station:', err));
    }, [stationIdInt]);

    if (!station) return <p>Loading station...</p>;

    return (
        <>
            <h1>Station Details: {station.name}</h1>
            <StationState />

            <ul>
                {station.sensors?.map(sensor => (
                    <li key={sensor.id} style={{ marginBottom: '12px' }}>
                        <span style={{ marginRight: '12px' }}>{sensor.sensor_type}</span>
                        <Switch
                            checked={!!checkedStates[sensor.id]}
                            onChange={value => handleSensorStateChange(sensor.id, value)}
                        />
                    </li>
                ))}
            </ul>
        </>
    );
}

export default StationDetails;