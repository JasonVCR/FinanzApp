// Common types for the application

export interface Asset {
  id: string;
  type: 'income' | 'credit_card' | 'bank_account';
  name: string;
  amount: number;
  date: Date;
  description: string;
}

export interface Expense {
  id: string;
  category: string;
  amount: number;
  description?: string;
  date: Date;
}

export interface Investment {
  id: string;
  type: string;
  amount: number;
  date: Date;
  description?: string;
  returns: number;
}

export interface Budget {
  id: string;
  category: string;
  limit: number;
  spent?: number;
  period: 'monthly' | 'annual';
}
