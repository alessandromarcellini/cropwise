import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Switch from 'rc-switch';
import 'rc-switch/assets/index.css';
import axios from 'axios';

function StationSensors() {
    const { stationId } = useParams();
    const stationIdInt = parseInt(stationId);
    const [sensors, setSensors] = useState([])
    const [checkedStates, setCheckedStates] = useState({});

    const handleSensorStateChange = (sensorId, value) => {
        //TODO call the api to set the sensor's state

        axios.post(
            `http://localhost:8000/api/station/${stationIdInt}/sensor/${sensorId}/setState`,
            {
                "new_state": value ? 'active' : 'inactive'
            }
        ).then(
            response => {
                if (response.status === 200) {
                    console.log("Toogled sensor state to " + (value ? "active" : "inactive"))
                    setCheckedStates(prev => ({ ...prev, [sensorId]: value }));
                } else {
                    console.error('Unexpected response:', response);
                }
            }
        ).catch(err => console.error('Error changing sensor state:', err));
    };

    useEffect(() => {
        axios.get(`http://localhost:8000/api/station/${stationIdInt}/sensors`)
            .then(
                response => {
                    setSensors(response.data);

                    // Initialize checkedStates based on sensor.state
                    const initialCheckedStates = {};
                    response.data.forEach(sensor => {
                        initialCheckedStates[sensor.id] = sensor.state === 'active';
                    });
                    setCheckedStates(initialCheckedStates);
                }
            )
            .catch(err => console.error('Error fetching station:', err));
    }, [stationIdInt]);

    return (
        <>
            <ul>
                {sensors?.map(sensor => (
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

export default StationSensors;