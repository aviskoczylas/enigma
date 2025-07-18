===================================
Enigma Tips and Tricks
===================================

This guide is most helpful after having done some easier puzzles already, and is meant mainly for with more difficult puzzles.
Throughout this guide, we'll refer to this puzzle as an example, but these tips can really be applied to any puzzle!

.. figure:: ../sample\ puzzles/board\ a/1/jump.png
    :align: center



Concentrations of letters
-------------------------

If you have experience with similar grid-filling puzzles, you may gravitate toward the bottom left of the grid for this puzzle, since it seems to be the most restricted area and therefore the easiest to work with. However, we will see that it is actually much more helpful to start on the left side of the board. 

As you start each puzzle, I highly recommend locating each letter of the keyword and noting which ones are close to each other, as well as which are in convenient areas. For example, if a word contains the letter 'a', if there are no other nearby letters, there are only three pieces that can reveal the 'a'. This can be a vital piece of starting knowledge, especially when one or more of those pieces cannot be used. In general, letters near the edges of the board are the most useful, and often make for the best starting points when other keyword letters are nearby.

For this puzzle, we immediately notice that 'j' and 'u' are next to each other on the far left of the board. After trying all of the pieces, we can quickly find that there are only 8 possible configurations that could possibly reveal both 'j' and 'u' while revealing no other letters, shown below.

|c1| |c2| |c3| |c4| |c5| |c6| |c7| |c8|


.. |c1| image:: images/c1.png
    :width: 11%
.. |c2| image:: images/c2.png
    :width: 13%
.. |c3| image:: images/c3.png
    :width: 15%
.. |c4| image:: images/c4.png
    :width: 16%
.. |c5| image:: images/c5.png
    :width: 10%
.. |c6| image:: images/c6.png
    :width: 10%
.. |c7| image:: images/c7.png
    :width: 10%
.. |c8| image:: images/c8.png
    :width: 10%

Looking for constraints based on letters rather than geometry is crucial for puzzles with very few starting pieces.

Symmetry
--------

While 8 configurations is a lot, half of these can actually be eliminated immediately. The rules mention that **EACH PUZZLE HAS ONLY ONE POSSIBLE SOLUTION**. While this may just seem like a fun fact, it can actually be very useful in solving puzzles if you use it cleverly. In the cases above, notice that configurations 5 and 6 have the same shape, use the same pieces, and reveal the same letters. This means that no matter how the rest of the board is set up, these two configurations are interchangeable, so a puzzle with one of these configurations as a solution cannot have only one solution! Since the puzzle only has one solution, these configurations need not be considered. The same logic applies to configurations 7 and 8, leaving us with only 1, 2, 3, and 4. This reveals an important conclusion: the zigzag piece must be in one of the two spots above!

I like to call this method of elimination symmetry, since it occurs where there is a line of symmetry along the configuration. Some other examples of configurations that can be eliminated via symmetry are shown below. 

|p1|       |p2|

.. |p1| image:: images/sym.png
    :width: 33%
.. |p2| image:: images/sym2.png
    :width: 45%

Importantly, the piece's holes must be symmetrical as well: just like the shape itself, the revealed letters (or lack thereof) must be mirrored across the line of symmetry or else the configurations are not interchangeable (this is an oversimplification - the strategy can still work in cases where this is not true, but it will always work when it is true). Below is an example of the shape having a line of symmetry, but we can see that this won't work when mirrored.

|p3| |p4|

.. |p3| image:: images/fake_sym.png
    :width: 45%
.. |p4| image:: images/fake_sym_flipped.png
    :width: 45%

Note that a symmetry elimination cannot be used on a starter piece, since this piece is not interchangeable.

Symmetry can also be used to eliminate confiugrations based on the leftover space in the grid as well as the pieces that have been placed. For example, say you started the puzzle like so:

..  figure:: images/blank_sym.png
    :align: center

A symmetry argument cannot be made based on the pieces, since the holes are not symmetrical and a starter piece is involved. However, the blank space left on the board is symmetrical horizontally, as are the remaining keyword letters j, u, and m. This means that for any configuration that could solve the puzzle, that same configuration could be flipped upside down and also be a solution. Since the puzzle only has one solution, no such configuration can exist, so the current setup can be eliminated.

These aren't the only ways that you can use the "only one solution" rule to your advantage, so don't be afraid to get creative! Using it is never necessary, but can save you a lot of effort (and make you feel smart)!

Pieces with two holes
---------------------

This tip is particularly useful for board A, but if you're smart about it, these principles can be applied to other boards as well. However, I'll only discuss board A here for the sake of simplicity.

Another good thing to do when starting a puzzle, once you have located all required letters, is to see it any pieces with two holes can cover multiple letters. **Due to the unique position of the holes on 2-hole pieces, the pieces will only cover 2 or 0 letters, never just 1 on board A.** In the case of the 'jump' puzzle, there is one piece that can cover two letters, shown below in both configurations.

|f1| |f2|

.. |f1| image:: images/Figure_1.png
    :width: 45%

.. |f2| image:: images/Figure_2.png
    :width: 45%

Let's assume these configurations are shown to not work (hint - they don't). **We then know that no piece with 2 holes can reveal a letter.** This extra information can be very useful when trying to figure out what options you have for filling a part of the grid.

Flippable pieces
----------------

There are 3 pieces that can maintain the same shape on the board while changing what holes they cover. In some cases they can even "choose" whether or not to cover a letter at all. On board A specifically, only the zigzag piece can do this, as shown below. This property can be a very powerful tool, so make sure to take full advantage of this flexibility!

|z1| |z2|

.. |z1| image:: images/zig.png
    :width: 30%

.. |z2| image:: images/zag.png
    :width: 29%

