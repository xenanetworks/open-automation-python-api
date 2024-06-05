Eye Diagram
=========================

Information
-----------------
Read out BER eye-measurement information such as the vertical and horizontal
bathtub curve information on a 25G serdes. This must be called after "PP_EYEMEASURE"
has run to return valid results.  Use "get" to see the status of the data
gathering process.

Corresponding CLI command: ``PP_EYEINFO``

.. code-block:: python

    # Eye Diagram Information
    resp = await port.serdes[0].eye_diagram.info.get()
    resp.width_mui
    resp.height_mv
    resp.h_slope_left
    resp.h_slope_right
    resp.y_intercept_left
    resp.y_intercept_right
    resp.r_squared_fit_left
    resp.r_squared_fit_right
    resp.est_rj_rms_left
    resp.est_rj_rms_right
    resp.est_dj_pp
    resp.v_slope_bottom
    resp.v_slope_top
    resp.x_intercept_bottom
    resp.x_intercept_top
    resp.r_squared_fit_bottom
    resp.r_squared_fit_top
    resp.est_rj_rms_bottom
    resp.est_rj_rms_top


Bit Error Rate
-----------------
Obtain BER estimations of an eye diagram.

Corresponding CLI command: ``PP_EYEBER``

.. code-block:: python

    # Eye Diagram Bit Error Rate
    resp = await port.serdes[0].eye_diagram.ber.get()
    resp.eye_ber_estimation


Dwell Bits
-----------------
Min and max dwell bits for an eye capture.

Corresponding CLI command: ``PP_EYEDWELLBITS``

.. code-block:: python

    # Eye Diagram Dwell Bits
    resp = await port.serdes[0].eye_diagram.dwell_bits.get()
    resp.max_dwell_bit_count
    resp.min_dwell_bit_count


Measure
-----------------
Start/stop a new BER eye-measure on a 25G serdes. Use "get" to see the status of
the data gathering process.

Corresponding CLI command: ``PP_EYEMEASURE``

.. code-block:: python

    # Eye Diagram Measure
    resp = await port.serdes[0].eye_diagram.measure.get()
    resp.status


Resolution
-----------------
Set or get the resolution used for the next BER eye-measurement.

Corresponding CLI command: ``PP_EYERESOLUTION``

.. code-block:: python

    # Eye Diagram Resolution
    resp = await port.serdes[0].eye_diagram.resolution.get()
    resp.x_resolution
    resp.y_resolution


Data Columns
-----------------
Read a single column of a measured BER eye on a 25G serdes. Every readout also
returns the resolution (x,y) and the number of valid columns (used to facilitate
reading out the eye while it is being measured).

.. note::
    The columns of the eye-data will be measured in the order: xres-1, xres-2, xres-3, ... 0. The values show the number of bit errors measured out of a total of 1M bits at each of the individual sampling points (x=timeaxis, y = 0/1 threshold).

Corresponding CLI command: ``PP_EYEREAD``

.. code-block:: python

    # Eye Diagram Data Columns
    resp = await port.serdes[0].eye_diagram.read_column[0].get()
    resp.valid_column_count
    resp.values
    resp.x_resolution
    resp.y_resolution