import { useState, useEffect } from 'react';
import { collection, query, where, orderBy, limit, onSnapshot } from 'firebase/firestore';
import db from '../firebase/config';

const useLatestMetrics = (stationId, types) => {
    const [metrics, setMetrics] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (!stationId || !types || types.length === 0) {
            setMetrics([]);
            setLoading(false);
            return;
        }

        setLoading(true);
        setError(null);

        const unsubscribes = [];
        const metricsMap = new Map();

        // Create a separate query for each type
        types.forEach(type => {
            const metricsQuery = query(
                collection(db, 'metrics'),
                where('station_id', '==', stationId),
                where('type', '==', type),
                orderBy('timestamp', 'desc'),
                limit(1)
            );

            // Set up real-time listener for each type
            const unsubscribe = onSnapshot(
                metricsQuery,
                (snapshot) => {
                    if (!snapshot.empty) {
                        const latestDoc = snapshot.docs[0];
                        const metricData = {
                            id: latestDoc.id,
                            ...latestDoc.data()
                        };
                        metricsMap.set(type, metricData);
                    } else {
                        metricsMap.delete(type);
                    }

                    // Update state with all metrics
                    setMetrics(Array.from(metricsMap.values()));
                    setLoading(false);
                },
                (err) => {
                    console.error(`Error listening to ${type} metrics:`, err);
                    setError(err.message);
                    setLoading(false);
                }
            );

            unsubscribes.push(unsubscribe);
        });

        // Cleanup all listeners on unmount or dependency change
        return () => {
            unsubscribes.forEach(unsubscribe => unsubscribe());
        };
    }, [stationId, JSON.stringify(types)]);

    return { metrics, loading, error };
};

export default useLatestMetrics;