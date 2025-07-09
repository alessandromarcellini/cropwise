import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

import useLatestMetrics from '../../hooks/useLatestMetrics';


const RealTimeData = () => {
    const { stationId } = useParams();
    const [sensors, setSensors] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/station/${parseInt(stationId)}/sensors`)
            .then(response => {
                setSensors(response.data);
            })
            .catch(err => {
                console.error('Error fetching sensors:', err);
            });
    }, []);



    const { metrics, loading, error } = useLatestMetrics(parseInt(stationId), sensors.filter(sensor => sensor.state == 'active').map(sensor => sensor.sensor_type));

    let inactive_sensors = sensors.filter(sensor => sensor.state == 'inactive');

    if (loading) return <p>Loading metrics...</p>;
    if (error) return <p>Error loading metrics: {error}</p>;
    if (!metrics || metrics.length === 0) return <p>No metrics available</p>;

    return (
        <ul>
            {metrics.map((metric) => (
                <li key={metric.id}>
                    {metric.type}: {metric.value}
                    {metric.type === 'temperature' ? '°C' : '%'}
                </li>
            ))}
            {inactive_sensors.map((sensor) => (
                <li>{sensor.sensor_type}: <span style={{ color: 'red' }}>OFF</span></li>
            )
            )}
        </ul>
    );
};

export default RealTimeData;