export const formatCurrency = (amount: number): string => {
  return new Intl.NumberFormat('es-ES', {
    style: 'currency',
    currency: 'EUR'
  }).format(amount);
};

export const formatDate = (date: Date): string => {
  return new Intl.DateTimeFormat('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date);
};

export const calculatePercentage = (current: number, total: number): number => {
  if (total === 0) return 0;
  return (current / total) * 100;
};

export const getColorByPercentage = (percentage: number): string => {
  if (percentage >= 100) return '#F44336'; // Rojo
  if (percentage >= 80) return '#FFC107';  // Amarillo
  return '#4CAF50';                        // Verde
};

export const formatPercentage = (percentage: number): string => {
  return `${Math.min(Math.round(percentage), 100)}%`;
};
