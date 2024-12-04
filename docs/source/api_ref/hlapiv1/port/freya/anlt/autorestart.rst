Autorestart
============

Enable/disable ANLT autorestart.

* AN+LT auto-restart when a link down condition is detected. A “link down” state signifies the loss of a valid input signal, which can occur due to events such as cable unplugging and re-plugging, TX disable, or link flap on the link partner’s end. The auto-restart process will continue until the link is re-established. Please note that this setting is only effective when AN and/or LT are enabled.

* If LT is enabled and experiences a failure on either side, the port will initiate the AN+LT restart process repeatedly until LT succeeds. This functionality is only applicable when LT is enabled.

.. code-block:: python

    await port_obj.l1.anlt.autorestart.set(values=[enums.FreyaAutorestartMode.OFF])
    await port_obj.l1.anlt.autorestart.set(values=[enums.FreyaAutorestartMode.WHEN_LINK_DOWN])
    await port_obj.l1.anlt.autorestart.set(values=[enums.FreyaAutorestartMode.WHEN_LT_FAILED])
    await port_obj.l1.anlt.autorestart.set(values=[enums.FreyaAutorestartMode.WHEN_LINK_DOWN_LT_FAILED])