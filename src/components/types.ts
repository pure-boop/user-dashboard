// types.ts
import { User } from './user.entity';
import { Dashboard } from './dashboard.entity';
import { Settings } from './settings.entity';

export interface IRes {
  statusCode: number;
  message?: string;
  data?: any;
}

export interface IReqBody {
  username: string;
  email: string;
  password: string;
}

export interface IReqParams {
  userId: string;
}

export interface IReqQuery {
  limit?: number;
  offset?: number;
  sort?: string;
}

export type UserCreateDTO = Omit<User, 'id'>;
export type UserUpdateDTO = Omit<User, 'id'> & Partial<User>;

export type DashboardCreateDTO = Omit<Dashboard, 'id'>;
export type DashboardUpdateDTO = Omit<Dashboard, 'id'> & Partial<Dashboard>;

export type SettingsCreateDTO = Omit<Settings, 'id'>;
export type SettingsUpdateDTO = Omit<Settings, 'id'> & Partial<Settings>;

export class UserDashboardTypes {}