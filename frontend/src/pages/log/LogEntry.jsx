import { useParams } from 'react-router-dom';

function LogEntry() {
    const { entryId } = useParams();

    // Convert to integer and validate
    const entryIdInt = parseInt(entryId);

    if (isNaN(entryIdInt)) {
        return (
            <div>
                <h1>Error</h1>
                <p>Invalid station ID. Please provide a valid integer.</p>
            </div>
        );
    }

    return (
        <h1>LogEntry {entryIdInt}</h1>
    )
}

export default LogEntry;