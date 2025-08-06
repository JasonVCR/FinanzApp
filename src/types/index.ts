export interface UserProfile {
  id: string;
  name: string;
  email: string;
}

export interface Asset {
  id: string;
  type: 'income' | 'credit_card' | 'bank_account';
  name: string;
  amount: number;
  description?: string;
  date?: Date;
}

export interface Expense {
  id: string;
  category: string;
  amount: number;
  date: Date;
  description?: string;
  isRecurring?: boolean;
  frequency?: 'daily' | 'weekly' | 'monthly' | 'yearly';
}

export interface Investment {
  id: string;
  type: string;
  amount: number;
  description?: string;
  returns: number;
  date?: Date;
}

export interface Budget {
  id: string;
  category: string;
  limit: number;
  spent?: number;
  period: 'daily' | 'weekly' | 'monthly';
  startDate: Date;  // Changed to required
  endDate: Date;    // Changed to required
}
