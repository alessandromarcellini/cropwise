import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function StationInterval() {
    const [interval, setInterval] = useState(null);
    const [displayInterval, setDisplayInterval] = useState(null);
    const { stationId } = useParams();
    const stationIdInt = parseInt(stationId);

    const debounceTimer = useRef(null);
    const isHolding = useRef(false);
    const holdInterval = useRef(null);
    const lastChangeTime = useRef(0);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/station/${stationIdInt}/currentInterval`)
            .then(
                response => {
                    if (response.status == 200) {
                        setInterval(response.data);
                        setDisplayInterval(response.data);
                    }
                    else {
                        console.log("Error fetching the current interval");
                    }
                }
            )
            .catch(err => console.error('Error fetching current interval:', err));
    }, []);

    const sendToBackend = useCallback(async (newInterval) => {
        try {
            await axios.post(`http://localhost:8000/api/station/${stationId}/setInterval`,
                {
                    "value": newInterval
                }
            );
            console.log("Fine");
            setInterval(newInterval);
        } catch (error) {
            console.error('Error updating interval:', error);
        }
    }, [stationId]);

    const handleIntervalChange = useCallback((newValue) => {
        const clampedValue = Math.max(500, Math.min(5000, newValue));
        setDisplayInterval(clampedValue);
        lastChangeTime.current = Date.now();

        // Clear existing debounce timer
        if (debounceTimer.current) {
            clearTimeout(debounceTimer.current);
        }

        // Set new debounce timer
        debounceTimer.current = setTimeout(() => {
            const timeSinceLastChange = Date.now() - lastChangeTime.current;
            if (timeSinceLastChange >= 2000) {
                sendToBackend(clampedValue);
            }
        }, 2000);
    }, [sendToBackend]);

    const startHolding = useCallback((direction) => {
        if (isHolding.current) return;

        isHolding.current = true;
        lastChangeTime.current = Date.now();

        const step = direction === 'up' ? 100 : -100;

        // Immediate first change
        handleIntervalChange((displayInterval || interval) + step);

        // Continue changing while holding
        holdInterval.current = setInterval(() => {
            setDisplayInterval(prev => {
                const newValue = prev + step;
                const clampedValue = Math.max(500, Math.min(5000, newValue));

                if (clampedValue !== prev) {
                    lastChangeTime.current = Date.now();

                    // Clear existing debounce timer
                    if (debounceTimer.current) {
                        clearTimeout(debounceTimer.current);
                    }

                    // Set new debounce timer
                    debounceTimer.current = setTimeout(() => {
                        const timeSinceLastChange = Date.now() - lastChangeTime.current;
                        if (timeSinceLastChange >= 2000) {
                            sendToBackend(clampedValue);
                        }
                    }, 2000);
                }

                return clampedValue;
            });
        }, 150);
    }, [displayInterval, handleIntervalChange, sendToBackend]);

    const stopHolding = useCallback(() => {
        if (!isHolding.current) return;

        isHolding.current = false;

        if (holdInterval.current) {
            clearInterval(holdInterval.current);
            holdInterval.current = null;
        }

        // Check if we need to send to backend immediately
        const timeSinceLastChange = Date.now() - lastChangeTime.current;
        if (timeSinceLastChange >= 2000) {
            if (debounceTimer.current) {
                clearTimeout(debounceTimer.current);
            }
            sendToBackend(displayInterval);
        }
    }, [displayInterval, sendToBackend]);

    // Cleanup on unmount
    useEffect(() => {
        return () => {
            if (debounceTimer.current) {
                clearTimeout(debounceTimer.current);
            }
            if (holdInterval.current) {
                clearInterval(holdInterval.current);
            }
        };
    }, []);

    if (!interval && !displayInterval) return <p>Loading Interval...</p>

    return (
        <div className="flex flex-col items-center space-y-4 p-4">
            <button
                onMouseDown={() => startHolding('up')}
                onMouseUp={stopHolding}
                onMouseLeave={stopHolding}
                onTouchStart={() => startHolding('up')}
                onTouchEnd={stopHolding}
                disabled={displayInterval >= 5000 || (displayInterval || interval) >= 5000}
                className="p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors text-xl font-bold"
            >
                ▲
            </button>

            <div className="text-center">
                <p className="text-lg font-semibold">Interval: {displayInterval || interval} ms</p>
                <p className="text-sm text-gray-600">Min: 500ms | Max: 5000ms</p>
            </div>

            <button
                onMouseDown={() => startHolding('down')}
                onMouseUp={stopHolding}
                onMouseLeave={stopHolding}
                onTouchStart={() => startHolding('down')}
                onTouchEnd={stopHolding}
                disabled={displayInterval <= 500 || (displayInterval || interval) <= 500}
                className="p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors text-xl font-bold"
            >
                ▼
            </button>
        </div>
    );
}

export default StationInterval;