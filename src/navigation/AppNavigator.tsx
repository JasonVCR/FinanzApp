import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

// Definición de tipos para el navegador
export type RootStackParamList = {
  Home: undefined;
  Assets: undefined;
  Expenses: undefined;
  Investments: undefined;
  Budget: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();

// Importación de pantallas
import HomeScreen from '../screens/HomeScreen';
import AssetsScreen from '../screens/AssetsScreen';
import ExpensesScreen from '../screens/ExpensesScreen';
import InvestmentsScreen from '../screens/InvestmentsScreen';
import BudgetScreen from '../screens/BudgetScreen';

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Home"
        screenOptions={{
          headerStyle: {
            backgroundColor: '#2196F3',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      >
        <Stack.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ title: 'Dashboard' }}
        />
        <Stack.Screen 
          name="Assets" 
          component={AssetsScreen} 
          options={{ title: 'Activos' }}
        />
        <Stack.Screen 
          name="Expenses" 
          component={ExpensesScreen} 
          options={{ title: 'Gastos' }}
        />
        <Stack.Screen 
          name="Investments" 
          component={InvestmentsScreen} 
          options={{ title: 'Inversiones' }}
        />
        <Stack.Screen 
          name="Budget" 
          component={BudgetScreen} 
          options={{ title: 'Presupuesto' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
