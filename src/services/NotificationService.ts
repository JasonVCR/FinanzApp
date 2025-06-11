import * as Notifications from 'expo-notifications';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
    shouldShowBanner: true,
    shouldShowList: true,
  }),
});

export const NotificationService = {  requestPermissions: async () => {
    const permission = await Notifications.requestPermissionsAsync();
    return permission.status === 'granted';
  },

  scheduleExpenseAlert: async (spent: number, limit: number, isWarning: boolean) => {
    const percentage = (spent / limit) * 100;
    const title = isWarning ? 'Alerta de Gastos - 80%' : 'Límite de Gastos Alcanzado';
    const body = isWarning 
      ? `Has alcanzado el ${percentage.toFixed(0)}% de tu límite diario de gastos.`
      : 'Has alcanzado el límite de gastos diario establecido.';

    await Notifications.scheduleNotificationAsync({
      content: {
        title,
        body,
        sound: true,
        priority: Notifications.AndroidNotificationPriority.HIGH,
        data: { spent, limit },
      },
      trigger: null, // Inmediato
    });
  },

  checkExpenseLimit: (spent: number, limit: number) => {
    const percentage = (spent / limit) * 100;
    
    if (percentage >= 100) {
      NotificationService.scheduleExpenseAlert(spent, limit, false);
    } else if (percentage >= 80 && percentage < 100) {
      NotificationService.scheduleExpenseAlert(spent, limit, true);
    }
  },
};
