import React, { useState, useEffect } from 'react';
import { View, Text, Image, FlatList, TouchableOpacity } from 'react-native';
import axios from 'axios';

const ProductFeed = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/products')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <FlatList
      data={products}
      keyExtractor={item => item._id}
      renderItem={({ item }) => (
        <TouchableOpacity>
          <Image source={{ uri: item.images[0] }} style={{ width: 100, height: 100 }} />
          <Text>{item.title}</Text>
          <Text>${item.price}</Text>
        </TouchableOpacity>
      )}
    />
  );
};

export default ProductFeed;


