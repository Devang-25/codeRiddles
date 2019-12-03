from generator_pipelined import *

delta_set = [
    {
        "type": "updateParagraph",
        "index": "p0",
        "text": "aaaAAaaa"
    },
    {
        "type": "addParagraph",
        "index": "p1",
        "text": "aaaAAaaa"
    },
    {
        "type": "updateParagraph",
        "index": "p5",
        "text": "EEeeeEEEEE"
    },
    {
        "type": "deleteParagraph",
        "index": "p0",
    },
]


def apply_delta(operations):
    for op in operations:
        if op == "updateParagraph":
            pass
        if op == "addParagraph":
            pass
        if op == "deleteParagraph":
            pass


if __name__ == '__main__':

    # para
    pc = [{'id': 'p0', 'text': 'aaa'},
          {'id': 'p1', 'text': 'bbb'},
          {'id': 'p2', 'text': 'ccc'},
          {'id': 'p3', 'text': 'ddd'},
          {'id': 'p4', 'text': 'eee'},
          {'id': 'p5', 'text': 'fff'},
          {'id': 'p6', 'text': 'ggg'},
          {'id': 'p7', 'text': 'hhh'}]

    # sections
    sec_case_1 = [
        {'id': 's0', 'ind': 0},
        {'id': 's1', 'ind': 2},
        {'id': 's2', 'ind': 4},
        {'id': 's3', 'ind': 6}
    ]

    # section pattern 2 for testing
    sec_case_2 = [
        {'id': 's0', 'ind': 0},
        {'id': 's1', 'ind': 4},
        {'id': 's3', 'ind': 6}
    ]


    # replace with 'sec_case_2' here for new pattern
    generated_content = (l for l in gen_content(sec_case_1, pc))

    if DEBUG:
        print('nothing executed yet. generator pipelining is cool')
        print("output: ")

    print('\n-\n'.join(generated_content))
