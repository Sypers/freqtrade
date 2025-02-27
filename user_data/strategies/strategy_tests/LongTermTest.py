import unittest

import pandas
import user_data.strategies.Longterm as strategy


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # Load Dataframes with pair data used for testing
        self.dataframe = pandas.read_json('BTC_USDT-1d.json')  # Dataframe to test indicator values
        self.dataframe.rename(columns={0: 'date', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'},
                              inplace=True)
        self.df_enter = pandas.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'], dtype=float, data=
        [[1581897600000, 9910.7, 9964.16, 9452.67, 9706.0, 70261.011901],
         [1581984000000, 9706.0, 10250.0, 9576.01, 10164.71, 70604.124019],
         [1582070400000, 10164.78, 10250.0, 9350.0, 9593.79, 55162.586895],
         [1582156800000, 9594.65, 9699.0, 9400.0, 9596.42, 60152.342914],
         [1582243200000, 9597.21, 9755.51, 9550.21, 9677.05, 42181.554524],
         [1582329600000, 9677.05, 9709.17, 9560.02, 9650.86, 24636.757623],
         [1582416000000, 9650.85, 9990.0, 9645.0, 9936.4, 37702.089843],
         [1582502400000, 9936.4, 9990.0, 9473.56, 9656.13, 55796.59612],
         [1582588800000, 9655.52, 9675.0, 9250.0, 9315.84, 54379.344552],
         [1582675200000, 9316.48, 9377.44, 8633.63, 8785.25, 92130.345482],
         [1582761600000, 8786.0, 8971.77, 8531.0, 8823.21, 72483.578762],
         [1582848000000, 8823.25, 8900.0, 8445.0, 8692.91, 71155.208977],
         [1582934400000, 8690.8, 8790.0, 8523.55, 8523.61, 36748.183035],
         [1583020800000, 8523.61, 8750.0, 8411.0, 8531.88, 43892.201779],
         [1583107200000, 8530.3, 8965.75, 8498.0, 8915.24, 60401.31773],
         [1583193600000, 8911.18, 8919.65, 8651.0, 8760.07, 55154.997282],
         [1583280000000, 8760.07, 8848.29, 8660.0, 8750.87, 38696.482578],
         [1583366400000, 8750.99, 9159.42, 8746.54, 9054.68, 58201.866355],
         [1583452800000, 9054.64, 9170.0, 8985.5, 9131.88, 43782.948044],
         [1583539200000, 9130.89, 9188.0, 8835.0, 8886.66, 45422.204525],
         [1583625600000, 8885.25, 8886.76, 8000.0, 8033.31, 77537.315166],
         [1583712000000, 8034.76, 8179.31, 7632.01, 7929.87, 116968.863268],
         [1583798400000, 7929.87, 8149.0, 7728.01, 7894.56, 86783.443875],
         [1583884800000, 7894.57, 7980.0, 7590.0, 7934.52, 79942.411172],
         [1583971200000, 7934.58, 7966.17, 4410.0, 4800.0, 261505.608653]])  # Expected buy signal

        self.df_exit = pandas.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'], dtype=float, data=
        [[1585008000000, 6465.25, 6833.0, 6371.33, 6744.72, 151138.009878],
         [1585094400000, 6744.69, 6957.96, 6450.0, 6677.43, 132155.734989],
         [1585180800000, 6677.42, 6780.0, 6510.0, 6737.36, 83026.555211],
         [1585267200000, 6737.27, 6842.59, 6261.0, 6359.11, 82914.968354],
         [1585353600000, 6359.11, 6360.0, 6024.0, 6236.65, 93159.693429],
         [1585440000000, 6236.65, 6266.0, 5866.56, 5881.42, 63311.627714],
         [1585526400000, 5880.5, 6599.0, 5857.76, 6394.38, 118889.549992],
         [1585612800000, 6394.45, 6523.23, 6321.4, 6410.44, 72337.595259],
         [1585699200000, 6412.14, 6679.94, 6150.11, 6642.92, 97500.7524],
         [1585785600000, 6643.36, 7198.0, 6551.0, 6794.09, 149299.906871],
         [1585872000000, 6793.86, 7048.0, 6602.1, 6734.1, 104080.276939],
         [1585958400000, 6732.97, 6990.41, 6650.01, 6856.99, 72990.861139],
         [1586044800000, 6857.41, 6895.54, 6677.52, 6772.78, 49685.356983],
         [1586131200000, 6772.78, 7355.14, 6765.0, 7329.9, 118052.000832],
         [1586217600000, 7329.9, 7459.69, 7077.0, 7197.32, 103585.168918],
         [1586304000000, 7197.32, 7420.0, 7150.0, 7361.28, 76059.145838],
         [1586390400000, 7360.26, 7371.92, 7108.08, 7283.54, 61094.872417],
         [1586476800000, 7283.54, 7295.75, 6739.98, 6858.92, 104674.623375],
         [1586563200000, 6858.92, 6944.3, 6760.0, 6876.83, 45470.293206],
         [1586649600000, 6876.84, 7177.0, 6780.0, 6903.79, 73868.666501],
         [1586736000000, 6903.79, 6903.79, 6575.0, 6837.91, 96415.476573],
         [1586822400000, 6838.04, 6978.0, 6754.28, 6868.7, 69068.623285],
         [1586908800000, 6868.57, 6933.0, 6605.0, 6621.24, 61571.384994],
         [1586995200000, 6621.25, 7190.0, 6468.27, 7101.94, 125009.857539],
         [1587081600000, 7101.99, 7148.12, 6972.98, 7027.55, 54126.509763],
         [1587168000000, 7026.78, 7293.08, 7014.4, 7248.6, 49488.542819],
         [1587254400000, 7248.6, 7266.15, 7055.6, 7120.74, 45664.86393],
         [1587340800000, 7121.4, 7220.0, 6751.0, 6826.83, 90149.49137],
         [1587427200000, 6828.98, 6940.0, 6762.0, 6841.37, 60109.710808],
         [1587513600000, 6841.36, 7156.38, 6818.0, 7125.14, 61486.377334],
         [1587600000000, 7125.12, 7738.0, 7020.0, 7482.39, 102773.569561],
         [1587686400000, 7483.96, 7615.96, 7388.0, 7505.0, 60182.119939],
         [1587772800000, 7505.0, 7705.0, 7431.07, 7538.67, 43874.427726],
         [1587859200000, 7539.03, 7700.0, 7480.0, 7693.1, 50522.616209],
         [1587945600000, 7693.1, 7792.02, 7606.0, 7774.62, 65441.339576],
         [1588032000000, 7773.51, 7780.0, 7659.12, 7738.98, 46302.752638],
         [1588118400000, 7738.58, 8952.89, 7710.05, 8778.57, 183546.887514],
         [1588204800000, 8778.58, 9460.0, 8401.0, 8620.0, 206277.214124],
         [1588291200000, 8620.0, 9059.18, 8613.56, 8826.96, 91468.815059],
         [1588377600000, 8825.67, 9010.0, 8753.0, 8972.05, 59002.08755],
         [1588464000000, 8972.58, 9200.0, 8712.0, 8894.16, 90126.065643],
         [1588550400000, 8894.15, 8950.0, 8522.0, 8871.96, 84418.512331],
         [1588636800000, 8871.92, 9118.58, 8760.0, 9021.83, 76480.765342],
         [1588723200000, 9021.36, 9395.0, 8906.21, 9142.92, 105925.30242],
         [1588809600000, 9143.4, 10067.0, 9021.0, 9986.4, 147154.611378],
         [1588896000000, 9986.3, 10035.96, 9705.0, 9800.01, 100683.7964],
         [1588982400000, 9800.02, 9914.25, 9520.0, 9539.4, 81950.679567],
         [1589068800000, 9539.1, 9574.83, 8117.0, 8722.77, 183865.182028],
         [1589155200000, 8722.77, 9168.0, 8200.0, 8561.52, 168807.251832]])  # Expected sell signal
        self.metadata = {'pair': "BTC/USDT"}
        self.df_enter = strategy.Longterm.populate_indicators(strategy.Longterm, dataframe=self.df_enter,
                                                              metadata=self.metadata)
        self.df_exit = strategy.Longterm.populate_indicators(strategy.Longterm, dataframe=self.df_exit,
                                                             metadata=self.metadata)
        self.dataframe = strategy.Longterm.populate_indicators(strategy.Longterm, dataframe=self.dataframe,
                                                               metadata=self.metadata)

    def testEntrySignal(self):
        self.df_enter = strategy.Longterm.populate_entry_trend(strategy.Longterm, dataframe=self.df_enter,
                                                               metadata=self.metadata)
        # Test if a correct enter signal is generated using the strategy
        self.assertEqual(self.df_enter['enter_long'].iloc[-1], 1)

    def testExitSignal(self):
        self.df_exit = strategy.Longterm.populate_exit_trend(strategy.Longterm, dataframe=self.df_exit,
                                                             metadata=self.metadata)
        # Test if a correct exit signal is generated using the strategy
        self.assertEqual(self.df_exit['exit_long'].iloc[-1], 1)

    def testMACD(self):
        # Test if MACD and MACDSignal values are calculated correctly
        self.assertAlmostEqual(self.dataframe['macd'].iloc[153], 257.498547, places=2)
        self.assertAlmostEqual(self.dataframe['macdsignal'].iloc[153], 234.300375, places=2)

    def testRSI(self):
        # Test if MACD and MACDSignal values are calculated correctly
        self.assertAlmostEqual(self.dataframe['rsi'].iloc[153], 63.687091, places=2)


if __name__ == '__main__':
    unittest.main()
