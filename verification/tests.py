"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[(2015, 1, 12, 10, 0, 0),
        (2015, 1, 12, 10, 10, 10),
        (2015, 1, 12, 11, 0, 0),
        (2015, 1, 12, 11, 10, 10),]],
            "answer": 1220,
        },
        {
            "input": [[(2015, 1, 12, 10, 0, 0),
        (2015, 1, 12, 10, 10, 10),]],
            "answer": 610,
        },
        {
            "input": [[(2015, 1, 12, 10, 0, 0),
        (2015, 1, 12, 10, 10, 10),
        (2015, 1, 12, 11, 0, 0),
        (2015, 1, 12, 11, 10, 10),
        (2015, 1, 12, 12, 10, 10),]],
            "answer": 4820,
        },
        {
            "input": [[(2015, 1, 12, 10, 0, 0),
        (2015, 1, 12, 10, 0, 1),]],
            "answer": 1,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0 , 0),
                    (2015, 1, 12, 10, 0 , 10),
                    (2015, 1, 12, 11, 0 , 0),
                    (2015, 1, 13, 11, 0 , 0),
                ]
            ],
            "answer": 86410
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                [2015, 1, 12, 10, 0, 5]
            ],
            "answer": 5,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                [2015, 1, 12, 10, 0, 0]
            ],
            "answer": 10,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                [2015, 1, 12, 11, 0, 0]
            ],
            "answer": 610,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                [2015, 1, 12, 11, 0, 10]
            ],
            "answer": 600,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                [2015, 1, 12, 10, 10, 0]
            ],
            "answer": 620,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                    (2015, 1, 12, 12, 10, 10),
                ],
                [2015, 1, 12, 12, 10, 10]
            ],
            "answer": 0,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                    (2015, 1, 12, 12, 10, 10),
                ],
                [2015, 1, 12, 12, 9, 10]
            ],
            "answer": 60,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                    (2015, 1, 12, 12, 10, 10),
                
                ],
                [2015, 1, 12, 11, 10, 0]
            ],
            "answer": 3610,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                [2015, 1, 12, 10, 0, 0],
                [2015, 1, 12, 10, 0, 10]
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                (2015, 1, 12, 10, 0, 0),
                (2015, 1, 12, 10, 0, 7) 
            ],
            "answer": 7
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                (2015, 1, 12, 10, 0, 3),
                (2015, 1, 12, 10, 0, 10)
            ],
            "answer": 7
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                ],
                (2015, 1, 12, 10, 0, 10),
                (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 0
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 10, 30, 0),
                (2015, 1, 12, 11, 0, 0)
            ],
            "answer": 0
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 10, 10, 0),
                (2015, 1, 12, 11, 0, 0)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 10, 10, 0),
                (2015, 1, 12, 11, 0, 10)
            ],
            "answer": 20
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 9, 50, 0),
                (2015, 1, 12, 10, 0, 10)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 9, 0, 0),
                (2015, 1, 12, 10, 5, 0)
            ],
            "answer": 300
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                ],
                (2015, 1, 12, 11, 5, 0),
                (2015, 1, 12, 12, 0, 0)
            ],
            "answer": 310
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                ],
                (2015, 1, 12, 11, 5, 0),
                (2015, 1, 12, 11, 10, 0)
            ],
            "answer": 300
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                ],
                (2015, 1, 12, 10, 10, 0),
                (2015, 1, 12, 11, 0, 10)
            ],
            "answer": 20
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                ],
                (2015, 1, 12, 9, 10, 0),
                (2015, 1, 12, 10, 20, 20)
            ],
            "answer": 610
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                ],
                (2015, 1, 12, 9, 10, 0),
                (2015, 1, 12, 10, 20, 20)
            ],
            "answer": 1220
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                ],
                (2015, 1, 12, 9, 9, 0),
                (2015, 1, 12, 10, 0, 0)
            ],
            "answer": 0
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                ],
                (2015, 1, 12, 9, 9, 0),
                (2015, 1, 12, 10, 0, 10)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    ((2015, 1, 12, 10, 0, 0), 2),
                    (2015, 1, 12, 10, 0, 10),
                    ((2015, 1, 12, 10, 1, 0), 2),
                ]
            ],
            "answer": 60
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 0, 10),
                    ((2015, 1, 12, 11, 0, 0), 2),
                    ((2015, 1, 12, 11, 1, 0), 2),
                ]
            ],
            "answer": 70
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ]
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ]
            ],
            "answer": 40
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                    ((2015, 1, 12, 10, 1, 0), 3),
                    ((2015, 1, 12, 10, 1, 20), 3),
                ]
            ],
            "answer": 60
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    ((2015, 1, 12, 10, 0, 0), 2),
                    (2015, 1, 12, 10, 0, 10),
                    ((2015, 1, 12, 10, 1, 0), 2),
                ], (2015, 1, 12, 10, 0, 50)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 30)
            ],
            "answer": 20
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 10)
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 50)
            ],
            "answer": 0
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 30)
            ],
            "answer": 20
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                    ((2015, 1, 12, 10, 1, 20), 2),
                    ((2015, 1, 12, 10, 1, 40), 2),
                ], (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 50
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    ((2015, 1, 12, 10, 0, 0), 2),
                    (2015, 1, 12, 10, 0, 10),
                    ((2015, 1, 12, 10, 1, 0), 2),
                ], (2015, 1, 12, 10, 0, 30), (2015, 1, 12, 10, 1, 0)
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    ((2015, 1, 12, 10, 0, 0), 2),
                    (2015, 1, 12, 10, 0, 10),
                    ((2015, 1, 12, 10, 1, 0), 2),
                ], (2015, 1, 12, 10, 0, 20), (2015, 1, 12, 10, 1, 0)
            ],
            "answer": 40
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    ((2015, 1, 12, 10, 0, 0), 2),
                    (2015, 1, 12, 10, 0, 10),
                ], (2015, 1, 12, 10, 0, 0), (2015, 1, 12, 10, 0, 30)
            ],
            "answer": 30
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 0), (2015, 1, 12, 10, 1, 0)
            ],
            "answer": 40
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 0), (2015, 1, 12, 10, 0, 10)
            ],
            "answer": 0
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                    (2015, 1, 12, 10, 0, 40),
                    ((2015, 1, 12, 10, 0, 50), 2),
                ], (2015, 1, 12, 10, 0, 10), (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                ], (2015, 1, 12, 10, 0, 10), (2015, 1, 12, 10, 0, 20)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    ((2015, 1, 12, 10, 0, 10), 3),
                    (2015, 1, 12, 10, 0, 20),
                    ((2015, 1, 12, 10, 0, 30), 3),
                    ((2015, 1, 12, 10, 0, 30), 2),
                ], (2015, 1, 12, 10, 0, 10), (2015, 1, 12, 10, 0, 30)
            ],
            "answer": 20
        },
        {
            "input": [
                [
                    ((2015, 1, 11, 0, 0, 0), 3),
                    (2015, 1, 12, 0, 0, 0),
                    ((2015, 1, 13, 0, 0, 0), 3),
                    ((2015, 1, 13, 0, 0, 0), 2),
                    (2015, 1, 14, 0, 0, 0),
                    ((2015, 1, 15, 0, 0, 0), 2),
                ], (2015, 1, 10, 0, 0, 0), (2015, 1, 16, 0, 0, 0)
            ],
            "answer": 345600
        }
    ],
    "Extra": [
        {
            "input": [[(2015, 1, 12, 10, 0, 0),
        (2015, 1, 12, 10, 0, 10),]],
            "answer": 10,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0, 0),
                    (2015, 1, 12, 10, 10, 10),
                    (2015, 1, 12, 11, 0, 0),
                    (2015, 1, 12, 11, 10, 10),
                    (2015, 1, 12, 12, 10, 10),
                ],
                [2015, 1, 12, 11, 10, 20]
            ],
            "answer": 3590,
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0 , 0),
                    (2015, 1, 12, 10, 10 , 10),
                    (2015, 1, 12, 11, 0 , 0),
                ],
                (2015, 1, 12, 10, 5 , 0),
                (2015, 1, 12, 10, 20 , 20)
            ],
            "answer": 310
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0 , 0),
                    (2015, 1, 12, 10, 0 , 10),
                ],
                (2015, 1, 11, 0, 0 , 0),
                (2015, 1, 13, 0, 0 , 0)
            ],
            "answer": 10
        },
        {
            "input": [
                [
                    (2015, 1, 12, 10, 0 , 0),
                    (2015, 1, 12, 10, 10 , 10),
                    (9999, 1, 12, 11, 0 , 0),
                    (9999, 1, 12, 11, 10 , 10),
                ]
            ],
            "answer": 1220
        },
        {
            "input": [
                [
                    ((9999, 1, 12, 10, 0, 10), 3),
                    (9999, 1, 12, 10, 0, 20),
                    ((9999, 1, 12, 10, 0, 30), 3),
                    ((9999, 1, 12, 10, 0, 30), 2),
                ], (9999, 1, 12, 10, 0, 10), (9999, 1, 12, 10, 0, 20)
            ],
            "answer": 10
        }
    ]
}
