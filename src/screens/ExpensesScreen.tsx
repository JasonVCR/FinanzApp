import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, TextInput, ActivityIndicator } from 'react-native';
import { useExpenses } from '../hooks/useExpenses';
import { formatCurrency, formatDate, calculatePercentage, getColorByPercentage } from '../utils/formatting';

export default function ExpensesScreen() {
  const { expenses, dailyLimit, isLoading, addExpense, saveDailyLimit, getTodayExpenses } = useExpenses();
  const [showAddForm, setShowAddForm] = useState(false);
  const [showLimitForm, setShowLimitForm] = useState(false);
  const [newExpense, setNewExpense] = useState({
    category: '',
    amount: '',
    description: '',
    isRecurring: false
  });
  const [newLimit, setNewLimit] = useState('');

  if (isLoading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#2196F3" />
      </View>
    );
  }

  const handleAddExpense = async () => {
    if (newExpense.category && newExpense.amount) {      await addExpense({
        category: newExpense.category,
        amount: parseFloat(newExpense.amount),
        description: newExpense.description
      });
      
      setShowAddForm(false);
      setNewExpense({ category: '', amount: '', description: '', isRecurring: false });
    }
  };

  const handleUpdateLimit = async () => {
    const limit = parseFloat(newLimit);
    if (!isNaN(limit) && limit > 0) {
      await saveDailyLimit(limit);
      setShowLimitForm(false);
      setNewLimit('');
    }
  };

  const todayExpenses = getTodayExpenses();
  const spentPercentage = calculatePercentage(todayExpenses, dailyLimit);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Gastos</Text>
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setShowAddForm(true)}
        >
          <Text style={styles.addButtonText}>+ Añadir Gasto</Text>
        </TouchableOpacity>
      </View>

      {/* Límite Diario */}
      <View style={styles.limitContainer}>
        <View style={styles.limitHeader}>
          <Text style={styles.limitTitle}>Límite Diario: {formatCurrency(dailyLimit)}</Text>
          <TouchableOpacity
            style={styles.limitButton}
            onPress={() => setShowLimitForm(true)}
          >
            <Text style={styles.limitButtonText}>
              {dailyLimit > 0 ? 'Cambiar' : 'Establecer'}
            </Text>
          </TouchableOpacity>
        </View>
        {dailyLimit > 0 && (
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <View 
                style={[
                  styles.progress, 
                  { 
                    width: `${Math.min(spentPercentage, 100)}%`,
                    backgroundColor: getColorByPercentage(spentPercentage)
                  }
                ]} 
              />
            </View>
            <Text style={styles.progressText}>
              {formatCurrency(todayExpenses)} / {formatCurrency(dailyLimit)}
            </Text>
          </View>
        )}
      </View>

      {showLimitForm && (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Nuevo límite diario"
            value={newLimit}
            keyboardType="numeric"
            onChangeText={setNewLimit}
          />
          <TouchableOpacity 
            style={styles.submitButton} 
            onPress={handleUpdateLimit}
          >
            <Text style={styles.submitButtonText}>Guardar Límite</Text>
          </TouchableOpacity>
        </View>
      )}

      {showAddForm && (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Categoría"
            value={newExpense.category}
            onChangeText={(text) => setNewExpense({ ...newExpense, category: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Monto"
            value={newExpense.amount}
            keyboardType="numeric"
            onChangeText={(text) => setNewExpense({ ...newExpense, amount: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Descripción (opcional)"
            value={newExpense.description}
            onChangeText={(text) => setNewExpense({ ...newExpense, description: text })}
          />
          <TouchableOpacity 
            style={[styles.checkbox, newExpense.isRecurring && styles.checkboxChecked]}
            onPress={() => setNewExpense({ ...newExpense, isRecurring: !newExpense.isRecurring })}
          >
            <Text style={styles.checkboxText}>Gasto Recurrente</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.submitButton} onPress={handleAddExpense}>
            <Text style={styles.submitButtonText}>Guardar</Text>
          </TouchableOpacity>
        </View>
      )}

      <View style={styles.expenseList}>
        {expenses.map((expense) => (
          <View key={expense.id} style={styles.expenseItem}>
            <View style={styles.expenseHeader}>
              <Text style={styles.expenseCategory}>{expense.category}</Text>
              <Text style={styles.expenseAmount}>-{formatCurrency(expense.amount)}</Text>
            </View>
            {expense.description && (
              <Text style={styles.expenseDescription}>{expense.description}</Text>
            )}
            <Text style={styles.expenseDate}>
              {formatDate(expense.date)}
            </Text>
          </View>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 16,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  addButton: {
    backgroundColor: '#2196F3',
    padding: 8,
    borderRadius: 8,
  },
  addButtonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  form: {
    backgroundColor: '#fff',
    margin: 16,
    padding: 16,
    borderRadius: 8,
    elevation: 2,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    padding: 8,
    marginBottom: 12,
  },
  checkbox: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 8,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
  },
  checkboxChecked: {
    backgroundColor: '#e3f2fd',
    borderColor: '#2196F3',
  },
  checkboxText: {
    marginLeft: 8,
    color: '#333',
  },
  submitButton: {
    backgroundColor: '#4CAF50',
    padding: 12,
    borderRadius: 4,
    alignItems: 'center',
  },
  submitButtonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  expenseList: {
    padding: 16,
  },
  expenseItem: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    elevation: 2,
  },
  expenseHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  expenseCategory: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  expenseAmount: {
    fontSize: 18,
    color: '#F44336',
    fontWeight: 'bold',
  },
  expenseDescription: {
    color: '#666',
    marginBottom: 4,
  },
  expenseDate: {
    color: '#999',
    fontSize: 12,
  },
  limitContainer: {
    backgroundColor: '#fff',
    margin: 16,
    padding: 16,
    borderRadius: 8,
    elevation: 2,
  },
  limitHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  limitTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  limitButton: {
    backgroundColor: '#2196F3',
    padding: 8,
    borderRadius: 4,
  },
  limitButtonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  progressContainer: {
    marginTop: 8,
  },
  progressBar: {
    height: 8,
    backgroundColor: '#e0e0e0',
    borderRadius: 4,
    marginBottom: 4,
  },
  progress: {
    height: '100%',
    borderRadius: 4,
  },
  progressText: {
    textAlign: 'right',
    color: '#666',
    fontSize: 12,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
