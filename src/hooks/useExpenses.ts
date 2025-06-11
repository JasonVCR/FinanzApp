import { useState, useEffect } from 'react';
import { Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Expense } from '../types';
import { NotificationService } from '../services/NotificationService';

const EXPENSES_STORAGE_KEY = '@finanzapp:expenses';
const DAILY_LIMIT_STORAGE_KEY = '@finanzapp:dailyLimit';

export const useExpenses = () => {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [dailyLimit, setDailyLimit] = useState(0);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [storedExpenses, storedLimit] = await Promise.all([
        AsyncStorage.getItem(EXPENSES_STORAGE_KEY),
        AsyncStorage.getItem(DAILY_LIMIT_STORAGE_KEY)
      ]);

      if (storedExpenses) {
        setExpenses(JSON.parse(storedExpenses));
      }
      
      if (storedLimit) {
        setDailyLimit(parseFloat(storedLimit));
      }
    } catch (error) {
      Alert.alert('Error', 'No se pudieron cargar los datos');
    } finally {
      setIsLoading(false);
    }
  };

  const saveExpenses = async (newExpenses: Expense[]) => {
    try {
      await AsyncStorage.setItem(EXPENSES_STORAGE_KEY, JSON.stringify(newExpenses));
      setExpenses(newExpenses);
    } catch (error) {
      Alert.alert('Error', 'No se pudieron guardar los gastos');
    }
  };

  const saveDailyLimit = async (limit: number) => {
    try {
      await AsyncStorage.setItem(DAILY_LIMIT_STORAGE_KEY, limit.toString());
      setDailyLimit(limit);
    } catch (error) {
      Alert.alert('Error', 'No se pudo guardar el límite diario');
    }
  };
  const addExpense = async (expense: Omit<Expense, 'id' | 'date' | 'isRecurring' | 'frequency'>) => {
    const newExpense: Expense = {
      ...expense,
      id: Date.now().toString(),
      date: new Date(),
      isRecurring: false,
      frequency: undefined
    };

    const newExpenses = [...expenses, newExpense];
    await saveExpenses(newExpenses);

    // Verificar límites y enviar notificaciones
    const todayExpenses = getTodayExpenses(newExpenses);
    if (dailyLimit > 0) {
      NotificationService.checkExpenseLimit(todayExpenses, dailyLimit);
    }

    return newExpense;
  };

  const getTodayExpenses = (expensesList = expenses) => {
    const today = new Date();
    return expensesList
      .filter(expense => {
        const expenseDate = new Date(expense.date);
        return expenseDate.toDateString() === today.toDateString();
      })
      .reduce((sum, expense) => sum + expense.amount, 0);
  };

  return {
    expenses,
    dailyLimit,
    isLoading,
    addExpense,
    saveDailyLimit,
    getTodayExpenses
  };
};
