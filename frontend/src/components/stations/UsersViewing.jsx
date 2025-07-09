import React from 'react';
import { Users } from 'lucide-react';

function UsersViewing() {
    return (
        <p className="flex items-center gap-2">
            <Users className="w-5 h-5 text-gray-700" style={{ marginRight: '12px', transform: 'translateY(2px)' }} />
            <span style={{ fontSize: '25px' }}>1</span>
        </p>
    );
}

export default UsersViewing;