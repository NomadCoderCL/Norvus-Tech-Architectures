/**
 * API v1 Contract Definitions for Agrotour Platform.
 * 
 * Shared across Backend (Django), Web (React), and Mobile (React Native) 
 * to ensure type safety and consistent data models.
 */

export interface UserProfile {
  id: string;
  username: string;
  activeRole: 'ADMIN' | 'OPERATOR' | 'TOURIST';
  lastSeen?: string;
}

export interface AgroActivity {
  uuid: string;
  type: 'HARVEST' | 'MAINTENANCE' | 'TOUR';
  status: 'PENDING' | 'IN_PROGRESS' | 'COMPLETED';
  timestamp: string;
  location: {
    lat: number;
    lng: number;
  };
  metadata: Record<string, any>;
}

export interface SyncPayload {
  deviceId: string;
  operations: AgroActivity[];
  checksum: string;
}

export type ApiResponse<T> = {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
  };
};

/**
 * Endpoint structure for the Sync Service.
 */
export const ENDPOINTS = {
  SYNC: '/v1/sync/push',
  FETCH_ACTIVITIES: '/v1/activities/list',
  PROFILE_UPDATE: '/v1/profile/edit',
} as const;
