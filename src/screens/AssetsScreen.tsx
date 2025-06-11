import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, TextInput } from 'react-native';
import { Asset } from '../types';

interface NewAsset {
  type: 'income' | 'credit_card' | 'bank_account';
  name: string;
  amount: string;
  description: string;
}

export default function AssetsScreen() {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [showAddForm, setShowAddForm] = useState(false);
  const [newAsset, setNewAsset] = useState<NewAsset>({
    type: 'income',
    name: '',
    amount: '',
    description: ''
  });

  const addAsset = () => {
    if (!newAsset.name || !newAsset.amount) {
      return;
    }
    const amount = parseFloat(newAsset.amount);
    if (isNaN(amount)) {
      return;
    }
    
    const asset: Asset = {
      id: Date.now().toString(),
      type: newAsset.type,
      name: newAsset.name,
      amount: amount,
      date: new Date(), // Aseguramos que la fecha es una instancia válida de Date
      description: newAsset.description || '' // Aseguramos que description nunca es undefined
    };

    setAssets([...assets, asset]);
    setShowAddForm(false);
    setNewAsset({ type: 'income', name: '', amount: '', description: '' });
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Activos</Text>
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setShowAddForm(true)}
        >
          <Text style={styles.addButtonText}>+ Añadir Activo</Text>
        </TouchableOpacity>
      </View>

      {showAddForm && (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Nombre del activo"
            value={newAsset.name}
            onChangeText={(text) => setNewAsset({ ...newAsset, name: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Monto"
            value={newAsset.amount}
            keyboardType="numeric"
            onChangeText={(text) => setNewAsset({ ...newAsset, amount: text })}
          />
          <TextInput
            style={styles.input}
            placeholder="Descripción (opcional)"
            value={newAsset.description}
            onChangeText={(text) => setNewAsset({ ...newAsset, description: text })}
          />
          <TouchableOpacity style={styles.submitButton} onPress={addAsset}>
            <Text style={styles.submitButtonText}>Guardar</Text>
          </TouchableOpacity>
        </View>
      )}

      <View style={styles.assetList}>
        {assets.map((asset) => (
          <View key={asset.id} style={styles.assetItem}>
            <Text style={styles.assetName}>{asset.name}</Text>
            <Text style={styles.assetAmount}>${asset.amount.toFixed(2)}</Text>
            {asset.description && (
              <Text style={styles.assetDescription}>{asset.description}</Text>
            )}
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
  assetList: {
    padding: 16,
  },
  assetItem: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
    elevation: 2,
  },
  assetName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  assetAmount: {
    fontSize: 24,
    color: '#2196F3',
    marginTop: 4,
  },
  assetDescription: {
    color: '#666',
    marginTop: 4,
  },
});
