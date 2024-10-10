Configuration
=========================

Enable
-----------------
Whether a filter is currently active on a port. While a filter is enabled its
condition cannot be changed, nor can any match term or length terms used by it.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_ENABLE`

.. code-block:: python

    await filter.enable.set(on_off=enums.OnOff.ON)
    await filter.enable.set_on()
    await filter.enable.set(on_off=enums.OnOff.OFF)
    await filter.enable.set_off()

    resp = await filter.enable.get()
    resp.on_off


Description
-----------
The description of a filter.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_COMMENT`

.. code-block:: python

    await filter.comment.set(comment="this is a comment")
    
    resp = await filter.comment.get()
    resp.comment


Condition
---------------
The boolean condition on the terms specifying when the filter is satisfied. The condition uses a canonical and-or-not expression on the match terms and length terms.

The condition is specified using a number of compound terms, each encoded as an integer value specifying an arbitrary set of the match terms
and length terms defined for the port. Each match or length term has a specific power-of-two value, and the set is encoded as the sum of the values for the contained terms:

Value for match term ``[match_term_xindex] = 2^match_term_xindex``

Value for length term ``[length_term_xindex] = 2^(length_term_xindex+16)``

A compound term is true if all the match terms and length terms contained in it are true. This supports the and-part of the condition.
If some compound term is satisfied, the condition as a whole is true.

This is the or-part of the condition. The first few compound terms at the even positions (second, fourth, ...) are inverted,
and all the contained match terms and length terms must be false at the same time that the those of the preceding compound term are true.
This is the not-part of the condition.

At the top level, a condition is a bunch of things or-ed together.

``<filter-condition> = <or-expr>``

Two of the or-operands are *general*, two are 'simple'.

``<or-expr> =  <general-and-expr>  or  <general-and-expr>  or  <simple-and-expr>  or  <simple-and-expr>``

A 'general' and-expression can include negated terms.

``<general-and-expr>  =  <term>  and  <term>  and ... and  not <term>  and ... and  not <term>``

A 'simple' and-expression can only have non-negated terms.

``<simple-and-expr>   =  <term>  and  <term>  and ... and <term>``

``<term>              =  <match-term>``

``<term>              =  <length-term>``

In practice, the simplest way to generate these encodings is to use the ValkyrieManager,
which supports Boolean expressions using the operators ``&, |, and ~``, and simply query the chassis for the resulting script-level definition.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_CONDITION`

.. code-block:: python

    await filter.condition.set(
        and_expression_0=0,
        and_not_expression_0=0,
        and_expression_1=0,
        and_not_expression_1=0,
        and_expression_2=0,
        and_expression_3=0
        )

    resp = await filter.condition.get()
    resp.and_expression_0
    resp.and_not_expression_0
    resp.and_expression_1
    resp.and_not_expression_1
    resp.and_expression_2
    resp.and_expression_3


String Representation
----------------------
The string representation of a filter.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_STRING`

.. code-block:: python

    await filter.string.set(string_name="this is a name")

    resp = await filter.string.get()
    resp.string_name