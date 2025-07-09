import { collection, getDocs, where, query } from "firebase/firestore";
import db from "../firebase/config"




export const get_last_metrics = (station_id) => {
    const metricsRef = collection(db, "metrics");

    const q = query(metricsRef, where("station_id", "==", station_id));

    return getDocs(q);
}