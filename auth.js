import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import ProductFeed from './screens/ProductFeed';
import ProductDetail from './screens/ProductDetail';

const AppNavigator = createStackNavigator({
  Feed: ProductFeed,
  Detail: ProductDetail,
});

export default createAppContainer(AppNavigator);
