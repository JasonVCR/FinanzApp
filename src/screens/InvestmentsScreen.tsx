import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, TextInput } from 'react-native';
import { Investment } from '../types';
import { LineChart } from 'react-native-chart-kit';

export default function InvestmentsScreen() {
  const [investments, setInvestments] = useState<Investment[]>([]);
  const [showAddForm, setShowAddForm] = useState(false);
  const [newInvestment, setNewInvestment] = useState({
    type: '',
    amount: '',
    description: '',
    returns: ''
  });

  const addInvestment = () => {
    if (newInvestment.type && newInvestment.amount) {
      const investment: Investment = {
        id: Date.now().toString(),
        type: newInvestment.type,
        amount: parseFloat(newInvestment.amount),
        date: new Date(),
        description: newInvestment.description || '',
        returns: parseFloat(newInvestment.returns || '0')
      };

      setInvestments([...investments, investment]);
      setShowAddForm(false);
      setNewInvestment({ type: '', amount: '', description: '', returns: '' });
    }
  };

  // Datos de ejemplo para el gráfico
  const chartData = {
    labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
    datasets: [{
      data: [
        10000,
        10500,
        11200,
        10800,
        11500,
        12000
      ]
    }]
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
        <Text style={styles.title}>Inversiones</Text>
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setShowAddForm(true)}
        >
          <Text style={styles.addButtonText}>+ Añadir Inversión</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.chartContainer}>
        <Text style={styles.subtitle}>Rendimiento de Inversiones</Text>
        <LineChart
          data={chartData}
          width={350}
          height={220}
          chartConfig={chartConfig}
          bezier
          style={styles.chart}
        />
      </View>

      {showAddForm && (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Tipo de inversión"
            value={newInvestment.type}
            onChangeText={(text) => setNewInvestment({ ...newInvestment, type: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Monto"
            value={newInvestment.amount}
            keyboardType="numeric"
            onChangeText={(text) => setNewInvestment({ ...newInvestment, amount: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Rendimiento esperado (%)"
            value={newInvestment.returns}
            keyboardType="numeric"
            onChangeText={(text) => setNewInvestment({ ...newInvestment, returns: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Descripción (opcional)"
            value={newInvestment.description}
            onChangeText={(text) => setNewInvestment({ ...newInvestment, description: text })}
          />
          <TouchableOpacity style={styles.submitButton} onPress={addInvestment}>
            <Text style={styles.submitButtonText}>Guardar</Text>
          </TouchableOpacity>
        </View>
      )}

      <View style={styles.investmentList}>
        {investments.map((investment) => (
          <View key={investment.id} style={styles.investmentItem}>
            <View style={styles.investmentHeader}>
              <Text style={styles.investmentType}>{investment.type}</Text>
              <Text style={styles.investmentAmount}>${investment.amount.toFixed(2)}</Text>
            </View>
            {investment.returns && (
              <Text style={styles.investmentReturns}>
                Rendimiento: {investment.returns}%
              </Text>
            )}
            {investment.description && (
              <Text style={styles.investmentDescription}>{investment.description}</Text>
            )}
            <Text style={styles.investmentDate}>
              {new Date(investment.date).toLocaleDateString('es-ES')}
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
  chart: {
    marginVertical: 8,
    borderRadius: 16,
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
  investmentList: {
    padding: 16,
  },
  investmentItem: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    elevation: 2,
  },
  investmentHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  investmentType: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  investmentAmount: {
    fontSize: 18,
    color: '#4CAF50',
    fontWeight: 'bold',
  },
  investmentReturns: {
    color: '#2196F3',
    fontWeight: 'bold',
    marginBottom: 4,
  },
  investmentDescription: {
    color: '#666',
    marginBottom: 4,
  },
  investmentDate: {
    color: '#999',
    fontSize: 12,
  },
});
