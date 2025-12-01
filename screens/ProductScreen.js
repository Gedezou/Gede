import React from 'react';
import { View, Text, Image, Button } from 'react-native';

const ProductScreen = ({ route }) => {
    const { product } = route.params;

    const addToCart = () => {
        // Add to cart functionality
        alert('Added to cart!');
    };

    return (
        <View style={{ padding: 20 }}>
            <Image source={{ uri: product.image }} style={{ width: '100%', height: 300 }} />
            <Text style={{ fontSize: 24, fontWeight: 'bold' }}>{product.name}</Text>
            <Text style={{ marginVertical: 10 }}>${product.price}</Text>
            <Text>{product.description}</Text>
            <Button title="Add to Cart" onPress={addToCart} />
        </View>
    );
};

export default ProductScreen;
