Configuration
=========================

Type
-------------------------
Defines the PRBS type used when the interface is in PRBS mode.

Corresponding CLI command: ``PP_PRBSTYPE``

.. code-block:: python

    # PRBS Configuration
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS7, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.CAUI_VIRTUAL, 
        polynomial=enums.PRBSPolynomial.PRBS9, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.PERSECOND)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS10, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS11, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS13, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS15, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS20, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS23, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS31, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS49, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS58, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)

    resp = await port.serdes[0].prbs.config.type.get()
    resp.prbs_inserted_type
    resp.polynomial
    resp.invert
    resp.statistics_mode
