import { useParams } from 'react-router-dom';

function RealTimeData() {
    const { stationId } = useParams();

    // Convert to integer and validate
    const stationIdInt = parseInt(stationId);

    if (isNaN(stationIdInt)) {
        return (
            <div>
                <h1>Error</h1>
                <p>Invalid station ID. Please provide a valid integer.</p>
            </div>
        );
    }

    return (
        <h1>RealTimeData of station: {stationIdInt}</h1>
    )
}

export default RealTimeData;