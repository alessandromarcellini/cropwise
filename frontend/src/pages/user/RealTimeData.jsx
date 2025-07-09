import React from 'react';
import { useParams } from 'react-router-dom';

import useLatestMetrics from '../../hooks/useLatestMetrics';


const RealTimeData = () => {
    const { stationId } = useParams();
    //TODO fetch from the backend the sensor types that the station has. Add them into the list passed to useLatestMetrics

    const { metrics, loading, error } = useLatestMetrics(parseInt(stationId), ['temperature', 'air_humidity', 'precipitation']);

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
        </ul>
    );
};

export default RealTimeData;