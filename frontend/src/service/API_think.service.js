import axios from 'axios'

const apiUrl = 'http://127.0.0.1:5000/';

export const apiService = {
    get: async (endpoint) => {
      try {
        const response = await axios.get(apiUrl + endpoint);
        return response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
      }
    },
  };
  
