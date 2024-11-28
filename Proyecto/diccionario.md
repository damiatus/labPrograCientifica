## _Made by ChatGPT, puede tener errores_

| Variable                                  | Tipo de dato | Descripción                                                                                     |
| ----------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------- |
| `borrow_block_number`                     | Numérica     | Número del bloque en el que se realizó el préstamo.                                             |
| `borrow_timestamp`                        | Numérica     | Marca de tiempo (timestamp) del momento en que se realizó el préstamo.                          |
| `wallet_address`                          | Categórica   | Dirección de la billetera asociada al usuario.                                                  |
| `first_tx_timestamp`                      | Numérica     | Marca de tiempo de la primera transacción del usuario.                                          |
| `last_tx_timestamp`                       | Numérica     | Marca de tiempo de la última transacción del usuario.                                           |
| `wallet_age`                              | Numérica     | Tiempo (en días o años) desde la creación de la billetera.                                      |
| `incoming_tx_count`                       | Numérica     | Número total de transacciones entrantes.                                                        |
| `outgoing_tx_count`                       | Numérica     | Número total de transacciones salientes.                                                        |
| `net_incoming_tx_count`                   | Numérica     | Número neto de transacciones entrantes (entrantes - salientes).                                 |
| `total_gas_paid_eth`                      | Numérica     | Total de gas pagado en transacciones, expresado en Ethereum (ETH).                              |
| `avg_gas_paid_per_tx_eth`                 | Numérica     | Promedio de gas pagado por transacción, en Ethereum (ETH).                                      |
| `risky_tx_count`                          | Numérica     | Número de transacciones consideradas de alto riesgo.                                            |
| `risky_unique_contract_count`             | Numérica     | Número de contratos únicos de alto riesgo involucrados en transacciones.                        |
| `risky_first_tx_timestamp`                | Numérica     | Marca de tiempo de la primera transacción arriesgada.                                           |
| `risky_last_tx_timestamp`                 | Numérica     | Marca de tiempo de la última transacción arriesgada.                                            |
| `risky_first_last_tx_timestamp_diff`      | Numérica     | Diferencia entre la primera y última transacción arriesgada (en días o segundos).               |
| `risky_sum_outgoing_amount_eth`           | Numérica     | Suma total de cantidades salientes en transacciones arriesgadas, expresado en Ethereum (ETH).   |
| `outgoing_tx_sum_eth`                     | Numérica     | Suma total de todas las transacciones salientes en Ethereum (ETH).                              |
| `incoming_tx_sum_eth`                     | Numérica     | Suma total de todas las transacciones entrantes en Ethereum (ETH).                              |
| `outgoing_tx_avg_eth`                     | Numérica     | Promedio de transacciones salientes en Ethereum (ETH).                                          |
| `incoming_tx_avg_eth`                     | Numérica     | Promedio de transacciones entrantes en Ethereum (ETH).                                          |
| `max_eth_ever`                            | Numérica     | Máxima cantidad de Ethereum (ETH) que ha tenido la billetera.                                   |
| `min_eth_ever`                            | Numérica     | Mínima cantidad de Ethereum (ETH) que ha tenido la billetera.                                   |
| `total_balance_eth`                       | Numérica     | Balance total de Ethereum (ETH) en la billetera.                                                |
| `risk_factor`                             | Numérica     | Factor de riesgo calculado para la billetera o transacción.                                     |
| `total_collateral_eth`                    | Numérica     | Total de garantía en Ethereum (ETH) utilizada.                                                  |
| `total_collateral_avg_eth`                | Numérica     | Promedio de garantías en Ethereum (ETH) a lo largo del tiempo.                                  |
| `total_available_borrows_eth`             | Numérica     | Total disponible para préstamos en Ethereum (ETH).                                              |
| `total_available_borrows_avg_eth`         | Numérica     | Promedio disponible para préstamos en Ethereum (ETH).                                           |
| `avg_weighted_risk_factor`                | Numérica     | Promedio ponderado del factor de riesgo de todas las transacciones.                             |
| `risk_factor_above_threshold_daily_count` | Numérica     | Número de días en que el factor de riesgo superó el umbral establecido.                         |
| `avg_risk_factor`                         | Numérica     | Promedio del factor de riesgo de todas las transacciones realizadas.                            |
| `max_risk_factor`                         | Numérica     | Valor máximo alcanzado por el factor de riesgo.                                                 |
| `borrow_amount_sum_eth`                   | Numérica     | Suma total de los montos prestados en Ethereum (ETH).                                           |
| `borrow_amount_avg_eth`                   | Numérica     | Promedio de los montos prestados en Ethereum (ETH).                                             |
| `borrow_count`                            | Numérica     | Número total de préstamos realizados.                                                           |
| `repay_amount_sum_eth`                    | Numérica     | Suma total de los montos pagados en repagos en Ethereum (ETH).                                  |
| `repay_amount_avg_eth`                    | Numérica     | Promedio de los montos pagados en repagos en Ethereum (ETH).                                    |
| `repay_count`                             | Numérica     | Número total de pagos de préstamos realizados.                                                  |
| `borrow_repay_diff_eth`                   | Numérica     | Diferencia entre los montos prestados y los repagos realizados en Ethereum (ETH).               |
| `deposit_count`                           | Numérica     | Número total de depósitos realizados.                                                           |
| `deposit_amount_sum_eth`                  | Numérica     | Suma total de los montos depositados en Ethereum (ETH).                                         |
| `time_since_first_deposit`                | Numérica     | Tiempo transcurrido desde el primer depósito (en días o años).                                  |
| `withdraw_amount_sum_eth`                 | Numérica     | Suma total de los montos retirados en Ethereum (ETH).                                           |
| `withdraw_deposit_diff_if_positive_eth`   | Numérica     | Diferencia entre los retiros y depósitos, solo si es positiva (en Ethereum ETH).                |
| `liquidation_count`                       | Numérica     | Número de veces que la cuenta ha sido liquidada.                                                |
| `time_since_last_liquidated`              | Numérica     | Tiempo transcurrido desde la última liquidación (en días o años).                               |
| `liquidation_amount_sum_eth`              | Numérica     | Suma total de la cantidad liquidada en Ethereum (ETH).                                          |
| `market_adx`                              | Numérica     | Indicador de dirección promedio (ADX), utilizado para medir la fuerza de una tendencia.         |
| `market_adxr`                             | Numérica     | Indicador de dirección promedio suavizado (ADXR), versión ajustada de ADX.                      |
| `market_apo`                              | Numérica     | Oscilador de precios (APO), utilizado para identificar tendencias.                              |
| `market_aroonosc`                         | Numérica     | Oscilador Aroon, usado para medir la duración de una tendencia.                                 |
| `market_aroonup`                          | Numérica     | Indicador Aroon hacia arriba, utilizado para medir la fuerza de una tendencia alcista.          |
| `market_atr`                              | Numérica     | Rango verdadero promedio (ATR), utilizado para medir la volatilidad del mercado.                |
| `market_cci`                              | Numérica     | Índice de canal de mercancías (CCI), usado para identificar ciclos en el mercado.               |
| `market_cmo`                              | Numérica     | Oscilador de momentum (CMO), utilizado para medir la velocidad del precio.                      |
| `market_correl`                           | Numérica     | Correlación entre dos activos o series temporales en el mercado.                                |
| `market_dx`                               | Numérica     | Indicador de movimiento direccional (DX), usado para evaluar la tendencia del mercado.          |
| `market_fastk`                            | Numérica     | %K rápido en el estocástico, utilizado para identificar señales de compra/venta.                |
| `market_fastd`                            | Numérica     | %D rápido en el estocástico, utilizado junto con %K para confirmar señales de trading.          |
| `market_ht_trendmode`                     | Categórica   | Modo de tendencia según el filtro de Hilbert (HT).                                              |
| `market_linearreg_slope`                  | Numérica     | Pendiente de la regresión lineal, utilizada para medir la inclinación de la tendencia.          |
| `market_macd_macdext`                     | Numérica     | Extensión del indicador MACD (Media móvil de convergencia/divergencia).                         |
| `market_macd_macdfix`                     | Numérica     | Versión ajustada del indicador MACD.                                                            |
| `market_macd`                             | Numérica     | Media móvil de convergencia/divergencia (MACD), usado para identificar cambios de tendencia.    |
| `market_macdsignal_macdext`               | Numérica     | Señal extendida del indicador MACD.                                                             |
| `market_macdsignal_macdfix`               | Numérica     | Señal ajustada del indicador MACD.                                                              |
| `market_macdsignal`                       | Numérica     | Señal del MACD, utilizado para identificar puntos de compra/venta.                              |
| `market_max_drawdown_365d`                | Numérica     | Máxima disminución en valor durante 365 días.                                                   |
| `market_natr`                             | Numérica     | Rango verdadero normalizado (NATR), utilizado para medir la volatilidad relativa.               |
| `market_plus_di`                          | Numérica     | Indicador de direccionalidad positiva (DI+), utilizado para medir la fuerza de las tendencias.  |
| `market_plus_dm`                          | Numérica     | Indicador de movimiento direccional positivo (DM+), usado para identificar tendencias.          |
| `market_ppo`                              | Numérica     | Oscilador de precio ponderado (PPO), usado para comparar dos medias móviles.                    |
| `market_rocp`                             | Numérica     | Tasa de cambio del precio (ROCP), usada para evaluar la velocidad de los movimientos de precio. |
| `market_rocr`                             | Numérica     | Tasa de cambio relativa del precio (ROCR), usada para comparar activos.                         |
| `unique_borrow_protocol_count`            | Numérica     | Número de protocolos de préstamo únicos utilizados.                                             |
| `unique_lending_protocol_count`           | Numérica     | Número de protocolos de préstamo únicos utilizados.                                             |
