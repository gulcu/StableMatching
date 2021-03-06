# A Solution to the Stable Matching Problem
A Gale-Shapley algorithm implementation in Python.

The program explains each step of the algorithm in quite a chatty manner both in comments and in output :)

Below is an example run, where 4 men numbered from 0 to 3 are to be stably matched with 4 women, again numbered 0 to 3.

All matchings are stable if there is no man-woman pair who would both prefer each other to their currently assigned partners!

Unmarried men: (0, 1, 2, 3)

Unmarried women: (0, 1, 2, 3)

Man 0 is matched with Woman 0 with her pref-level: 3



Unmarried men: (1, 2, 3)

Unmarried women: (1, 2, 3)

Woman 0 was previously assigned to Man 0

Man 2 is matched with Woman 0 with her pref-level: 2

Man 0 is now free



Unmarried men: (1, 3, 0)

Unmarried women: (1, 2, 3)

Woman 0 was previously assigned to Man 2

Man 1 is matched with Woman 0 with her pref-level: 1

Man 2 is now free



Unmarried men: (3, 0, 2)

Unmarried women: (1, 2, 3)

Man 2 is rejected by Woman 0 , he will consider Woman 1 next



Unmarried men: (3, 0, 2)

Unmarried women: (1, 2, 3)

Man 3 is matched with Woman 3 with her pref-level: 3



Unmarried men: (0, 2)

Unmarried women: (1, 2)

Man 0 is rejected by Woman 0 , he will consider Woman 1 next



Unmarried men: (0, 2)

Unmarried women: (1, 2)

Woman 3 was previously assigned to Man 3

Man 2 is matched with Woman 3 with her pref-level: 2

Man 3 is now free



Unmarried men: (0, 3)

Unmarried women: (1, 2)

Man 3 is rejected by Woman 3 , he will consider Woman 1 next



Unmarried men: (0, 3)

Unmarried women: (1, 2)

Man 0 is matched with Woman 1 with her pref-level: 3



Unmarried men: (3)

Unmarried women: (2)

Woman 1 was previously assigned to Man 0

Man 3 is matched with Woman 1 with her pref-level: 2

Man 0 is now free



Unmarried men: (0)

Unmarried women: (2)

Man 0 is rejected by Woman 1 , he will consider Woman 2 next



Unmarried men: (0)

Unmarried women: (2)

Man 0 is matched with Woman 2 with her pref-level: 0



Man # 0 gets married to Woman # 2

Man # 1 gets married to Woman # 0

Man # 2 gets married to Woman # 3

Man # 3 gets married to Woman # 1

========= THE HAPPY END =========

Or, is it? It is NOT the **happiest** end for everyone! Why?
Because the assignment process is not symmetric between the men and the women.
If we were to start assigning the women to the men instead of the men to the women,
the women would have been matched with men of their higher preferences!

