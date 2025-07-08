import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import NotFound from './pages/NotFound';

// Registration Views
import BasicRegistration from './pages/registration/BasicRegistration';
import FarmerRegistration from './pages/registration/FarmerRegistration';

// Authentication
import Login from './pages/auth/Login';

// User Views
import SearchStation from './pages/user/SearchStation';
import RealTimeData from './pages/user/RealTimeData';
import HistoricalData from './pages/user/HistoricalData';

// Admin Views
import AdminHome from './pages/admin/Home';
import StationList from './pages/admin/StationList';
import StationDetails from './pages/admin/StationDetails';

// Log Views
import LogHome from './pages/log/LogHome';
import LogEntry from './pages/log/LogEntry';
import LogAnomalies from './pages/log/LogAnomalies';


function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <main style={{ padding: '2rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />

            {/* Registration routes */}
            <Route path="/register/" element={<BasicRegistration />} />
            <Route path="/register/farmer" element={<FarmerRegistration />} />

            {/* Authentication */}
            <Route path="/login" element={<Login />} />

            {/* User routes */}
            <Route path="/search-station" element={<SearchStation />} />
            <Route path="/real-time-data/:stationId" element={<RealTimeData />} />
            <Route path="/historical-data/:stationId" element={<HistoricalData />} />

            {/* Admin routes */}
            <Route path="/admin" element={<AdminHome />} />
            <Route path="/admin/stations" element={<StationList />} />
            <Route path="/admin/station/:stationId" element={<StationDetails />} />

            {/* Log routes */}
            <Route path="/logs" element={<LogHome />} />
            <Route path="/logs/entry/:entryId" element={<LogEntry />} />
            <Route path="/logs/anomalies" element={<LogAnomalies />} />

            {/* Catch-all route for 404 - must be last */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;