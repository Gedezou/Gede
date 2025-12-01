import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Image, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { ScollView, SafeAreaView } from 'react-native-safe-area-context';
import  { Stack, userRouter } from 'expo-router';
import { COLORS, icons, images, SIZES } from '../constants';


const HomeScreen = ({ navigation }) => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/products')
            .then(response => setProducts(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <View>
            <Text style={{ fontSize: 24, fontWeight: 'bold', margin: 10 }}>BeautyDrop</Text>
            <FlatList
                data={products}
                keyExtractor={(item) => item._id}
                renderItem={({ item }) => (
                    <TouchableOpacity onPress={() => navigation.navigate('Product', { product: item })}>
                        <View style={{ margin: 10, flexDirection: 'row', alignItems: 'center' }}>
                            <Image source={{ uri: item.image }} style={{ width: 100, height: 100 }} />
                            <Text style={{ marginLeft: 10 }}>{item.name} - ${item.price}</Text>
                        </View>
                    </TouchableOpacity>
                )}
            />
        </View>
    );
};

export default HomeScreen;
