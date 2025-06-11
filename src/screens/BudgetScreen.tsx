import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, TextInput } from 'react-native';
import { Budget } from '../types';
import { ProgressChart } from 'react-native-chart-kit';

export default function BudgetScreen() {
  const [budgets, setBudgets] = useState<Budget[]>([]);
  const [showAddForm, setShowAddForm] = useState(false);
  const [newBudget, setNewBudget] = useState({
    category: '',
    limit: '',
    period: 'monthly' as const
  });

  const addBudget = () => {
    if (newBudget.category && newBudget.limit) {      const now = new Date();
      const monthEnd = new Date(now.getFullYear(), now.getMonth() + 1, 0);
      const budget: Budget = {
        id: Date.now().toString(),
        category: newBudget.category,
        limit: parseFloat(newBudget.limit),
        spent: 0,
        period: newBudget.period,
        startDate: now,
        endDate: monthEnd
      };

      setBudgets([...budgets, budget]);
      setShowAddForm(false);
      setNewBudget({ category: '', limit: '', period: 'monthly' });
    }
  };

  // Datos de ejemplo para el gráfico circular de progreso
  const progressData = {
    data: [0.4, 0.6, 0.8]
  };

  const chartConfig = {
    backgroundColor: '#ffffff',
    backgroundGradientFrom: '#ffffff',
    backgroundGradientTo: '#ffffff',
    color: (opacity = 1) => `rgba(33, 150, 243, ${opacity})`,
    style: {
      borderRadius: 16
    }
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Presupuesto</Text>
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setShowAddForm(true)}
        >
          <Text style={styles.addButtonText}>+ Añadir Presupuesto</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.chartContainer}>
        <Text style={styles.subtitle}>Progreso del Presupuesto</Text>
        <ProgressChart
          data={progressData}
          width={350}
          height={220}
          chartConfig={chartConfig}
          hideLegend={false}
        />
      </View>

      {showAddForm && (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Categoría"
            value={newBudget.category}
            onChangeText={(text) => setNewBudget({ ...newBudget, category: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Límite"
            value={newBudget.limit}
            keyboardType="numeric"
            onChangeText={(text) => setNewBudget({ ...newBudget, limit: text })}
          />
          <TouchableOpacity style={styles.submitButton} onPress={addBudget}>
            <Text style={styles.submitButtonText}>Guardar</Text>
          </TouchableOpacity>
        </View>
      )}

      <View style={styles.budgetList}>
        {budgets.map((budget) => (
          <View key={budget.id} style={styles.budgetItem}>
            <View style={styles.budgetHeader}>
              <Text style={styles.budgetCategory}>{budget.category}</Text>
              <Text style={styles.budgetAmount}>
                ${budget.spent?.toFixed(2) || '0.00'} / ${budget.limit.toFixed(2)}
              </Text>
            </View>
            <View style={styles.progressBar}>
              <View 
                style={[
                  styles.progress, 
                  { width: `${((budget.spent || 0) / budget.limit) * 100}%` }
                ]} 
              />
            </View>
            <Text style={styles.budgetPeriod}>
              {budget.startDate.toLocaleDateString()} - {budget.endDate.toLocaleDateString()}
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
  subtitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 16,
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
  chartContainer: {
    padding: 16,
    backgroundColor: '#fff',
    margin: 16,
    borderRadius: 8,
    elevation: 2,
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
  budgetList: {
    padding: 16,
  },
  budgetItem: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    elevation: 2,
  },
  budgetHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  budgetCategory: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  budgetAmount: {
    fontSize: 16,
    color: '#2196F3',
  },
  progressBar: {
    height: 8,
    backgroundColor: '#e0e0e0',
    borderRadius: 4,
    marginBottom: 8,
  },
  progress: {
    height: '100%',
    backgroundColor: '#2196F3',
    borderRadius: 4,
  },
  budgetPeriod: {
    color: '#999',
    fontSize: 12,
  },
});
